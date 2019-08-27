# This program is by: Nidhi Patel
# It uses: Python & Tkinter 
# It answers user's question using an api system.


from tkinter import * 
import wolframalpha

def answer(): 
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
theLabel.grid(row=1, column =1)
theLabel.config(font=("Times", 17))

entry = Entry(root, bg='light grey', font=35)
entry.place(x = 10, y= 50, height= 40, width = 290)
button = Button(root, text ="Enter", width = 8, font=20, height= 1, command=lambda:answer())
button.place(x=310,y=50)

# the output system of the code.
output = Text(bg='light grey')
output.config(state=DISABLED)
output.place(x=10, y= 100, height = 290, width= 360)

root.mainloop()

