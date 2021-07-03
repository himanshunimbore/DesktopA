import datetime
import webbrowser
import pyttsx3
import wikipedia
import subprocess
import ctypes
import os
import winshell
import speech_recognition as sr
import pyjokes
import time
import random
import pywhatkit


def say(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        say("Good Morning Sir !")

    elif 12 <= hour < 18:
        say("Good Afternoon Sir !")

    else:
        say("Good Evening Sir !")

    say("I am your Assistant Hexa")


def yourname():
    say("What can i call you sir")
    username = takeCommand()
    say("Welcome Mister")
    say(username)
    print(f"Welcome Mr.{username}")

    say("How can i Help you, Sir")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Say...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize You.")
        return "None"

    return query

if __name__ == '__main__':

    wish()
    yourname()

    while True:
        
        query = takeCommand().lower()

        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command
        if 'wikipedia' in query:
            say('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            say("According to Wikipedia")
            print(results)
            say(results)

        elif 'open youtube' in query:
            say("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            say("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            say("Here you go to Stack Over flow Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query or "play song" in query:
            say("Here you go with music")
            music_dir = 'E:\Docs\Music'
            songs = os.listdir(music_dir)
            no = random.randint(0, 100)
            os.startfile(os.path.join(music_dir, songs[no]))

        elif 'play' in query:
            song = query.replace('play', '')
            say('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'search' in query:
            say("searching")
            webbrowser.open_new(query)

        elif 'the time' in query:
            # print("Showing Time")
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir, the time is {strTime}")

        elif 'how are you' in query:
            say("I am fine, Thank you")
            say("How are you, Sir")

        elif 'fine' in  query :
            say("It's good to know that your fine")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query

        elif 'exit' in query:
            say("Thanks for giving me your time")
            exit()

        elif "who made you" in query or "who created you" in query:
            say("I have been created by Himanshu.")

        elif 'joke' in query:
            say(pyjokes.get_joke())

        elif "who i am" in query:
            say("you are a human being.")

        elif "why you came to world" in query:
            say("I am your vitual assissant,I am here for you")

        elif 'is love' in query:
            say("It is Hard to understand ")

        elif "who are you" in query:
            say("I am your assistant created by Himanshu")

        elif 'reason for you' in query:
            say("I was created as a project by Mister Himanshu ")

        elif 'lock window' in query:
            say("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            say("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            say("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            say("for how much seconds you want to stop hexa from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            say("You asked to Locate")
            say(location)
            webbrowser.open("https://www.google.com/maps/place/" + location + "")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            say("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            say("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            say("What should i write, sir")
            note = takeCommand()
            file = open('hexa.txt', 'w')
            say("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            say("Showing Notes")
            file = open("hexa.txt", "r")
            print(file.read())
            say(file.read(6))

        elif "hexa" in query:

            wish()
            say("Hexa in your service Sir")


        elif 'good morning' in query:
            say("A warm" + query)
            say("How are you Sir")

        elif "will you be my girlfriend" in query or "will you be my boyfriend" in query:
            say("I'm not sure about, may be you should give me some time")

        elif "how are you" in query:
            say("I'm fine")

        elif "i am happy today" in query:
            say("Glad to hear that you are happy")

        elif 'open code' in query:
            codePath = "C:\\Program Files\\IntelliJ IDEA Community Edition 2020.3.1\\bin\\idea64.exe"
            say("Opening Intellijidea")
            if os.startfile(codePath):
                say("Opening")
