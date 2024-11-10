import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate",190)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Hearing......")
        r.pause_threshold=1
        r.energy_threshold=300
        audio=r.listen(source,0,4)

    try:
        print("Recognizing......")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print("Repeat that again please......")
        return "None"
    return query


def searchYoutube(query):
    if "youtube" in query:
        query=query.replace("reona","")
        query=query.replace("youtube","")
        query=query.replace("search","")
        query=query.replace("on","")
        speak("Searching in youtube!")
        web= "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done!")

def searchWikipedia(query):
    if "wikipedia" in query:
        query=query.replace("reona","")
        query=query.replace("wikipedia","")
        query=query.replace("search","")
        query=query.replace("on","")
        speak("Searching in wikipedia!")
        results=wikipedia.summary(query,sentences=2)
        print(results)
        speak(results)

def Music(query):
    if "playlist" in query:
        web= "https://music.youtube.com/watch?v=tEhf_HpkNQ4&list=PLALk_KIB33pWvgqTqbCiEsQrqBjkgqEif"
        webbrowser.open(web)
        pywhatkit.playonyt("playlist")
        speak("Done!")
