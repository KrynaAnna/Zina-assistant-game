#Libraries
import pyttsx3
import speake3
import speech_recognition as sr
import random
import difflib

zina = pyttsx3.init()
voices = zina.getProperty('voices')
for voice in voices:
    if 'english' in voice.name.lower() :
        zina.setProperty('voice', voice.id)
        zina.setProperty('rate', 170)

zina.say("What is your name?")
zina.runAndWait()
zina.stop()
answer = ''

#Perception of the text
while len(answer) == 0:
    try:
        r = sr.Recognizer()
        r . energy_threshold  =  1000
        with sr.Microphone(device_index=0) as source:
            audio = r.listen(source)
        answer = r.recognize_google(audio, language = "pl-PL").split()
    except sr.UnknownValueError:
        zina.say("Please repeat your name")
        zina.runAndWait()
        zina.stop()


useless = ['my', 'name', 'is']
for i in range(len(answer)):
    if answer[i] in useless:
        answer[i] = ''

zina.say("Hello," + ''.join(answer))
zina.runAndWait()
zina.stop()
zina.say("My name is Zina. Let's play a fun guessing game. I guess a number from one to five, and you try to guess.")
zina.runAndWait()
zina.stop()

#Game
n = random.randint(1,5)
print(n)
zina.say("Ordered, guess!")
zina.runAndWait()
zina.stop()

dict = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
help = ['', 'run', '', 'siri', 'fall', '', '', '', '', '', '']

r = sr.Recognizer()
r . energy_threshold  =  1000
with sr.Microphone(device_index=0) as source:
    audio = r.listen(source)
    zina.stop()
    answer = r.recognize_google(audio, language = "en-US")
    print(answer)

while answer != n:
    try:
        if answer.isdigit() == False or len(answer) == 0:
            word = difflib.get_close_matches(answer.lower(), dict)
            word2 = difflib.get_close_matches(answer.lower(), help)
            word = ''.join(word)
            word2 = ''.join(word)
            if word in dict:
                answer = dict.index(word)
            elif word2 in help:
                answer = help.index(word2)
                if int(answer) != int(n) and int(answer) <= 5 and int(answer) >= 1:
                    zina.say("Try again")
                    zina.runAndWait()
                    zina.stop()
                elif int(answer) > 5 or int(answer) < 1:
                    zina.say("I said, from one to five. Try again.")
                    zina.runAndWait()
                    zina.stop()
                r = sr.Recognizer()
                r . energy_threshold  =  1000
                with sr.Microphone(device_index=0) as source:
                    audio = r.listen(source)
                    answer = r.recognize_google(audio, language = "en-US")
                    print(answer)
            else:
                zina.say("Please repeat. It must be a number")
                zina.runAndWait()
                zina.stop()
                r = sr.Recognizer()
                r . energy_threshold  =  1000
                with sr.Microphone(device_index=0) as source:
                    audio = r.listen(source)
                    answer = r.recognize_google(audio, language = "en-US")
                    print(answer)

        elif answer.isdigit() == True:
            if int(answer) != int(n) and int(answer) <= 5 and int(answer) >= 1:
                zina.say("Try again")
                zina.runAndWait()
                zina.stop()
            elif int(answer) == n:
                zina.say("Well done, I thought you wouldn't guess.")
                zina.runAndWait()
                zina.stop()
                zina.say("Good game, we'll play again later. Bye.")
                zina.runAndWait()
                zina.stop()
                break
            elif int(answer) > 5 or int(answer) < 1:
                zina.say("I said, from one to five. Try again.")
                zina.runAndWait()
                zina.stop()
            r = sr.Recognizer()
            r . energy_threshold  =  1000
            with sr.Microphone(device_index=0) as source:
                audio = r.listen(source)
                answer = r.recognize_google(audio, language = "en-US")
                print(answer)

    except sr.UnknownValueError:
        print('error')
        zina.say("I did not understand what you said, please repeat")
        zina.runAndWait()
        zina.stop()
        r = sr.Recognizer()
        r . energy_threshold  =  1000
        with sr.Microphone(device_index=0) as source:
            audio = r.listen(source)
            answer = r.recognize_google(audio, language = "en-US")
            print(answer)