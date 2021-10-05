import pyttsx3
import speech_recognition as sr
import whatsapp

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voices', voices[0].id)
Assistant.setProperty('rate',170)

def Speak(text):
    print("  ")
    Assistant.say(text)
    print(f": {text}")
    print("  ")
    Assistant.runAndWait()
    
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
            print(" ")
        
        return query.lower()
    
def TaskGui():
    
    while True:
        query = takeCommand()
        
        if 'hello' in query:
            Speak("Hello sir, how are you?")
            
        elif 'whatsapp message' in query:
            query = query.replace("jarvis","")
            query = query.replace("send","")
            query = query.replace("whatsapp message","")
            query = query.replace("to","")
            name = query
            
            if 'dad' in name:
                numb = '9687612325'
                Speak(f"What's the message for {name}")
                mess = takeCommand()
                whatsapp.whatsapp(numb,mess)
                
            elif 'mama' in name:
                numb = '9821853311'
                Speak(f"What's the message for {name}")
                mess = takeCommand()
                whatsapp.whatsapp(numb,mess)
                
            elif 'masi' in name:
                numb = '8879477430'
                Speak(f"What's the message for {name}")
                mess = takeCommand()
                whatsapp.whatsapp(numb,mess)
                
            elif 'krisha' in name:
                numb = '7506996620'
                Speak(f"What's the message for {name}")
                mess = takeCommand()
                whatsapp.whatsapp(numb,mess)
                
            elif 'group' in name:
                gro = 'BJ9KqDf3umVJjo3y26V3MB'
                Speak(f"What's the message for {name}")
                mess = takeCommand()
                whatsapp.Whatsapp_Grp(gro,mess)

TaskGui()