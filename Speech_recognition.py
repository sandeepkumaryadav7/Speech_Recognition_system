import speech_recognition as sr
import datetime
import os
import pyttsx3
import webbrowser
import time

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Could not understand audio")
def speechtx(x):
    engine=pyttsx3.init()
    voices=engine.getProperty("voices")
    engine.setProperty('voice',voices[1].id)
    rate=engine.getProperty("rate")
    engine.setProperty("rate",150)
    engine.say(x)
    engine.runAndWait()
if __name__=='__main__':

        if "computer" in  sptext().lower():
            while True:
                    data1=sptext().lower()
                    if "your name" in data1:
                        name="my name is computer"
                        speechtx(name)
                    elif "old are you" in data1:
                        age="i am two years old"
                        speechtx(age)
                    elif "time" in data1:
                        time=datetime.datetime.now().strftime("%I%M%p")
                        speechtx(time)
                    elif "web" in data1:
                        webbrowser.open("https://www.cricbuzz.com/")
                    elif "play song" in data1:
                        add="D:\movies"
                        listsong=os.listdir(add)
                        print(listsong)
                        os.startfile(os.path.join(add,listsong[1]))
                    elif "exit " in data1:
                        speechtx("thank you")
                        break
                    time.sleep(10)
        else:
         print("thanks...")








