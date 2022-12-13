import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("SAY SOMETHING IN TAMIL AND BE SILENT ")
    audio = r.listen(source)
    print("GOT YOU")
try:
    WhatUSpoke = r.recognize_google(audio,language="ta-IN")
    print("WHAT YOU SPOKE : ",WhatUSpoke)
except:
    pass
          
