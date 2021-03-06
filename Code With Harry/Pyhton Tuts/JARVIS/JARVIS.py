import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import googlesearch
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)


def Speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        Speak("Good Afternoon!")

    else:
        Speak("Good Evening!")

    Speak("JARVIS at your service sir.")

def TakeCommand():
    # It takes microphone input and returns string output.

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 1500
        r.pause_threshold = 1  # seconds of non-speaking audio before a phrase is considered complete.
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n") 

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def sendemail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('patiljay32145@gmail.com', 'Jaypatil@1234')
    server.sendmail('patiljay32145@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    WishMe()
    while True:
        query = TakeCommand().lower()
        Greeting = ["hi", "hello", "hey"]

        # Logic for executing tasks based on query.
        if Greeting[0] in query:
            Speak("Hi there! How may i help you?")

        if Greeting[1] in query:
            Speak("Hello. What can i do for you?")

        if Greeting[2] in query:
            Speak("Hi How may i help you?")

        if 'wikipedia' in query:
            print("Searching Wikipedia...")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            Speak("According to Wikipedia")
            print(results)
            Speak(results)
            Speak("Do you need something else?")
            W = TakeCommand()
            if 'yes' in W:
                Speak("You may speak to me now.")
                continue
            elif 'no' in W:
                Speak("Thanks for using me.")
                exit()


        elif 'search youtube' in query:
            Speak("What do you want to search?")
            S = TakeCommand()
            print("Searching...")
            Speak("Here's your result.")
            webbrowser.open(f'https://www.youtube.com/results?search_query={S}')
            Speak("Do you need something else?")
            U = TakeCommand()
            if 'yes' in U:
                Speak("You may speak to me now.")
                continue
            elif 'no' in U:
                Speak("Thanks for using me.")
                exit()

        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com/')
            print("Opened.")
            Speak("Do you need anthing else?")
            YsU = TakeCommand()
            if 'yes' in YsU:
                Speak("You may speak to me now.")
                continue
            elif 'no' in YsU:
                Speak("Thanks for using me. Bye.")
                exit()

        elif 'search google' in query:
            Speak("What do you want to search?")
            G = TakeCommand()
            print("Searching...")
            Speak("Here's your result.")
            webbrowser.open(f'https://www.google.com/search?source=hp&ei=pX7XXtutNeHA3LUP35uR0A0&q={G}')
            Speak("Do you need anthing else?")
            GssU = TakeCommand()
            if 'yes' in GssU:
                Speak("You may speak to me now.")
                continue
            elif 'no' in GssU:
                Speak("Thanks for using me. Bye.")
                exit()

        elif 'google' in query:
            webbrowser.open('https://www.google.com/')
            print("Opened.")
            Speak("Do you need anthing else?")
            GsU = TakeCommand()
            if 'yes' in GsU:
                Speak("You may speak to me now.")
                continue
            elif 'no' in GsU:
                Speak("Thanks for using me. Bye.")
                exit()
            
        elif 'stack overflow' in query:
            webbrowser.open('https://stackoverflow.com/')
            print("Opened.")
            Speak("Do you need anthing else?")
            SsU = TakeCommand()
            if 'yes' in SsU:
                Speak("You may speak to me now.")
                continue
            elif 'no' in SsU:
                Speak("Thanks for using me. Bye.")
                exit()

        elif 'music' in query:
            print("Playing..")
            music_dir = 'C:\\Songs' # Give the path of the file.
            songs = os.listdir(music_dir)
            # print(songs)
            Speak("I would leave now. You enjoy the music.")
            os.startfile(os.path.join(music_dir, random.choice(songs)))
            exit()        

        elif 'time' in query:
            srttime = datetime.datetime.now().strftime("%H:%M:%S")
            Speak(f"The time is {srttime}")

        elif 'open vs code' in query:
            VSCode = "C:\\Users\\SHREE\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            print("Opened.")
            os.startfile(VSCode)
            Speak("Do you need anthing else?")
            VsU = TakeCommand()
            if 'yes' in VsU:
                Speak("You may speak to me now.")
                continue
            elif 'no' in VsU:
                Speak("Thanks for using me. Bye.")
                exit()

        elif 'email' in query:  # Admin.google.com
            try:
              Speak("What should i say?")
              content = TakeCommand()
              to = "patiljay32145@gmail.com" 
              sendemail(to, content)
              Speak("Email sent.")
            except Exception as e:
                print("The email couldn't be sent now.")
                Speak("The mail couldn't be sent now.") 

        elif 'desktop' in query:
            D = "C:\\Users\\SHREE\\Desktop"
            print("Opened.")
            os.startfile(D)
            Speak("Do you need anthing else?")
            DyU = TakeCommand()
            if 'yes' in DyU:
                Speak("You may speak to me now.")
                continue
            elif 'no' in DyU:
                Speak("Thanks for using me. Bye.")
                exit()

        elif 'downloads' in query:
            Do = "C:\\Users\\SHREE\\Downloads"
            print("Opened.")
            os.startfile(Do)
            Speak("Do you need anthing else?")
            DoU = TakeCommand()
            if 'yes' in DoU:
                Speak("You may speak to me now.")
                continue
            elif 'no' in DoU:
                Speak("Thanks for using me. Bye.")
                exit()

        elif 'online lectures' in query:
            L = "C:\\Users\\SHREE\\Desktop\\JAY\\Online Lectures"
            print("Opened.")
            os.startfile(L)
            Speak("Do you need anthing else?")
            LyU = TakeCommand()
            if 'yes' in LyU:
                Speak("You may speak to me now.")
                continue
            elif 'no' in LyU:
                Speak("Thanks for using me. Bye.")
                exit()

        elif 'recorded lectures' in query:
            Rl = "C:\\Users\\SHREE\\Desktop\\JAY\\Recorded Lectures"
            print("Opened.")
            os.startfile(Rl)
            Speak("Do you need anythin else?")
            RlU = TakeCommand()
            if 'yes' in RlU:
                Speak("You may speak to me now.")
                continue
            elif 'no' in RlU:
                Speak("Thanks for using me. Bye.")
                exit()

        elif 'tuition' in query:
            Speak("Maths or Science?")
            MrS = TakeCommand()
            if 'maths' in MrS:
                os.startfile("C:\\Users\\SHREE\\Desktop\\JAY\\Tuition (Maths)")
                print("Opened.")
            elif 'science' in MrS:
                os.startfile("C:\\Users\\SHREE\\Desktop\\JAY\\Tuition (Science)")
                print("Opened.")
            Speak("Do you need anything else?")
            TuU = TakeCommand()
            if 'yes' in TuU:
                Speak("You may speak to me now.")
                continue
            elif 'no' in TuU:
                Speak("Thanks for using me. Bye.")
                exit()

        elif 'revise' in query:
            Speak("From where do you want to revise? Byju's or My CBSE Guide? Or you want solutions?")
            Rw = TakeCommand()
            os.startfile(f"C:\\Users\\SHREE\\Desktop\\JAY\\Self Study\\{Rw.capitalize()}")
            print("Opened.")
            Speak("Do you want anything else?")
            RwU = TakeCommand()
            if 'yes' in RwU:
                Speak("You may speak to me now.")
                continue
            elif 'no' in RwU:
                Speak("Thanks for using me. Bye.")
                exit()

        elif 'rd sharma' in query:
            RdS = "C:\\Users\\SHREE\\Desktop\\JAY\\Self Study\\SOLUTIONS\\RD SHARMA CLASS 10 SOLUTIONS"
            os.startfile(RdS)
            print("Opened.")
            Speak("Do you need anything else?")
            RdsU = TakeCommand()
            if 'yes' in RdsU:
                Speak("You may speak to me now.")
                continue
            elif 'no' in RdsU:
                Speak("Thanks for using me. Bye.")
                exit()

        elif 'download revision' in query:
            Speak("From where do you want to download? Byju's ofMy CBSE Guide?")
            DoR = TakeCommand()
            if "byju's" in DoR:
                webbrowser.open("https://learn.byjus.com/revision/dashboard")
                print("Opened.")
            elif 'my cbse guide' in DoR:
                webbrowser.open("https://mycbseguide.com/dashboard/home")
                print("Opened.")
            Speak("Do you need anything else?")
            DouR = TakeCommand()
            if 'yes' in DouR:
                Speak("You may speak to me now.")
                continue
            elif 'no' in DouR:
                Speak("Thanks for using me. Bye.")
                exit()

        elif 'start zoom' in query:
            Z = "C:\\Users\\SHREE\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Zoom\\Start Zoom"
            print("Opened.")
            os.startfile(Z)
            Speak("Do you need anthing else?")
            ZyU = TakeCommand()
            if 'yes' in ZyU:
                Speak("You may speak to me now.")
                continue
            elif 'no' in ZyU:
                Speak("Thanks for using me. Bye.")
                exit()

        elif 'open drive' in query:
            GooD = "C:\\Users\\SHREE\\Desktop\\JAY\\Google Drive"
            os.startfile(GooD)
            print("Opened.")
            Speak("Do you need anything else?")
            GoDU = TakeCommand()
            if 'yes' in GoDU:
                Speak("You may speak to me now.")
                continue
            elif 'no' in GoDU:
                Speak("Thanks for using me. Bye.")
                exit()

        elif 'open web drive' in query:
            Speak("Which drive you want to open? 10th or 8th standard?")
            WCl = TakeCommand()
            if 'tenth' in WCl:
                webbrowser.open('https://drive.google.com/drive/folders/1SjHQjfBnpsxzP0oVX0IQBXY6fgvegIor')
                print("Opened.")
                Speak("Do you need anyting else?")
                GooDW1=TakeCommand()
                if 'yes' in GooDW1:
                    Speak("You may speak to me now.")
                    continue
                elif 'no' in GooDW1:
                    Speak("Thanks for using me.Bye.")
                    exit()

            elif '8' in WCl:
                webbrowser.open('https://drive.google.com/drive/u/1/folders/1SdYVMXCuC-7Rw5xApOWbZAfnqQ_4HUh1')
                print("Opened.")
                Speak("Do you need anything else?")
                GooDW=TakeCommand()
                if 'yes' in GooDW:
                    Speak('You may speak to me now.')
                    continue
                elif 'no' in GooDW:
                    Speak("Thanks for using me.Bye.")
                    exit()

        elif 'open python' in query:
            Speak("What do you want to open?") 
            Speak("Press 1 for Folder\n2 for IDE.")
            P = int(input("Enter: \n1 for Folder\n2 for IDE\n"))
            if P == 1:
                PyF = "C:\\Users\\SHREE\\Jay (Coding)"
                print("Opened.")
                os.startfile(PyF)
                Speak("Do you need anthing else?")
                PfyU = TakeCommand()
                if 'yes' in PfyU:
                    Speak("You may speak to me now.")
                    continue
                elif 'no' in PfyU:
                    Speak("Thanks for using me. Bye.")
                    exit()
            
            elif P == 2:
                Speak("Which one should i open?")
                Speak("Press 1 for VSCode and 2 for Py-charm")
                Ide = int(input("Enter:\n1 for VSCode\n2 for Pycharm\n"))
                
                if Ide == 1:
                    V = "C:\\Users\\SHREE\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    print("Opened.")
                    os.startfile(V)
                    Speak("Do you need anthing else?")
                    VyU = TakeCommand()
                    if 'yes' in VyU:
                        Speak("You may speak to me now.")
                        continue
                    elif 'no' in VyU:
                        Speak("Thanks for using me.Bye.")
                        exit()
                    
                
                elif Ide == 2:
                    PyC = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.1\\bin\\pycharm64.exe"
                    print("Opened.")
                    os.startfile(PyC)
                    Speak("Do you need somethin else?")
                    PyU = TakeCommand()
                    if 'yes' in PyU:
                        Speak("You may speak to me now.")
                        continue
                    elif 'no' in PyU:
                        Speak("Thanks for using me. Bye.")
                        exit()
        
        elif 'whatsapp' in query:
            W = "C:\\Users\\SHREE\\AppData\\Local\\WhatsApp\\WhatsApp"
            print("Opended.")
            os.startfile(W)
            Speak("Do you need anything else?")
            WhU = TakeCommand()
            if 'yes' in WhU:
                Speak("You may speak to me now.")
                continue
            elif 'no' in WhU:
                Speak("Thanks for using me. Bye.")
                exit()

        elif 'thanks' in query:
            Speak("Welcome. Bye.")
        
        elif 'bye' in query:
            Speak("Bye. Thanks for using me.")
            exit()

# This can be used to:
# 1] Open and Search Google and Youtube.
# 2] Open Desktop and Downloads (of this PC only).
# 3] Open Online Lectures file (JAY).
# 4] Start Zoom.
# 5] Open Python (Folder and IDE).
# 6] Open Recorded Lectures (JAY).
# 7] Open WhatsApp.
# 8] Search on Wikipedia.
# 9] Open stackoverflow.com (Programming).
# 10] Play Music.
# 11] Send an Email (from Jay to Jay)(update in progress).
# 12] Know Time.
# 13] Open Tution Folder (JAY).
# 14] Open Revision Folder (JAY).
# 15] Download PDF for revision (JAY).
# 16] Open Google Drive (Folder, On Web).
