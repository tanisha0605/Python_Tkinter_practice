from tkinter import *

food=["pizza","hamburger","hotdog"]

def order():
    if(x.get()==0):
        print("You ordered a pizza")
    elif(x.get()==1):
        print("You ordered a hamburger")
    elif(x.get()==2):
        print("You ordered a hotdog")
    else:
        print("Huh!?")

window=Tk()
window.geometry("420x420")
window.title("Practice 6")

x=IntVar()

for index in range(len(food)):
    radiobutton=Radiobutton(window,
                            text=food[index], #adds text to radio button
                            variable=x, #groups radiobuttons together if they share the same variable
                            value=index, #assigns each radio button a different value
                            padx=25,
                            font=("Impact",50),
                            #indicatoron=0,
                            #width=375,
                            command=order
                            )

    radiobutton.pack(anchor=W)
window.mainloop()