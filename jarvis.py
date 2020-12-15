
def AI():


    import pyttsx3
    from datetime import datetime
    import speech_recognition as sr
    import wikipedia 
    import webbrowser
    import os
    import smtplib
    import random as rd

    memes_list = ['I gotcha in my sight, leave the memes and try to save your life.', 'Hanging out with some friends is cool but coding 100 lines and getting no error while running is Heaven!!!!!!!!!!', 
    'BedWars: Destroy the Bed,,,,,,,,,,,,,,, ShadowApples: I need to sleep and mod this', 
    'Diamond: I am the Best,,,,,,,,,,,,,,,,,,,,,,,, Netherite: Are you sure about that.', 
    'Dream: Let me speedrun minecraft real quick,,,,,,,,,,,,,,,,,,,,, Me: Lemme Speadrun my homework on the last 10 mins of the due']


    webbrowser.register('chrome',
        None,
        webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')

    engine.setProperty(voices, voices[0].id)


    def speak(audio):
        engine.say(audio)
        engine.runAndWait()


    def wishMe():
        hour = int(datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak("Good Morning")
        elif hour >= 12 and hour<18:
            speak('Good afternoon')
        else:
            speak("Good Evening")
        speak("I am Your Assistant. How may I help you !")


    def takeCommand():
        # Input from microphone and returns string output
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening.....")

            r.pause_threshold = 1

            audio = r.listen(source)

        try:
            print("Recognizing......")
            query = r.recognize_google(audio, language='en-uk')
            print(f"User Said: {query}\n")

        except Exception:
            # print(e)

            print("Say that again...")

            return "None"
        return query

    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('email', 'password')

        server.sendmail('sender email', to, content)
        server.close()


    if __name__ == '__main__':
        wishMe()  
        while True:

            query = takeCommand().lower()

            #Logic for executing 
            if 'wikipedia' in query:
                speak('Searching Wikipedia........')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=3)
                speak("According to wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:

                webbrowser.get('chrome').open('youtube.com')

            elif 'open google' in query:
                webbrowser.get('chrome').open('google.com')

            elif 'open school meet' in query:
                webbrowser.get('chrome').open('https://meet.google.com/?hs=197&pli=1&authuser=1')

            elif 'open chat' in query:
                webbrowser.get('chrome').open('web.whatsapp.com')

            elif 'open media' in query:
                webbrowser.get('chrome').open('github.com')

            elif 'open my website' in query:
                webbrowser.get('chrome').open('https://tkn6qbyjao3lqsopxzkhha-on.drv.tw/School%20Projects/main.html')

            elif 'play surah' in query:

                music_dir = "C:\\Users\\Ahmer Khan\\Downloads\\Test_Surah"

                surah = os.listdir(music_dir)
                print(surah)
                os.startfile(os.path.join(music_dir, surah[0]))

            elif 'the time' in query:
                strTime = datetime.now().strftime("%H;%M;%S")
                speak(f"The time is {strTime}\n")

            elif 'open code' in query:
                code_path = "C:\\Users\\Ahmer Khan\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"

                os.startfile(code_path)

            elif 'open cmd' in query:
                cmd_path = "C:\\Windows\\System32\\cmd.exe"

                os.startfile(cmd_path)

            elif 'email' in query:
                try:
                    speak('What should I say')
                    content = takeCommand()
                    to = "saadyarkhan11@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent")

                
                except Exception as e:
                    print(e)

                    speak('Not sent bhai')

            elif "open classroom" in query:
                webbrowser.get('chrome').open('classroom.google.com/u/1/h')


            elif 'who are you' in query:
                speak('I am better than google')

                speak('Thats it!')

            elif 'start' in query:
                speak('I am started,   BRUH!')


            elif 'meme' in query:
                speak(rd.choice(memes_list))

            elif 'quit' in query:

                speak('Hope you are Satisfied')

                speak('Bye See you soon')

                quit()

AI()
