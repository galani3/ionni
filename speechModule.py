import pyaudio
import wave
import requests
from urllib.parse import quote

def playback(audio):    
    CHUNK = 1024
    wf = audio
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)
    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)
        if(len(data) <= 0):
            break

    stream.stop_stream()
    stream.close()
    p.terminate()

def speak(expression):
    audio_file = open("response.wav", "wb")
    req = requests.get("https://watson-api-explorer.mybluemix.net/text-to-speech/api/v1/synthesize?accept=audio%2Fwav&voice=en-US_AllisonVoice&text=" + quote(expression))
    speech_response = req.content
    audio_file.write(speech_response)
    playback(wave.open("response.wav", "rb"))
