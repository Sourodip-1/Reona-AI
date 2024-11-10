import os
import pyttsx3
import speech_recognition as sr
import datetime
import pywhatkit
import wikipedia
import webbrowser
import requests
from bs4 import BeautifulSoup
import random
import time
import sys  # Import sys for reliable exit
import pyautogui
import google.generativeai as genai
import re

def launch_executable(executable_path):
    try:
        os.startfile(executable_path)
    except Exception as e:
        speak(f"Sorry, I couldn't launch the executable. Error: {str(e)}")

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 175)  # Slightly slower rate for natural flow
engine.setProperty("volume", 0.9)  # Lower volume slightly for softness

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)
    greetings = [
        "Good Morning!.",
        "Good Afternoon!.",
        "Good Evening!."
    ]
    
    if 0 <= hour < 12:
        greet = greetings[0]
    elif 12 <= hour < 18:
        greet = greetings[1]
    else:
        greet = greetings[2]

    speak(greet)
    speak("I’m Reona, Ready to Assist You!!")

def searchGoogle(query):
    import wikipedia as googlescrap
    query = query.replace("reona", "").replace("google", "").replace("on", "").replace("google search", "")
    speak("Alright, searching Google for you.")
    time.sleep(1)  # Simulate a brief pause

    try:
        pywhatkit.search(query)
        results = googlescrap.summary(query, sentences=1)
        speak("Here's what I found:")
        speak(results)
    except Exception:
        speak("Sorry, I couldn't find anything on that.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, timeout=100, phrase_time_limit=100)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception:
        return "None"
    return query.lower()

def alarm(query):
    timehere = open("alarmfile.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarmfile.txt")

if __name__ == "__main__":
    sleeping = False  # Initialize in awake mode

    while True:
        if not sleeping:  # Only take commands if awake
            query = takeCommand()
            if query in ["None", ""]:
                continue
            
            if "wake up" in query:
                greetMe()
                sleeping = False  # Set to awake mode
            
            elif "go to sleep" in query:
                speak("Going to sleep now. Just call me anytime.")
                sleeping = True  # Set to sleep mode
            else:
                
                if "hello" in query:
                    speak("Hello! Hope you're having a wonderful day!")

                elif "tell me about yourself" in query:
                    speak("I am Reona,  An Advance AI Virtual Assistant Model created by Sourodip Roy of Class 12 A. I am here to assist you with your tasks and provide information. How can I help you today?")
                  
                elif "i am fine" in query:
                    speak("That's great to hear! Anything I can help you with?")
                elif "how are you" in query:
                    speak("I'm doing great, thank you for asking!")
                elif "thank you" in query:
                    speak("You're very welcome!")
                elif "pause" in query:
                    pyautogui.press("space")
                    speak("Paused!!")
                elif "play" in query:
                    pyautogui.press("space")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("Muted!!")
                elif "unmute" in query:
                    pyautogui.press("m")
                    speak("Unmuted!!")
                elif "volume down" in query:
                    from keyboard import volume_down
                    volume_down()
                    speak("decreasing volume!!")
                elif "volume up" in query:
                    from keyboard import volume_up
                    volume_up()
                    speak("increasing volume!!")

                elif "open" in query:
                    from apps import openApp
                    src=openApp(query)
                    if src:
                        launch_executable(src)
                elif "close this window" in query:
                    speak("Closing the current window.")
                    pyautogui.hotkey("alt", "f4")
                elif "close" in query:
                    from apps import closeappweb
                    closeappweb(query)
                elif "shutdown" in query:
                    os.system("shutdown /s /t 1")
                elif "hibernate" in query:
                    os.system("shutdown /h")
                # elif "unlock" in query:
                #     for i in range(3):
                #         pyautogui.press("enter")
                #     speak("Unlocked!!")
                elif "lock" in query:
                    os.system("rundll32.exe user32.dll,LockWorkStation")
                elif "google" in query:
                    searchGoogle(query)
                # elif "playlist " in query:
                #     from search import Music
                #     Music()
                #     speak("Playing your playlist!!")
                elif "youtube" in query:
                    if "homepage" in query:
                        webbrowser.open("https://www.youtube.com/")
                        speak("Opening YouTube homepage for you.")
                    else:
                        from search import searchYoutube
                        speak("Looking up YouTube for you.")
                        searchYoutube(query)
                elif "wikipedia" in query:
                    from search import searchWikipedia
                    speak("Searching Wikipedia...")
                    searchWikipedia(query)
                elif "temperature in asansol" in query or "weather in asansol" in query:
                    city = "ASANSOL"  # Default location; can modify based on user input
                    speak(f"Checking the temperature in {city}...")
                    url = f"https://www.google.com/search?q=Temperature+in+{city}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"The current temperature in {city} is {temp}")

                elif "set alarm" in query:
                    print("input time example: 12 and 30")
                    speak("set the time for alarm")
                    a= input("Enter the time for alarm: ")
                    alarm(a)
                    speak("Done!!")
                elif "current date" in query:
                    strDate = datetime.datetime.now().strftime("%d %B %Y")
                    speak(f"Today's date is {strDate}")
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%I:%M %p")
                    speak(f"It's currently {strTime}")
                elif "turn off" in query:
                    speak("Closing the program now.")
                    sys.exit()  # Use sys.exit() to ensure program termination
                elif "remember that" in query:
                    rememberMessege = query.replace("remember that", "").replace("reona", "").strip()
                    with open("remember.txt", "w") as remember:
                        remember.write(rememberMessege)
                    speak("Hmm!! Done!!")
                elif "continue remembering" in query:
                    additionalMessage = query.replace("continue remembering", "").replace("reona", "").strip()
                    with open("remember.txt", "a") as remember:
                        remember.write(" " + additionalMessage)
                    speak("Hmm!! Added to memory.")

                elif "what do you remember" in query:
                    with open("remember.txt", "r") as remember:
                        rememberedText = remember.read()
                    if rememberedText:
                        speak("You told me to remember: " + rememberedText)
                    else:
                        speak("You haven't asked me to remember anything yet.")
                else:
                    if query:
                        genai.configure(api_key="AIzaSyCX_VGcIE4NOCpX6d36dXTdid3R0pbCzVM")
                        model = genai.GenerativeModel("gemini-1.5-pro-002")
                        response = model.generate_content(query)

                        # Clean up the response text by removing '*' and '#' symbols
                        cleaned_text = re.sub(r'[\*#]', '', response.text)
                        
                        # Limit the response to a maximum of two lines
                        max_characters = 150  # Adjust as needed for line length
                        brief_response = cleaned_text[:max_characters].rsplit('.', 1)[0] + '.'
                        
                        print(brief_response)
                        speak(brief_response)
                    else:
                        speak("")
        else:
            # Only listen for wake-up command while sleeping
            query = takeCommand()
            if "wake up" in query:
                greetMe()
                sleeping = False  # Exit sleep mode and resume processing
