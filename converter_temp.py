from tkinter import *

window = Tk()

e0 = Label(window,text="Enter the temperature in Celcius:")
e1 = StringVar()
e2 = Entry(window,textvariable=e1)
e3 = Label(window,text="Here is the convertion in Farenheit:")

t0 = Text(window,height=1,width=20)

def convert():
    farenheit = float(e1.get())*1.8+32

    t0.delete("1.0",END)
    t0.insert(END,farenheit)

b = Button(window,text="Convert",command=convert)

e0.grid(row=0,column=0)
e2.grid(row=0,column=1)
e3.grid(row=1,column=0)
t0.grid(row=1,column=1)
b.grid(row=2,column=0)

window.mainloop()
