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
    output.insert(END, ("User's Question: " + question + '\n'))
    
    app_id = "ELVQP7-XW8G556KRV"
    client = wolframalpha.Client(app_id)

    res = client.query(question)
    answer = next(res.results).text

    output.insert(END, ("Chatbot: " + answer + '\n'))
    output.config(font=("Times", 15))

# This program is for the main background of the function
root = Tk() 
root.title("Chatbot")
root.geometry('400x400')


# tells the user to enter the question 
theLabel = Label(root, text=" Enter your question here:")
theLabel.config(font=("Times", 17))
theLabel.grid(row=0, column=0)


entry = Entry(root, bg='light grey', font=35)
entry.bind("<Return>", answer)
entry.grid(row=1, column=0)

button_listen = Button(root, text= "Listen", width = 8, font=20, height=1)
button_listen.grid(row=0, column=1)

# the output system of the code.
output = Text(bg='light grey', height = 20, width= 50)
output.config(state=DISABLED)
output.grid(row=2, column=0)

root.mainloop()

