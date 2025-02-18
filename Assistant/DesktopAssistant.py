import pyttsx3                                                            # installing library ( pip install pyttsx3)
import speech_recognition as sr                                           # speech to text module (pip install SpeechRecognition)
import datetime
import os
import random   
import webbrowser
import wikipedia      
import pyjokes   
import subprocess                 
import time   
import pyautogui                                                          # play random media 
import psutil
import socket
import winshell
import sys
import socket
import imdb
import string
import pandas as pd


from   calendar   import *
from   random     import randint
#from   Projects.Assistant.camera     import *
from   GoogleNews import GoogleNews



engine = pyttsx3.init('sapi5')                                             # Holds two voices 0-male, 1-female
voices = engine.getProperty('voices')
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)
else:
    engine.setProperty('voice', voices[0].id)    
    

def password():
    char = string.ascii_letters + string.digits
    ret='' .join(random.choice(char) for x in range (0,15))
    print(ret)

def news():
    news = GoogleNews(period='id')
    news.search("India")
    result = news.result()
    #print(result)
    data = pd.DataFrame.from_dict(result)
    data = data.drop(columns={"img"})
    data.head()

    for i in result:
        speak(i["title"])



def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        r.pause_threshold =2
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            print("Recognizing.....")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query
        except sr.WaitTimeoutError:
            print("Listening timed out. Please try speaking again.")
            return None
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Could you please repeat? ?")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            
        

def username():
    speak(" What should I call you,sir?")
    uname = takecommand()
    if uname:
        speak(" Welcome mister " + uname)
        speak(" How can I help you,sir?")
    else:
        speak(" I couldn't catch your name, could you please tell me again?")

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(" Good Morning Sir!")
    elif hour >=12 and hour < 18:
        speak(" Good Afternoon Sir!")
    else:
        speak(" Good Evening Sir!")
    speak(" I am your assisting partner Kina.")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+ usage)
    battery = str(psutil.sensors_battery())
    speak("CPU is at"+ battery)
    
def movie():
    moviesdb= imdb.IMDB()
    speak(" Please tell me the movie name sir")
    text = takecommand()
    movies= moviesdb.search_movie(text)
    speak(" Searching for" +text)
    if len(movie==0):
        speak(" No result found ")
    else:
        speak(" I found these:")
        for movie in movies:
            title= movie["title"]
            year= movie["year"]
            speak( f'{title} - {year}')
            info= movie.getID()
            movie= moviesdb.get_movie(info)
            rating = movie["rating"]
            plot= movie['plot outline']
            if year<int(datetime.datetime.now().strftime("%y")):
                speak( f'(title) was released in {year} has IMDB rating of {rating}. The plot summary of movie id {plot}')
                break
            else:
                speak( f'{title} will be released in {year} has IMDb rating of {rating}. The plot summary of movie is {plot}')
                break

def rock():
    you = int (input(" Pleae enter your choice:- \n 1-Rock \n 2-Paper \n 3-Scissor"))
    shapes = {1:'rock', 2:'paper', 3:'scissor'}
    if you not in shapes:
        print(" Please enter a valid number")
        exit()
        
    comp = random.randint(1,3)
    print(" you choose", you)
    print("Computer choose", comp)
    if(you==1) and (comp==3) or (you==2) and (comp==1) or (you==3) and (comp==2):
        speak("Congratulations you won!")
    elif(you==comp):
        speak("Match tied")
    else:
        speak("You loose")
        
        
def count():
    t = int (input(" Enter time in seconds: "))
    while t:
        min, secs= divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(min,secs)
        print(timer, end = "\r")
        time.sleep(1)
        t-=1
        print("\n")
        
        
def guess():
    start=1
    end=1000
    value = randint(start,end) 
    print("The computer choose a number between", start, "and", end)
    guess = None
    while guess != value:
        text = input(" Guess the number; ")
        guess = int(text)
        if guess < value:
            speak("The number is higher")
        elif guess > value:
            speak(" The number is lower")
            
    speak("Congratulations!! you won")
        
    
    

