import pyttsx3
from datetime import datetime

BOSS = "Nency & Yesha"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    # hour = datetime.now().hour
    hour = 2
    if 5 <= hour < 12:
        speak("Good Morning" + BOSS)
    elif 12 <= hour < 16:
        speak("Good Afternoon" + BOSS)
    elif 16 <= hour < 20:
        speak("Good Evening" + BOSS)
    elif 20 <= hour < 24:
        speak("Good Night" + BOSS)
    else:
        speak(BOSS + "You should be sleeping at this moment")

# initializing pyttsx3
engine = pyttsx3.init()

# changing the speed of speaking
engine.setProperty('rate', 175)

# changing voice to a female voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

greet()