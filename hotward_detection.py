import os
import speech_recognition as sr

def takeCommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        command.pause_threshold = 1
        audio = command.listen(source)
        
        try:
            print("Recognizing.....")
            query = command.recognize_google(audio, language='en-in')
            print(f"You said: {query}")
            
        except:
            return "None"
        
        return query.lower()
    
while True:
    
    wake_up = takeCommand()
    
    if 'wake up' in wake_up:
        os.startfile('C:\\Users\\Samay Ashar\\OneDrive\\Desktop\\JARVIS\\main.py')
        
    else:
        print("Nothing.....")     