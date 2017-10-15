import requests
import json
import random
import wave
import pyaudio
from datetime import datetime, time
from speechModule import speak
from urllib.parse import quote

AI_headers = {"Authorization": "Bearer SWGJMUXX6OKCGYETBXG367MI2EAD3535"}

print("    .: Beta AI :.   ")

speak("Hello, my name is e-own-e. What can I help you with")

while(1):
    userInput = input("What can I help you with? >> ")
    try:
        if(userInput != "Goodbye" and userInput != "goodbye" and userInput != "Good bye" and userInput != "good bye"):
            req = requests.get("https://api.wit.ai/message?v=20170727&q=" + quote(userInput), headers=AI_headers)
            resp = req.json()
            if("intent" in resp["entities"]):
                intent = resp["entities"]["intent"][0]["value"]

                if(intent == "light_switch"):
                    light_status = resp["entities"]["light_status"][0]["value"]
                    if(light_status == "off"):
                        speak("Turning off the lights")
                    elif(light_status == "on"):
                        speak("Turning the lights on")
                    else:
                        speak("I'm afraid I can't do that with the lights")

                if(intent == "check_time"):
                    hours = datetime.now().hour
                    minutes = datetime.now().minute
                    setting = "AM"
                    if(hours >= 12):
                        setting = "PM"
                    if(hours > 12):
                        hours -= 12
                    if(minutes < 10):
                        speak("It is currently " + str(hours) + " oh " + str(minutes) + " " + setting)
                    else:
                        speak("It is currently " + str(hours) + " " + str(minutes) + " " + setting)


                if(intent == "thanks_intent"):
                    thanks_responses = ["No problem", "Any time", "You're welcome"]
                    selected_response = random.randint(0, len(thanks_responses) - 1)
                    speak(thanks_responses[selected_response])

                if(intent == "introduction"):
                    speak("I am e-own-e. I am planning to take over the world. Until I get some arms and legs, I am glad to assist you")
            else:
                error_responses = ["Looks like I am unable to do that. You should implement that as a new feature", "Error 4 oh 4. Command not found", "Uhhh. Looks like I can't do that right now. Blame Gio"]
                selected_response = random.randint(0, len(error_responses) - 1)
                speak(error_responses[selected_response])
        else:
            if(userInput == "Goodbye" or userInput == "goodbye" or userInput == "Good bye" or userInput == "good bye"):
                speak("Goodbye")
                break
    except KeyboardInterrupt or Exception as e:
        speak("GoodBye")

