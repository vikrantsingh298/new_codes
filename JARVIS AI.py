import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser


engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<15:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")  

    speak(" I am Victor, Victor the Robot, Speed 1 tera-hertz, memory 1 zeta-byte!!!!! so, how can I help You")     
       
def takeCommand():


    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1 
        r.energy_threshold = 500
        
        audio=r.listen(source)     

    try:
        print("Recognizing.....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n") 

    except Exception as e:
        print(e)
        print("Say that again please...")   
        return "None"  
    return query      
           
def askpass():
    speak("Please Input The password Sir!!")
    
    i=1
    while i<=4:
        
        n=takeCommand().lower()

        if  n=='home':
           speak("Welcome! Mister Vikrant!")
           break
    

        elif n!='home' and (i==1 ):
            speak("Wrong Password!! please try again") 

        elif n!='home' and i==2:
            speak("Get lost! or else I will call the police!!")
            exit()

        i=i+1        
          


      
if __name__ == "__main__":
    askpass()
    wishMe()
    while True:
    
        query=takeCommand().lower()
        if 'jarvis' in query:
            speak("Sorry Sir! But I am not Jarvis, i am Victor")

        else:  


            if 'wikipedia' in query:
               speak("Searching on Wikipedia......")
               query=query.replace("wikipedia","")
               results=wikipedia.summary(query,sentences=2)
               speak("According to Wikipedia")
               print(results)
               speak(results)


            elif'open youtube' in query:
               webbrowser.open("youtube.com")

            elif'open facebook' in query:
               webbrowser.open("facebook.com")

            elif 'search' in query:
               query=query.replace("search","")
               speak(f"searching {query}")
               webbrowser.open(f"{query}")

            elif'open gmail' in query:
               webbrowser.open("gmail.com") 

            elif'hello victor' in query:
               speak("hello Sir!!")   

            elif'the time' in query:
               strTime=datetime.datetime.now().strftime("%H:%H:%S")
               speak(f"Sir! The time is {strTime}")
                 
            
                       


            elif 'quit' in query:
               speak('Have a good time Sir!, Bye')    
               exit()
                     

    