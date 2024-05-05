from tkinter import *

count = 0

def click():
    global count
    count += 1
    print(count)

window=Tk()
window.geometry("420x420")
window.title("Practice 3")

button=Button(window,
              text='Click me',
              command=click,
              font=("Comic Sans",30),
              fg="#0000FF",
              bg='white',
              activeforeground="#0000FF",
              activebackground="white",
              state=ACTIVE)
button.pack()

window.mainloop()