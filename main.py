from typing import Text
from gtts.tts import Speed
import pyttsx3
import speech_recognition as sr
from bs4 import BeautifulSoup
import webbrowser
from pywikihow import search_wikihow
import pywhatkit
import wikipedia
from googletrans import Translator
import os
import pyautogui
import requests
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Tk
from tkinter import StringVar
from gtts import gTTS
from pytube import YouTube
import PyPDF2 
import datetime
from playsound import playsound
import keyboard
import pyjokes
from PyDictionary import PyDictionary as Diction
import smtplib

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voices', voices[0].id)
Assistant.setProperty('rate',170)

def Speak(audio):
    print("  ")
    Assistant.say(audio)
    print(f": {audio}")
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
            return "None"
        
        return query.lower()

def TaskExe():
    
    def wishMe():
        
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            Speak("Good Morning!")
            
        elif hour>=12 and hour<18:
            Speak("Good Afternoon!")
            
        else:
            Speak("Good Evening!")
            
        Speak("I am Jarvis Sir. Please tell me how may I help you.")
    
    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('samayashar@gmail.com', 'samaydeepakashar')
        server.sendmail('samayashar@gmail.com', to, content)
        server.close()
    
    def Music():
        Speak("Tell me the name of the song, sir!")
        musicName = takeCommand()
    
        
        if 'baaton ko teri' in musicName:
            os.startfile('C:\\Users\\Samay Ashar\\OneDrive\\Desktop\\Songs\\Baaton Ko Teri.mp3')

        elif 'main phir bhi tumko chahunga' in musicName:
            os.startfile('C:\\Users\\Samay Ashar\\OneDrive\\Desktop\\Songs\\Main Phir Bhi Tumko Chahunga.mp3')
            
        elif 'muskurane' in musicName:
            os.startfile('C:\\Users\\Samay Ashar\\OneDrive\\Desktop\\Songs\\Muskurane - Arijit Singh.mp3')
        
        else:
            pywhatkit.playonyt(musicName)     
            
        Speak("Your song has been started! Enjoy sir!")     
            
    def Whatsapp():
        Speak("Tell me the name of the person!")
        name = takeCommand()
        
        if 'dad' in name:
            Speak("Tell me the message sir!")
            msg = takeCommand()
            Speak("Ok sir! Tell me the time sir!")
            Speak("Time in hour!")
            hour = int(takeCommand())
            Speak("Time in minutes!")
            min = int(takeCommand())
            pywhatkit.sendwhatmsg("+919687612325",msg,hour,min,20)
            Speak("Ok sir, Sending the message!")
        
        elif 'mama' in name:
            Speak("Tell me the message sir!")
            msg = takeCommand()
            Speak("Ok sir! Tell me the time sir!")
            Speak("Time in hour!")
            hour = int(takeCommand())
            Speak("Time in minutes!")
            min = int(takeCommand())
            pywhatkit.sendwhatmsg("+919821853311",msg,hour,min,20)
            Speak("Ok sir, Sending the message!")
        
        elif 'masi' in name:
            Speak("Tell me the message sir!")
            msg = takeCommand()
            Speak("Ok sir! Tell me the time sir!")
            Speak("Time in hour!")
            hour = int(takeCommand())
            Speak("Time in minutes!")
            min = int(takeCommand())
            pywhatkit.sendwhatmsg("+918169807313",msg,hour,min,20)
            Speak("Ok sir, Sending the message!")\
                
        elif 'krisha' in name:
            Speak("Tell me the message sir!")
            msg = takeCommand()
            Speak("Ok sir! Tell me the time sir!")
            Speak("Time in hour!")
            hour = int(takeCommand())
            Speak("Time in minutes!")
            min = int(takeCommand())
            pywhatkit.sendwhatmsg("+917506996620",msg,hour,min,20)
            Speak("Ok sir, Sending the message!")
            
        else:
            Speak("Tell me the phone number sir!")
            phone = int(takeCommand())
            ph = '+91' - phone
            Speak("Tell me the message sir!")
            msg = takeCommand()
            Speak("Ok sir! Tell me the time sir!")
            Speak("Time in hour!")
            hour = int(takeCommand())
            Speak("Time in minutes!")
            min = int(takeCommand())
            pywhatkit.sendwhatmsg("+917506996620",ph,msg,hour,min,20)
            Speak("Ok sir, Sending the message!")

    def OpenApps():
        
        Speak("Ok sir, wait a second!")
        
        if 'code' in query:
            os.startfile("C:\\Users\\Samay Ashar\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code")

        elif 'telegram' in query:
            os.startfile("C:\\Users\\Samay Ashar\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Telegram Desktop")
            
        elif 'whatsapp' in query:
            os.startfile("C:\\Users\\Samay Ashar\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\WhatsApp")

        elif 'chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    
        elif 'facebook' in query:
            webbrowser.open('https://www.facebook.com/')
            
        elif 'instagram' in query:
            webbrowser.open('https://www.instagram.com/')
            
        elif 'linkedin' in query:
            webbrowser.open('www.linkedin.com/in/samayashar')
            
        elif 'github' in query:
            webbrowser.open('https://github.com/')
            
        elif 'maps' in query:
            webbrowser.open('https://www.google.com/maps/@22.3019008,73.2004352,12z')
        
        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com/')
        
        Speak("Your command has been successfully completed sir!")    

    def Temp():
        search = "temperature in vadodara"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_ = "BNeawe").text
        Speak(f"The temperature outside is {temperature}") 
    
    def Reader():
        Speak("Tell me the name of the book!")
        
        name = takeCommand()
        
        if 'astronomy' in name:
            
            os.startfile('C:\\Users\\Samay Ashar\\OneDrive\\Desktop\\Astronomy.pdf')
            book = open('C:\\Users\\Samay Ashar\\OneDrive\\Desktop\\Astronomy.pdf','rb')
            pdfReader = PyPDF2.PdfFileReader(book)
            pages = pdfReader.getNumPages()
            Speak(f"Number of pages in this book are {pages}")
            Speak("From which page should I start reading sir?")
            numPage = int(input("Enter the page number: "))
            page = pdfReader.getPage(numPage)
            text = page.extractText()
            Speak("In which language, I have to read?")
            lang = takeCommand()
            
            if 'hindi' in lang:
                trans1 = Translator()
                textHin = trans1.translate(text,'hi')
                textm = textHin.text
                speech = gTTS(text=textm)
                try:
                    speech.save("book.mp3")
                    playsound("book.mp3")
                
                except:
                    playsound("book.mp3")
                    
            else:
                Speak(text)
        
        elif 'time' in name:
            
            os.startfile('Downloads//Stephen Hawking - A Brief History Of Time.pdf')
            book = open('Downloads//Stephen Hawking - A Brief History Of Time.pdf','rb')
            pdfReader = PyPDF2.PdfFileReader(book)
            pages = pdfReader.getNumPages()
            Speak(f"Number of pages in this book are {pages}")
            Speak("From which page should I start reading sir?")
            numPage = int(input("Enter the page number: "))
            page = pdfReader.getPage(numPage)
            text = page.extractText()
            Speak("In which language, I have to read?")
            lang = takeCommand()
            
            if 'hindi' in lang:
                trans1 = Translator()
                textHin = trans1.translate(text,'hi')
                textm = textHin.text
                speech = gTTS(text=textm)
                try:
                    speech.save("book.mp3")
                    playsound("book.mp3")
                
                except:
                    playsound("book.mp3")
                    
            else:
                Speak(text)
    
    def SpeedTest():
        import speedtest
        Speak("Checking speed.....")
        speed = speedtest.Speedtest()
        downloading_speed = speed.download()
        correctDown_speed = int(downloading_speed/800000)
        uploading_speed = speed.upload()
        correctUplo_speed = int(uploading_speed/800000)
        
        if 'downloading speed' in query:
            Speak(f"The downloading speed is {correctDown_speed} mbps")
            
        elif 'uploading speed' in query:
            Speak(f"The uploading speed is {correctUplo_speed} mbps")

        else:
            Speak(f"The downloading speed is {correctDown_speed} mbps and the uploading speed is {correctUplo_speed} mbps")
            
    def Dict():
        Speak("Activated dictionary!")
        Speak("Tell me the problem sir!")
        probl = takeCommand()

        if 'meaning' in probl:
            probl = probl.replace("what is the","")
            probl = probl.replace("jarvis","")
            probl = probl.replace("of",'')
            probl = probl.replace("meaning of","")
            result = Diction.meaning(probl)
            Speak(f"The meaning of {probl} is {result}")
            
        elif 'synonym' in probl:
            probl = probl.replace("what is the","")
            probl = probl.replace("jarvis","")
            probl = probl.replace("of",'')
            probl = probl.replace("synonym of","")
            result = Diction.synonym(probl)
            Speak(f"The synonym of {probl} is {result}")
         
        elif 'antonym' in probl:
            probl = probl.replace("what is the","")
            probl = probl.replace("jarvis","")
            probl = probl.replace("of",'')
            probl = probl.replace("antonym of","")
            result = Diction.antonym(probl)
            Speak(f"The antonym of {probl} is {result}")
            
        Speak("Exited dictionary!")  
                      
    def CloseApps():
        Speak("Ok sir, wait a second!")
        
        if 'youtube' in query:
            os.system("TASKKILL /F /im chrome.exe")
        
        elif 'chrome' in query:
            os.system("TASKKILL /F /im chrome.exe")
        
        elif 'telegram' in query:
            os.system("TASKKILL /F /im Telegram.exe")
            
        elif 'code' in query:
            os.system("TASKKILL /F /im code.exe") 
            
        elif 'instagram' in query:
            os.system("TASKKILL /F /im chrome.exe")    
        
        elif 'facebook' in query:
            os.system("TASKKILL /F /im chrome.exe")
            
        elif 'linkedin' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'github' in query:
            os.system("TASKKILL /F /im chrome.exe")
            
        elif 'maps' in query:
            os.system("TASKKILL /F /im chrome.exe")
            
        elif 'whatsapp' in query:
            os.system("TASKKILL /F /im WhatsApp.exe")
            
        Speak("Your command has been successfully executed, sir!")

    def YoutubeAuto():
        Speak("What should I do sir?")
        comm = takeCommand()
        
        if 'pause' in comm:
            keyboard.press('space bar')
            
        elif 'restart' in comm:
            keyboard.press('0')                       
            
        elif 'mute' in comm:
            keyboard.press('m')
            
        elif 'skip' in comm:
            keyboard.press('l')
            
        elif 'back' in comm:
            keyboard.press('j')
            
        elif 'full screen' in comm:
            keyboard.press('f')
            
        elif 'film mode' in comm:
            keyboard.press('t')
            
        Speak("Done sir!")

    def TakeHindi():
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening.....")
            command.pause_threshold = 1
            audio = command.listen(source)
        
        try:
            print("Recognizing.....")
            query = command.recognize_google(audio, language='hi')
            print(f"You said: {query}")
            
        except:
            return "None"
        
        return query.lower()
    
    def Tran():
        Speak("Tell me the line!")
        line = TakeHindi()
        translate_speech = Translator()
        result = translate_speech.translate(line)
        Text = result.text
        Speak("The translation for this line is: "+Text)
    
    def ChromeAuto():
        Speak("Chrome automation started!") 
        
        command = takeCommand()
        
        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')
            
        elif 'open this tab' in command:
            keyboard.press_and_release('ctrl + t')
            
        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')
            
        elif 'history' in command:
            keyboard.press_and_release('ctrl + h')
            
    def screenshot():
        Speak("Ok sir, what should I name that file?")
        path = takeCommand()
        path1name = path + ".png"
        path1 = "C:\\Users\\Samay Ashar\\OneDrive\\Desktop\\JARVIS\\Screenshots by JARVIS\\" + path1name
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile("C:\\Users\\Samay Ashar\\OneDrive\\Desktop\\JARVIS\\Screenshots by JARVIS")
        Speak("Here is your screenshot sir!")         
                    
    while True:
        query = takeCommand()
        
        if 'jarvis are you there' in query:
            Speak("At your service sir!")
        
        elif 'hello' in query:
            Speak("Hello Sir, I am Jarvis.")
            Speak("Your personal AI assistant!")
            Speak("How may I help you?")
            
        elif 'how are you' in query:
            Speak("I am fine sir!")
            Speak("What about you?")
            
        elif 'you need a break' in query:
            Speak("Ok sir, you can call me anytime!")
            Speak("Just say wake up jarvis to call me!")
            break
        
        elif "what's up jarvis" in query:
            Speak("All good sir!")
            
        elif 'i am fine' in query:
            Speak("Great sir!")
            
        elif 'bye' in query:
            Speak("Ok sir, bye!")
            break
        
        elif 'thank you jarvis' in query:
            Speak("My pleasure sir!")
        
        elif 'who has made you' in query:
            Speak("I am made by Samay Ashar.")
        
        elif 'i am feeling bored' in query:
            Speak("I can do many things! I can tell you a joke, get you a solution to your problem, and can play some music and videos for you!")
            Speak("All this can be done with your command! Please tell me what should I do?")
        
        elif 'i need some motivation' in query:
            Speak("All i can say is that stars can't shine without darkness sir!")
            Speak("Life is all about ups and downs! There is always a ray of hope in the dark!")
            Speak("Never lose hope and stay focused! Always believe in yourself sir! That's the ultimate motivation!")

        elif 'what is life' in query:
            Speak("Life is the way we live sir! According to me, we must forget all our sorrows and live life happily to the fullest!")
            Speak("So, enjoy every moment of your life, stay happy always and fulfill all your dreams sir!")
        
        elif 'youtube search' in query:
            Speak("Ok sir, This is what I found for your search!")
            query = query.replace("jarvis", "")
            query = query.replace("youtube search", "")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak("Done sir!")
            
        elif 'search on google' in query:
            Speak("This is what I found for your search sir!")
            query = query.replace("jarvis","")
            query = query.replace("gogle search","")
            pywhatkit.search(query)
            Speak("Done sir!")
            
        elif 'website' in query:
            Speak("Ok sir, Launching...")
            query = query.replace("jarvis","")
            query = query.replace("website","")
            query = query.replace(" ","")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            Speak("Launched!")

        elif 'launch' in query:
            Speak("Tell me the name of the website!")
            name = takeCommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            Speak("Done sir!")
        
        elif 'play music' in query:
            Music()
            
        elif 'wikipedia' in query:
            Speak("Searching Wikipedia...")
            query = query.replace("jarvis","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            Speak(f"According to Wikipedia: {wiki}")
          
        elif 'whatsapp message' in query:
            Whatsapp()  
            
        elif 'screenshot' in query:
            screenshot()

        elif 'open code' in query:
            OpenApps()
            
        elif 'open telegram' in query:
            OpenApps()
        
        elif 'open whatsapp' in query:
            OpenApps()
            
        elif 'open chrome' in query:
            OpenApps()
        
        elif 'open facebook' in query:
            OpenApps()
            
        elif 'open instagram' in query:
            OpenApps()
            
        elif 'open linkedin' in query:
            OpenApps()
            
        elif 'open github' in query:
            OpenApps()
            
        elif 'open maps' in query:
            OpenApps()
            
        elif 'open youtube' in query:
            OpenApps()                   

        elif 'close code' in query:
            CloseApps()
            
        elif 'close telegram' in query:
            CloseApps()
        
        elif 'close whatsapp' in query:
            CloseApps()
            
        elif 'close chrome' in query:
            CloseApps()
        
        elif 'close facebook' in query:
            CloseApps()
            
        elif 'close instagram' in query:
            CloseApps()
            
        elif 'close linkedin' in query:
            CloseApps()
            
        elif 'close github' in query:
            CloseApps()
            
        elif 'close maps' in query:
            CloseApps()
            
        elif 'close youtube' in query:
            CloseApps() 

        elif 'pause' in query:
            keyboard.press('space bar')
            
        elif 'restart' in query:
            keyboard.press('0')                       
            
        elif 'mute' in query:
            keyboard.press('m')
            
        elif 'skip' in query:
            keyboard.press('l')
            
        elif 'back' in query:
            keyboard.press('j')
            
        elif 'full screen' in query:
            keyboard.press('f')
            
        elif 'film mode' in query:
            keyboard.press('t')
            
        elif 'youtube tool' in query:
            YoutubeAuto()
        
        elif 'close this tab' in query:
            keyboard.press_and_release('ctrl + w')
            
        elif 'open this tab' in query:
            keyboard.press_and_release('ctrl + t')
            
        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')
            
        elif 'history' in query:
            keyboard.press_and_release('ctrl + h')
            
        elif 'chrome automation' in query:
            ChromeAuto()
        
        elif 'joke' in query:
            get = pyjokes.get_joke()
            Speak(get)                  
        
        elif 'repeat my words' in query:
            Speak("Speak sir!")
            jj = takeCommand()
            Speak(f"You said: {jj}")       

        elif 'my location' in query:
            Speak("Ok sir. Wait a second!")
            webbrowser.open('https://www.google.com/maps/@22.3578876,73.1939609,15z')
            
        elif 'dictionary' in query:
            Dict()    

        elif 'alarm' in query:
            Speak("Enter the time!")
            time = input(": Enter the time : ")
            
            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")
                
                if now == time:
                    Speak("Time to wake up sir!")
                    playsound('C:\\Users\\Samay Ashar\\OneDrive\\Desktop\\JARVIS\\Jarvis Alarm Ringtone.mp3')
                    Speak("Alarm closed!")
                    
                elif now > time:
                    break
          
        elif 'greetings' in query:
            wishMe()
        
        elif 'email to dad' in query:
            try:
                Speak("What should I say?")
                content = takeCommand()
                to = "ashar.deepak@gmail.com"
                sendEmail(to, content)
                Speak("Email has been sent!")
            except Exception as e:
                print(e)
                Speak("Sorry, my friend Samay. I am not able to send this email")
                
        elif 'email to faldee news and updates' in query:
            try:
                Speak("What should I say?")
                content = takeCommand()
                to = "faldeenewsandupdates@gmail.com"
                sendEmail(to, content)
                Speak("Email has been sent!")
            except Exception as e:
                print(e)
                Speak("Sorry, my friend Samay. I am not able to send this email")
        
        elif 'email to mama' in query:
            try:
                Speak("What should I say?")
                content = takeCommand()
                to = "sameerudeshi83@gmail.com"
                sendEmail(to, content)
                Speak("Email has been sent!")
            except Exception as e:
                print(e)
                Speak("Sorry, my friend Samay. I am not able to send this email")
           
        elif 'video downloader' in query:
            root = Tk()
            root.geometry('500x300')
            root.resizable(0,0)
            root.title("Youtube video downloader")
            Speak("Enter video url here: ")
            
            Label(root,text = "Youtube video downloader",font = 'arial 15 bold').pack()
            link = StringVar()
            Label(root,text = 'Paste Yt Video URL Here',font = 'arial 15 bold').place(x=160,y=60)
            Entry(root,width = 70,textvariable = link).place(x=32,y=90)
            
            
            def VideoDownloader():
                url = YouTube(str(link.get()))
                video = url.streams.first()
                video.download()
                Label(root,text = "Downloaded",font = 'arial 15').place(x=180,y=210)
                
            Button(root,text = "Download",font = 'arial 15 bold',bg = 'pale violet red',padx = 2, command = VideoDownloader).place(x=180,y=150)
            
            root.mainloop()
            Speak("Video has been downloaded!")

        elif 'translator' in query:
            Tran()
            
        elif 'remember that' in query:
            rememberMsg = query.replace("remember that","")
            rememberMsg = rememberMsg.replace("jarvis","")
            Speak("Okay sir! I will remind you that"+rememberMsg)
            remember = open('data.txt','w')
            remember.write(rememberMsg)
            remember.close()
            
        elif 'what do you remember' in query:
            remember = open('data.txt','r')
            Speak("You had told me to remember that" + remember.read())        

        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            query = query.replace("google","")
            Speak("This is what I found on the web, sir!")
            pywhatkit.search(query)
            
            try:
                result = googleScrap.summary(query, 2)
                Speak(result)
            
            except:
                Speak("No speakable data available, sir!")
            
        elif 'temperature' in query:
            Temp()
            
        elif 'read a book' in query:
            Reader()

        elif 'downloading speed' in query:
            SpeedTest()
        
        elif 'uploading speed' in query:
            SpeedTest()
            
        elif 'internet speed' in query:
            SpeedTest()   
        
        elif 'how to' in query:
            Speak("Getting data from the internet!")
            op = query.replace("jarvis","")
            max_result = 1
            how_to_func = search_wikihow(op,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            Speak(how_to_func[0].summary)
         
TaskExe()