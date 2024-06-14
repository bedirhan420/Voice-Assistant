import pyttsx3
import speech_recognition as sr
import webbrowser
import random
import os 
import datetime
import pyautogui
import time

songs =["https://www.youtube.com/watch?v=5b2f-kfMQ7I&list=RD5b2f-kfMQ7I&index=1","https://www.youtube.com/watch?v=bvNZeh6f8vE&list=RD5b2f-kfMQ7I&index=2","https://www.youtube.com/watch?v=qa15t50-52U&list=RD5b2f-kfMQ7I&index=3","https://www.youtube.com/watch?v=SVbc_Fwbt50&list=RD5b2f-kfMQ7I&index=5","https://www.youtube.com/watch?v=aXsLlOPwe48&list=RD5b2f-kfMQ7I&index=6","https://www.youtube.com/watch?v=-UldvT2zJKI&list=RD5b2f-kfMQ7I&index=8","https://www.youtube.com/watch?v=052sPiY3vqI&list=RD5b2f-kfMQ7I&index=9","https://www.youtube.com/watch?v=IvUU8joBb1Q&list=RD5b2f-kfMQ7I&index=10","https://www.youtube.com/watch?v=JhiUacGzIg8&list=RD5b2f-kfMQ7I&index=11","https://www.youtube.com/watch?v=ch-fed2_swY&list=RD5b2f-kfMQ7I&index=12"]
sites =[["youtube","https://www.youtube.com"],["instagram","https://www.instagram.com"],["whatsapp","https://web.whatsapp.com"],["wikipedia","https://www.wikipedia.org"]]
applications =[["discord","C:\\Users\\bedir\\OneDrive\\Masaüstü\\Discord.lnk"],["game","C:\\Users\\Public\\Desktop\\Legends_of_Runeterra.lnk"],["visual studio code","C:\\Users\\bedir\\OneDrive\\Masaüstü\\Visual_Studio_Code.lnk"],["visual studio","C:\\Users\\bedir\\OneDrive\\Masaüstü\\Visual_Studio_2022.lnk"]]
peoples = [["father","babam"],["mom","Annem"],["brother","kardeşim"],["family","ailem"]]

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def take_command(help_msg):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        print("Listening...")
        say(help_msg)
        try:
            audio = r.listen(source, timeout=30, phrase_time_limit=30)
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User Said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I did not understand. Please try again.")
            say("Sorry, I did not understand. Please try again.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""
        except sr.WaitTimeoutError:
            print("Listening timed out. Please speak within the provided time limit.")
            say("Listening timed out. Please speak within the provided time limit.")
            exit()
        
def open_site(text):
    for site in sites:
            if f"open {site[0]}".lower() in text.lower():
                say(f"Opening {site[0]} Sir ...")
                webbrowser.open(site[1])

def play_song():
    say("Playing any song sir ...")
    index=random.randint(0,9)
    url=songs[index]
    webbrowser.open(url)

def open_viking_radio():
    say("Opening Herknungr Live Radio sir ...")
    index=random.randint(0,9)
    url=songs[index]
    webbrowser.open("https://www.youtube.com/watch?v=CcVqy90Iy4E")

def open_application(text):
    for application in applications:
            if f"open {application[0]}".lower() in text.lower():
                path=application[1]
                say(f"Opening {application[0]} Sir ...")
                os.system(f"start {path}")

def write(text,param):
    pyautogui.typewrite(text.split(param)[1])

def press_enter():
    pyautogui.press("enter")

def open_notepad():
    pyautogui.hotkey('winleft', 'r')
    pyautogui.write("notepad")
    press_enter()

def search_on_youtube(text,param):
    for i in range(4):
        pyautogui.press("tab")
    write(text,param)
    press_enter()

def send_messaage(msg,whom):
    pyautogui.hotkey("alt","tab")
    open_site("open whatsapp")
    time.sleep(15)
    for i in range(7):
        pyautogui.press("tab")
    pyautogui.write(whom.lower())
    time.sleep(0.5)
    press_enter(),
    press_enter()
    time.sleep(0.5)
    pyautogui.write(msg)
    time.sleep(0.5)
    press_enter()  
    
if __name__ == "__main__":
    say("Hello       I'm     JARVIS     AI")
    control = ""
    while "stop" not in control.lower():
        text = take_command("How can I assist you?")
        control = text.lower()
        open_site(text) 
        open_application(text)
        if "play song" in text.lower():
            play_song()
        elif "open viking radio" in text.lower():
            open_viking_radio()
        elif "open notepad" in text.lower():
            open_notepad()
        elif "the time" in text.lower():
            hour = datetime.datetime.now().strftime("%H")
            minute = datetime.datetime.now().strftime("%M")
            say(f"Sir the time is {hour}     {minute}")
        elif "write" in text.lower(): 
            write(text,"write")
            press_enter()
        elif "search" in text.lower():
            write(text,"search")
            press_enter()
        elif "search on youtube" in text.lower():
            search_on_youtube(text,"youtube")
        elif "send message to" in text.lower():
            msg=take_command("Please say the message you want to send")
            for people in peoples:
                if people[0] in text.split("to")[1].lower():
                    print(people[1])
                    send_messaage(msg,people[1])
        

    say("See you later")                    

