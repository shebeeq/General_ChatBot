import wolframalpha
import webbrowser
import pyttsx3
import wikipedia
import tkinter
from tkinter import *

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def chatbot_response(msg):
    res = msg.lower()
    stopwords = ['hello', 'sam', 'Hi', 'Hey', 'bot']
    querywords = res.split()

    resultwords  = [word for word in querywords if word.lower() not in stopwords]
    query = ' '.join(resultwords)
    try:
        query = query.replace('sam', '')
        client = wolframalpha.Client("***Paste Your API Key Here**") # Login to wolframalpha and  get Your API Key Here....!!!
        res = client.query(query)
        ans = next(res.results).text
        return ans
        
    except Exception:
        try:
            results = wikipedia.summary(query, sentences=2)
            return results

        except:
            return "Nothing Found"
            


def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    
    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))

        res = chatbot_response(msg)
        ChatLog.insert(END, "Fusi: " + res + '\n\n')
        speak(res)

        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
        


base = Tk()
base.title("Bot: Your Query Companion")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)


#Create Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)

ChatLog.config(state=NORMAL)
ChatLog.insert(END,"I am Bot and here to help you to address  your queries in general and scientific questions \n\n")

ChatLog.config(state=DISABLED)


#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height="5",
                    bd=0, bg="green", activebackground="#3c9d9b",fg='#ffffff', relief="sunken",
                    command= send )

#Create the box to enter message
EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")
#EntryBox.bind("<Return>", send)


#Place all components on the screen
scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)

base.mainloop()