if __name__ == '__main__':
    wishMe()
    username()

    while True:
        order = takecommand().lower()

        if 'how are you' in order:
            speak(" I an great, Thankyou for asking.")
            speak(" How are you Sir?")

        elif 'fine' in order or 'good' in order:
            speak(" It's good to know that you are doing fine.")

        elif 'who i am' in order:
            speak(" If you can talk then suerly you are a human")

        elif 'What is love' in order:
            speak(" The permanent 404 error whenever you try to find logical reasoning.")

        elif 'who are u' in order:
            speak(" I’m the Wi-Fi wizard with answers. No magic wand, but lots of bandwidth.")

        elif 'I love You' in order:
            speak(" well that's sweet, but Are you sure you’re not just in love with the fact that I can’t argue back?")

        elif 'will you be my girlfriend' in order or 'will you be my valientine' in order:
            speak (" Oh, how sweet! But I’m afraid my heart is full... of code.")

        elif 'what is your name' in order:
            speak(" Well, my friends call me kina , but you can call me kinu. ")

        elif 'open notepad' in order:
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)

        elif 'play music' in order or 'play songs' in order:
            music_dir = "C:\\Others\\Song\\Hindi"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir,rd))
            
        elif 'open Brave' in order:
            npath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Brave.lnk"
            os.startfile(npath)
            
        elif 'open Chrome' in order:
            npath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"
            os.startfile(npath)


        elif('wikipedia') in order:
            speak("Searching.... \n")
            order=order.replace("wikipedia"," ")
            results = wikipedia.summary(order,sentences=2)
            speak(" According to wikipedia")
            speak(results)
        
        elif 'open google' in order :
            speak(" Opening google Sir \n")
            webbrowser.open("google.com")

        elif 'open myntra' in order:
            speak(" Opening myntra Sir \n")
            webbrowser.open("myntra.com")
        
        elif 'open youtube' in order:
            speak(" Opening Youtube Sir \n")
            webbrowser.open("youtube.com")

        elif 'open amazon' in order:
            speak(" Opening Amazon \n")
            webbrowser.open("Amazon.in")

        elif 'open Stackoverflow' in order:
            speak(" Opening Stackoverflow Sir \n")
            webbrowser.open("Stackoverflow.com")

        elif 'where is' in order:
            order=order.replace("where is","")
            location=order
            speak(" Locating....")
            speak(location)
            webbrowser.open("https://www.google.co.in/maps/place/"+location+"")
        
        elif 'Write a note' in order:
            speak(" What should i write Sir?")
            note = takecommand()
            file = open('jarvis.txt','w')
            speak(" Sir,Should i include date and time as well?")
            sn=takecommand()
            if 'yes' in sn or 'sure' in sn or 'yeah' in sn:
                strTime = datetime.datetime.now().strftime("%H: %M: %S:")
                file.write(strTime)
                file.write(note)
                speak(" Done Sir!")
            else:
                file.write(note)
                speak(" Done Sir!")

        elif 'Show note' in order:
            speak(" Showing Notes")
            file = open("jarvix.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif 'joke' in order:
            speak(pyjokes.get_joke(language="en",category="neutral"))   

        elif 'the time' in order:
            strTime = datetime.datetime.now().strftime("%H: %M: %S:") 
            speak(f" Well the time is {strTime}")

        elif 'shutdown' in order or 'turn off' in order:
            speak(" Hold on a second Sir! Your system is on its way to Shutdown")
            speak(" Make Sure all your Applications are Closed")
            time.sleep(5)
            subprocess.call(['shutdown','/s'])

        elif 'restart' in order:
            subprocess.call(['shutdown','/r'])

        elif 'hibernate' in order:
            speak(" Hibernating...")
            subprocess.call(['shutdown','/h'])


        elif 'sign out' in order or 'log off' in order:
            speak(" Make Sure all your Applications are Closed before signing out Sir")
            time.sleep(5)
            subprocess.call(['shutdown','/i'])
        
        elif 'switch window' in order:
            pyautogui.keydown('alt')                        # to take screenshot we press first alt button                                                                            
            pyautogui.press('tab')                          # then be press tab buttpon
            time.sleep(1)                                   # this will take some time , so we put assistant to sleep 
            pyautogui.keyUp('alt')                          # then we lift the alt button

        elif 'take a screenshot' in order or 'screenshot this' in order:
            speak(" please tell me the name for this file.")
            name = takecommand().lower()
            speak(" Please hold the screen")
            time.sleep(3)
            img =pyautogui.screenshot()
            img.save(f"name.png")
            speak(" Screenshot captured Sir!")
        
        elif 'cpu status' in order:
            cpu()

        elif 'empty recycle bin' in order:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("recycle bin recycled")

        
            
        elif 'exit' in order or 'quit' in order:
            speak("Thankyou for using me sir, Have a good day ")
            sys.exit()
            
        elif 'ip' in order:
            host=socket.gethostname()
            ip=socket.gethostbyname(host)
            speak(" Your ip address is " +ip)
            
        elif 'bmi' in order:
            speak("Please tell your hight in centimeters")
            height= takecommand()
            speak("Please tell your weight in kilograms")
            weight= takecommand()
            height= float (height)/100
            BMI= float (weight)/(height*height)
            speak(" Your bodymass index is"+ str(BMI))
            if (BMI>0):
                if (BMI <=16):
                    speak("You are severly underweight")
                elif (BMI <=18.5):
                    speak("You are underweight")   
                elif (BMI <=25):
                    speak("You are healthy")
                elif (BMI <=30):
                    speak("You are severly overweight")
                else:
                    speak("you are severly overweight")
            else:
                speak("Enter valid details") 
                
        elif 'movie' in order:
            movie()
                    
        
        elif 'news' in order:
            news()
            
        elif 'password' in order:
            password()
            
        elif 'rock' in order:
            rock()
            
        elif 'guess' in order:
            guess()
            
        elif 'countdown' in order:
            count()
            