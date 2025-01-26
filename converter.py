from tkinter import *

window = Tk()

def convert():
    #convert Kg to Grams
    gram = float(e1.get())*1000
    #convert Kg to Pounds
    pound = float(e1.get())*2.20462
    #convert Kg to Ounce
    ounce = float(e1.get())*35.274

    #END is a constant in Tkinter that represents the end of the content in the Text widget.
    #1.0 means the first line and the 0th character (the very beginning of the text).
    t0.delete("1.0",END)
    t0.insert(END,gram)

    t1.delete("1.0",END)
    t1.insert(END,pound)

    t2.delete("1.0",END)
    t2.insert(END,ounce)

#creating the label widgets
e0 = Label(window,text="Enter the weight in Kg:")
e1 = StringVar()
e2 = Entry(window,textvariable=e1)
e3 = Label(window,text="Grams")
e4 = Label(window,text="Pounds")
e5 = Label(window,text="Ounce")

#creating the text widgets
t0 = Text(window,height=1,width=20)
t1 = Text(window,height=1,width=20)
t2 = Text(window,height=1,width=20)

#creating the button widget
b = Button(window,text="Convert",command=convert)

#grid method used for placement
#widget placed in table format

e0.grid(row=0,column=0)
e2.grid(row=0,column=1)
e3.grid(row=1,column=0)
e4.grid(row=1,column=1)
e5.grid(row=1,column=2)

t0.grid(row=2,column=0)
t1.grid(row=2,column=1)
t2.grid(row=2,column=2)

b.grid(row=0,column=2)

window.mainloop()