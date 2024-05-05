from tkinter import *

def display():
    if(x.get()==1):
        print("You agree!")
    else:
        print("You don't agree :(")

window=Tk()

x = IntVar()

check_button= Checkbutton(window,
                         text="I agree to something",
                         variable=x,
                         onvalue=1,
                         offvalue=0,
                         command=display,
                         font=("Arial",20),
                         fg='#0000FF',
                         bg='white',
                         activeforeground='#0000FF',
                         activebackground='white',
                         padx=25,
                         pady=10
                         )

check_button.pack()

window.mainloop()