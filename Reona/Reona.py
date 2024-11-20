import tkinter as tk #ignore 
import pyttsx3#ignore 
import os#ignore 
import time#ignore 
import threading#ignore 
import speech_recognition as sr#ignore 
import pyautogui#ignore 
import datetime#ignore 
import pywhatkit#ignore 
import wikipedia#ignore 
import requests#ignore 
from bs4 import BeautifulSoup#ignore 
import sys#ignore 
import google.generativeai as genai#ignore 
import re#ignore 
import webbrowser#ignore 
import subprocess#ignore 

# Initialize the Tkinter root window
root = tk.Tk()
root.geometry("200x80+1166+676")  # Position in bottom-right for 1366x756 screen
root.overrideredirect(True)  # Removes title bar
root.attributes("-topmost", True)  # Keep window always on top
root.wm_attributes("-transparentcolor", "black")  # Make background color transparent

# Initialize the pyttsx3 engine for speech
engine = pyttsx3.init("sapi5")
engine.setProperty("rate", 175)  # Set a comfortable speaking rate
engine.setProperty("voice", engine.getProperty("voices")[1].id)

# Frame to hold content
frame = tk.Frame(root, bg="black")
frame.pack(fill=tk.BOTH, expand=True)

# Label to show assistant's status
status_label = tk.Label(frame, text="Status: Ready", fg="white", bg="black", font=("Helvetica", 12))
status_label.pack(pady=5)

# Function to update the status message in the UI
def update_status(status_text):
    status_label.config(text=f"Status: {status_text}")
    root.update_idletasks()

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to handle the assistant's commands
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        update_status("Listening...")
        recognizer.pause_threshold = 1
        recognizer.energy_threshold = 300
        
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)  # Increase timeout to 10 seconds
            update_status("Recognizing...")
            command = recognizer.recognize_google(audio, language="en-in")
            update_status("Ready")
            return command.lower()
        except sr.WaitTimeoutError:
            update_status("Listening timed out. Try again.")
            speak("")
            return None
        except sr.UnknownValueError:
            update_status("Couldn't understand. Try again.")
            return None
        except sr.RequestError:
            update_status("Network error.")
            return None

# Flag to manage sleep/wake status
is_asleep = False

dictappp= {"CMD":"cmd","paint":"paint","word":"winword","excel":"excel","chrome":"chrome","notepad":"notepad","vlc":"vlc","calculator":"calc","camera":"camera","calendar":"outlookcal","edge":"msedge","file explorer":"explorer","microsoftstore":"ms-windows-store","photos":"photos","settings":"ms-settings","snippingtool":"SnippingTool","spotify":"Spotify","sticky":"StikyNot","telegram":"Telegram","whatsapp":"WhatsApp","zoom":"Zoom","vscode":"code","file explorer":"explorer","microsoft store":"ms-windows-store","snipping tool":"SnippingTool","sticky notes":"StikyNot"}

