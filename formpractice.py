from tkinter import *

def gettext():
    print("You clicked the button")
    print("The text is: " + submit_button.cget("text"))


window=Tk()
window.title("Form")
window.geometry("450x450")

title_label=Label(text="Hello, How may I help you!",
      font=('Arial', 15 ,'bold'),
      pady=15)

title_label.grid(row=0,column=3)

name=Label(window,text="Name:")
phone=Label(window,text="Phone:")


name.grid(row=1,column=2)
phone.grid(row=2,column=2)

namevalue=StringVar()
phonevalue=StringVar()
male=StringVar()
female=StringVar()

nameentry = Entry(window, textvariable=namevalue)
phoneentry = Entry(window, textvariable=phonevalue)

nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)

malecheckbox=Checkbutton(text="Male",
                         variable=male,
                         onvalue="Male",
                         )
femalecheckbox=Checkbutton(text="Female",
                           variable=female,
                           onvalue="Female",
                           )

malecheckbox.grid(row=3,column=2)
femalecheckbox.grid(row=3,column=3)

submit_button = Button(window, text="Submit", command=gettext)  
submit_button.grid(row=7, column=3) 

window.mainloop()
