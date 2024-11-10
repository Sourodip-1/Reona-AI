import pyttsx3
import datetime
import os

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate",190)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

extractedtime = open("alarmfile.txt","rt")
time = extractedtime.read()
Time= str(time)
extractedtime.close()

deletetime = open("alarmfile.txt","r+")
deletetime.truncate(0)
deletetime.close()

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("reona","")
    timenow = timenow.replace("set alarm","")
    timenow = timenow.replace("set an alarm","")
    timenow = timenow.replace(" and ",":")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
            speak("Time to wake up!")
            os.startfile("Sketch-1.mp3")
        elif currenttime + "00:00:30" == Alarmtime:
            exit()
ring(time)

