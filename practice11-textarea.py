from tkinter import *

def submit():
    input=text.get("1.0",END)
    print(input)

window=Tk()
text=Text(window)
text.pack()
button=Button(window,text="Submit",command=submit)
button.pack()

window.mainloop()