# This program is by: Nidhi Patel
# It uses: Python & Tkinter 
# It answers user's question using an api system.


from tkinter import * 
import wolframalpha
import speech_recognition as sr

def answer(*args): 
    output.config(state=NORMAL)
    question = entry.get()
    entry.delete(0, END)
    print (question)
    output.insert(END, ("User: " + question + '\n'))
    
    app_id = "ELVQP7-XW8G556KRV"
    client = wolframalpha.Client(app_id)

    res = client.query(question)
    answer = next(res.results).text

    output.insert(END, ("Chatbot: " + answer + '\n'))
    output.see('end')
    
    
def answer_listen(text): 
    output.config(state=NORMAL)
    output.insert(END, ("User: " + text + '\n'))
    
    app_id = "ELVQP7-XW8G556KRV"
    client = wolframalpha.Client(app_id)

    res = client.query(text)
    answer = next(res.results).text

    output.insert(END, ("Chatbot: " + answer + '\n'))
    output.see('end')
    

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Speak into the mic: ")
        audio = r.listen(source)
    
    try:
        print("Transcription: " + r.recognize_google(audio))
        answer_listen(r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Audio unintelligible")
    except sr.RequestError as e:
        print("Cannot obtain results; {0}".format(e))

# This program is for the main background of the function
root = Tk() 
root.title("Chatbot")
root.geometry('766x590')

scroll = Scrollbar(root, bg='black', troughcolor='light green', width=8)
scroll.grid(row=0, column=1, sticky=N+S+W+E)

entry = Entry(root, bg='black', fg='light green', font=35)
entry.bind("<Return>", answer)
entry.grid(row=1, column=0, sticky=W+E)

button_listen = Button(root, text= "Listen", command=lambda: listen())
button_listen.grid(row=1, column=1)

# the output system of the code.
output = Text(root, bg='black', fg='light green', height = 35, width= 90, wrap=WORD, yscrollcommand=scroll.set)
output.config(state=DISABLED)
output.grid(row=0, column=0)

scroll.config(command=output.yview)

root.mainloop()

