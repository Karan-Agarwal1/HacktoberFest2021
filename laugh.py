import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

rate = engine.getProperty("rate")
engine.setProperty("rate",200)

engine.setProperty("volume",1.0)

volume = engine.getProperty("volume")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


speak("haa,haa,haa,haa!")
