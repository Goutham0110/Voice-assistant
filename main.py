import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import os
import pywhatkit


def listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening')
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 0.6
        audio = r.listen(source)

        try:
            print("Recognizing")
            cmd = r.recognize_google(audio, language='en-in')
            print("the command is printed= ", cmd)

        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"

        return cmd


def say(audio):

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()


def wake():
    say("Hi. I am Gwen. Tell me how may I help you")


def tell_day():

    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
                4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        say("It is " + day_of_the_week)


def tell_time():

    time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    min = time[14:16]
    say("It is" + hour + "Hours and" + min + "Minutes")


def tell_date():
    pass


def run():

    wake()

    while(True):
        command = listen().lower()

# date and time
        if "which day it is" in command:
            tell_day()
            continue

        elif "tell me the time" in command:
            tell_time()
            continue

# browser
        elif "open" in command:
            url = command.replace("open ", "", 1)
            say("Opening"+url)
            url = url.replace(" ", "")
            webbrowser.open("www."+url+".com")
            continue

        elif "search" in command:
            key_word = command.replace("search ", "", 1)
            say("Searching web for "+key_word)
            webbrowser.open(key_word)
            continue

# wikipedia

        elif "from wikipedia" in command:
            say("Checking the wikipedia ")
            command = command.replace("wikipedia", "")
            result = wikipedia.summary(command, sentences=4)
            say("According to wikipedia")
            say(result)
            continue

# youtube

        elif "play" in command:
            key_word = command.replace("play ", "", 1)
            if "from youtube" in key_word:
                key_word = key_word.replace("from youtube", " ", 1)
            say("Playing"+key_word+"from youtube")
            pywhatkit.playonyt(key_word)
            continue

# others
        elif "tell me your name" in command:
            say("I am Gwen.")
            continue

        elif "bye" in command:
            say("Bye. See you soon")
            exit()


if __name__ == '__main__':
    run()
