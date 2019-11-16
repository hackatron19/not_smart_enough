import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say what you want to search in the video");
    audio = r.listen(source, timeout=1, phrase_time_limit = 5)
    #print(audio)
    #print(type(audio))
try:
    print("You said: " + r.recognize_google(audio))
except:
    pass
#