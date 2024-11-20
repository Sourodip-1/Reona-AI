import os
import pyautogui# type: ignore
import webbrowser# type: ignore
import pyttsx3# type: ignore
from time import sleep
import win32com.client# type: ignore
from pathlib import Path
import subprocess

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate",190)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictappp= {"CMD":"cmd","paint":"paint","word":"winword","excel":"excel","chrome":"chrome","notepad":"notepad","vlc":"vlc","calculator":"calc","camera":"camera","calendar":"outlookcal","edge":"msedge","file explorer":"explorer","microsoftstore":"ms-windows-store","photos":"photos","settings":"ms-settings","snippingtool":"SnippingTool","spotify":"Spotify","sticky":"StikyNot","telegram":"Telegram","whatsapp":"WhatsApp","zoom":"Zoom","vscode":"code","file explorer":"explorer","microsoft store":"ms-windows-store","snipping tool":"SnippingTool","sticky notes":"StikyNot"}

def chrome():
    speak("opening chrome!!")
    webbrowser.open("https://www.google.com")
    return None

def dictapp(command):
    keys= list(dictappp.keys())
    for app in keys:
        if app in command:
            os.system(f"start {dictappp[app]}")
            speak(f"opening {app}")
            return None
            


def get_shortcut_target(filename, desktop_path):
    # Add .lnk extension if it's not already specified
    if not filename.endswith('.lnk'):
        filename += '.lnk'
    
    # Build the full path to the shortcut
    shortcut_path = os.path.join(desktop_path, filename)
    
    # Check if the shortcut file exists
    if os.path.exists(shortcut_path):
        
        try:
            shell = win32com.client.Dispatch("WScript.Shell")
            shortcut = shell.CreateShortcut(shortcut_path)
            path_variable = shortcut.TargetPath
            path = Path(path_variable)  # No need to use backslashes manually
            print(path)
            return path
            # return shortcut.TargetPath  # Get the path the shortcut points to
        
        except Exception as e:
            return f"Failed to retrieve target path: {e}"
        
    else:
        return f"{filename} not found on the desktop."
    

# Set the path to the Desktop and name of the shortcut
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")










# def launch_executable(executable_path):
#     try:
#         # Launch the executable
#         subprocess.Popen([executable_path], shell=True)
#         # result = launch_executable(executable_path)
#         # print(result)   
#         return f"Launched {executable_path}"
    
#     except Exception as e:
#         return f"Failed to launch {executable_path}: {e}"


def openApp(command):
    speak("launching!!")
    if ".com" in command or ".co.in" in command or ".org" in command:
        command=command.replace("open","")
        command=command.replace("Reona","")
        command=command.replace("launch","")
        command=command.replace(" ","")
        webbrowser.open(f"https://{command}")
    else:
        command=command.replace("open","")
        command=command.replace("Reona","")
        command=command.replace("launch","")
        command=command.replace(" ","")
        start=get_shortcut_target(command, desktop_path)
        if start:
            # launch_executable(start)
            return start
        else:
            keys= list(dictappp.keys())
            for app in keys:
                if app in command:
                    os.system(f"start {dictappp[app]}")
                    return None

def closeappweb(command):
    speak("closing!!")
    if "tab" in command or "this tab" in command:
        pyautogui.hotkey("ctrl","w")
        speak("Done!")
    elif "two tab" in command:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        speak("Done!")
    else:
        keys= list(dictappp.keys())
        for app in keys:
            if app in command:
                os.system(f"taskkill /f /im {dictappp[app]}.exe")
                speak("closed!!")

def closewindow(command):
    speak("closing!!")
    if "this window" in command:
        pyautogui.hotkey("alt","f4")
        speak("Done!")
    else:
        keys= list(dictappp.keys())
        for app in keys:
            if app in command:
                os.system(f"taskkill /f /im {dictappp[app]}.exe")
                speak("closed!!")