# Main assistant function to process commands
def assistant():
    global is_asleep  # To track sleep/wake status

    while True:
        command = take_command()
        if command:
            if is_asleep:
                if "wake up" in command:
                    speak("I'm awake now.")
                    update_status("Ready")
                    is_asleep = False
                else:
                    speak("")
                    continue
            elif "wake up" in command:
                speak("I'm already awake.")
            elif "go to sleep" in command:
                speak("Going to sleep.")
                update_status("Asleep")
                is_asleep = True
            elif "hello" in command:
                speak("Hello! How can I assist you?")
            elif "tell me about yourself" in command:
                speak("I am Reona, an advanced AI virtual assistant created by Sourodip Roy of Class 12 A.")
            elif "how are you" in command:
                speak("I'm doing great, thank you for asking!")
            elif "thank you" in command:
                speak("You're very welcome!")
            elif "pause" in command:
                pyautogui.press("space")
                speak("Paused!")
            elif "play" in command:
                pyautogui.press("space")
                speak("Playing!")
            elif "mute" in command:
                pyautogui.press("m")
                speak("Muted!")
            elif "unmute" in command:
                pyautogui.press("m")
                speak("Unmuted!")
            elif "volume down" in command:
                pyautogui.hotkey("volumedown")
                pyautogui.hotkey("volumedown")
                pyautogui.hotkey("volumedown")
                pyautogui.hotkey("volumedown")
                pyautogui.hotkey("volumedown")
                speak("Decreasing volume!")
            elif "volume up" in command:
                pyautogui.hotkey("volumeup")
                pyautogui.hotkey("volumeup")
                pyautogui.hotkey("volumeup")
                pyautogui.hotkey("volumeup")
                pyautogui.hotkey("volumeup")
                speak("Increasing volume!")
            # elif "on youtube" in command:
            #     from search import searchYoutube
            #     searchYoutube(command)
            elif "open youtube" in command:
                webbrowser.open("https://www.youtube.com")
                speak("Opening YouTube.")
            
            elif "open website" in command:
                query = command.replace("open website", "").strip()
                webbrowser.open(f"https://{query}")
                speak(f"Opening website {query}.")
            elif "open chrome" in command or "open browser" in command or "open Google" in command or "open Google Chrome" in command:
                from apps import chrome
                chrome()
            # elif "open + {dictapp}" in command:
            elif "open desktop " in command:
                app = command.replace("open", "").strip()
                speak(f"Opening {app}.")
                try:
                    subprocess.run([app])
                except Exception as e:
                    speak(f"Sorry, I couldn't open {app}. Error: {str(e)}")

            elif "open" in command:
                from apps import dictapp
                dictapp(command)

            elif "close this tab" in command:
                speak("Closing the current tab.")
                pyautogui.hotkey("ctrl", "w")

            elif "close this window" in command:
                speak("Closing the current window.")
                pyautogui.hotkey("alt", "f4")

            elif "shutdown" in command:
                speak("Shutting down the system.")
                os.system("shutdown /s /t 1")
            elif "hibernate" in command:
                speak("Hibernating the system.")
                os.system("shutdown /h")
            elif "lock" in command:
                speak("Locking the system.")
                os.system("rundll32.exe user32.dll,LockWorkStation")
            elif "full screen" in command or "maximize" in command:
                speak("Maximizing the window.")
                pyautogui.hotkey("f")
            elif "minimize" in command:
                speak("Minimizing the window.")
                pyautogui.hotkey("f")
            elif "google" in command:
                query = command.replace("google", "").strip()
                pywhatkit.search(query)
                results = wikipedia.summary(query, sentences=1)
                speak("Here's what I found on Google.")
                speak(results)
            elif "youtube" in command:
                webbrowser.open("https://www.youtube.com")
                speak("Opening YouTube.")
            elif "news" in command:
                speak("Fetching the latest news for you.")
                url = "https://news.google.com"
                webbrowser.open(url)
                speak("Opening Google News.")
            elif "temperature" in command or "weather" in command:
                city = "Asansol"  # Default location
                speak(f"Checking the temperature in {city}...")
                url = f"https://www.google.com/search?q=Temperature+in+{city}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(f"The current temperature in {city} is {temp}")
            elif "set alarm" in command:
                speak("Set the time for the alarm in format HH:MM.")
                alarm_time = input("Enter time (HH:MM): ")
                with open("alarmfile.txt", "w") as file:
                    file.write(alarm_time)
                speak("Alarm is set.")
            elif "current date" in command:
                date = datetime.datetime.now().strftime("%d %B %Y")
                speak(f"Today's date is {date}")
            elif "the time" in command:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                speak(f"It's currently {current_time}")
            elif "turn off" in command or "exit" in command:
                speak("Closing the assistant. Goodbye!")
                root.destroy()
                sys.exit()
            elif "remember that" in command:
                note = command.replace("remember that", "").strip()
                with open("remember.txt", "w") as file:
                    file.write(note)
                speak("Noted.")
            elif "what do you remember" in command:
                try:
                    with open("remember.txt", "r") as file:
                        note = file.read()
                    if note:
                        speak("You asked me to remember: " + note)
                    else:
                        speak("I don't have anything to remember.")
                except FileNotFoundError:
                    speak("I don't have anything to remember.")
            
            elif "do not disturb" in command:
                speak("Activating Do Not Disturb mode.")
                # Add code to activate DND (example: mute notifications)
            elif "restart" in command:
                speak("Restarting the system.")
                os.system("shutdown /r /t 1")
            elif "search for" in command:
                query = command.replace("search for", "").strip()
                pywhatkit.search(query)
                speak(f"Searching for {query}.")
            # elif "wirte a " in command:
            #     a=open("Writing.txt", "w+")
            #     genai.configure(api_key="AIzaSyCX_VGcIE4NOCpX6d36dXTdid3R0pbCzVM")
            #     model = genai.GenerativeModel("gemini-1.5-pro-002")
            #     response = model.generate_content(command)
            #     # Clean up the response text by removing '*' and '#' symbols
            #     cleaned_text = re.sub(r'[\*#]', '', response.text)
            #     a.write(cleaned_text)
            #     speak("Done!!")

            else:
                # Use Gemini API to generate a response when no predefined command matches
                if command:
                    genai.configure(api_key="AIzaSyCX_VGcIE4NOCpX6d36dXTdid3R0pbCzVM")
                    model = genai.GenerativeModel("gemini-1.5-pro-002")
                    response = model.generate_content(command)

                    # Clean up the response text by removing '*' and '#' symbols
                    cleaned_text = re.sub(r'[\*#]', '', response.text)

                    # Limit the response to a maximum of two lines
                    max_characters = 150  # Adjust as needed for line length
                    brief_response = cleaned_text[:max_characters].rsplit('.', 1)[0] + '.'

                    print(brief_response)
                    speak(brief_response)
                else:
                    speak("I'm not sure how to help with that. Can you please rephrase?")

# Function to start the assistant in a separate thread
def run_assistant():
    threading.Thread(target=assistant, daemon=True).start()

# Add a close button to the frame
def close_app():
    root.destroy()

close_button = tk.Button(frame, text="X", command=close_app, bg="red", fg="white", font=("Helvetica", 10))
close_button.place(relx=0.9, rely=0.1)  # Position at top-right inside the frame

# Start the assistant
run_assistant()

# Start the Tkinter event loop
root.mainloop()
