import subprocess
import sys
import time
from bs4 import BeautifulSoup
import pyttsx3
import requests
import wikipedia
import webbrowser
import os
import speech_recognition as sr
import psutil
import pyautogui as pg
from playsound import playsound
from googletrans import Translator
import datetime
import pywhatkit as pw

engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[10].id)
rate = engine.getProperty('rate')
engine.setProperty('rate',190)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')

        print(f"You said: {query}\n")

    except Exception as e:
        print(e)


        print("Say that again please...")

        return "None"
    return query
    

def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning!")
        speak("Good Morning!")
        
    
    elif hour >= 12 and hour < 18:
        print("Good Afternoon")
        speak("Good Afternoon")
    
    else:
        print("Good Evening")
        speak("Good Evening")


if __name__ == "__main__":

    wishme()
    print("I'm Lisa... How can I help you today? ")
    speak("I'm Lisa... How can I help you today? ")
    playsound('/Users/hari/Desktop/Code/Python/Automation with Lisa/final_notification_alert.mp3')
    query = takeCommand().lower()
    translator = Translator()
    while True:

        if 'hello' in query:
            speak("Hello! ")
            break

        
        elif 'name' in query:
            speak("I am Lisa...Pleased to meet you")
            speak("How can I be of your Assistance?")
            playsound('/Users/hari/Desktop/Code/Python/Automation with Lisa/final_notification_alert.mp3')
            query = takeCommand().lower()

        elif 'wikipedia' in query:
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2) 
            print(results)
            speak(results)
            break

        elif 'translate' in query:
            query = query.replace("translate","")
            speak("What Language do you want me to translate? ")
            playsound('/Users/hari/Desktop/Code/Python/Automation with Lisa/final_notification_alert.mp3')
            lang = takeCommand().lower()
            destLang = "hi"
            if 'telugu' in lang:
                destLang = 'te'
            elif 'hindi' in lang:
                destLang = 'hi'
            elif 'tamil' in lang:
                destLang = 'ta'
            elif 'malayalam' in lang:
                destLang = 'ml'
            elif 'kannada' in lang:
                destLang = 'kn'
            elif 'spanish' in lang:
                destLang = 'es'
            elif 'french' in lang:
                destLang = 'fr'
            else:
                speak("Please Say it again")
                
            
            out = translator.translate(query,dest=destLang)
            print(out.text)
            engine.setProperty("rate",130)
            speak(out.pronunciation)
            break


        elif 'temperature' in query:
            print("In which city do you want to know the temperature ?")
            speak("Which city's temperature do you want to know ? ")
            playsound("/Users/hari/Desktop/Code/Python/Automation with Lisa/final_notification_alert.mp3")
            cityname = takeCommand().lower()
            search = f"temperature in {cityname}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data =  BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"Current {search} is {temp} in Celsius")
            break


            
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
            break

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            break

        
        
        elif 'brave' in query:
            codepath = "/Applications/Brave Browser.app"
            open_file(codepath)
            break

        elif 'battery' in query:
            battery = psutil.sensors_battery()
            print("Battery Percentage: ", battery.percent)
            speak(f"Your battery status is about {battery.percent} percent")
            break

        
        elif 'play' in query:
            query = query.replace("play","")
            print("Playing " + query)
            
            webbrowser.open("https://www.youtube.com")
            time.sleep(6)
            pg.click(537,138)
            pg.write(query)
            pg.press('enter')
            time.sleep(3)
            pg.click(455,366)
            time.sleep(3)
            pg.press('f')
            break
                

            

                

        elif 'bye' in query:
            speak("It's been a pleasure ")
            break

        elif 'screenshot' in query:
            speak("Taking a Screenshot ")
            speak("set the time duration to take screenshot")
            t = int(input("What is the countdown time : "))
            for x in reversed(range(0,t)):
                seconds = x % 60
                mins = int(x / 60) % 60
                hrs = int(x / 3600) 
                print(f"{hrs:02}:{mins:02}:{seconds:02}")
                time.sleep(1)
            playsound('/Users/hari/Desktop/Code/Python/Automation with Lisa/Screenshot_alert.wav')
            pg.screenshot('./screenshot.png')
            break

        
        elif query is not []:
            speak(f"Fetching Results for {query} from Google")
            time.sleep(1)
            pw.search(query)
            break

        else:
            speak("Sorry I didn't get that... Can you please repeat")
            playsound('/Users/hari/Desktop/Code/Python/Automation with Lisa/final_notification_alert.mp3')
            query = takeCommand().lower()


     