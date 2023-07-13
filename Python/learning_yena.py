"""
1. Listen what we speak - Reproducing speech into text (Speech Recognition)
2. Understand the meaning
3. Action:
    greet
    opening a website
    finding something from wiki
    opening an app on the computer
    play songs
    open pictures from the computer
4. Speak - Text To Speech (TTS)
"""

"""
import pyttsx3

engine = pyttsx3.init()

# rate = engine.getProperty('rate')   # getting details of current speaking rate
# print (rate)                        #printing current voice rate
engine.setProperty('rate', 175)     # setting up new voice rate

voices = engine.getProperty('voices')
print(voices)
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female


engine.say("Hello Nency & Yesha")
engine.runAndWait()
"""

import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
