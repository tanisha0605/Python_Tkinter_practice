from tkinter import *

window = Tk()

def getvals():
    print("It works!")
window.geometry("644x344")
#window.config(background='#ffffff')
#Heading
Label(window, text="Welcome to Harry Travels", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

#Text for our form
name = Label(window, text="Name")
phone = Label(window, text="Phone")
gender = Label(window, text="Gender")
emergency = Label(window, text="Emergency Contact")
paymentmode = Label(window, text="Payment Mode")

#Pack text for our form
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)

# Tkinter variable for storing entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()


#Entries for our form
nameentry = Entry(window, textvariable=namevalue)
phoneentry = Entry(window, textvariable=phonevalue)
genderentry = Entry(window, textvariable=gendervalue)
emergencyentry = Entry(window, textvariable=emergencyvalue)
paymentmodeentry = Entry(window, textvariable=paymentmodevalue)

# Packing the Entries
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)

#Checkbox & Packing it
foodservice = Checkbutton(text="Want to prebook your meals?", variable = foodservicevalue)
foodservice.grid(row=6, column=3)

#Button & packing it and assigning it a command
Button(text="Submit to Harry Travels", command=getvals).grid(row=7, column=3)



window.mainloop()