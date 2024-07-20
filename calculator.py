from tkinter import *

win=Tk()
win.title("simple calculator")

def add():
    a=int(entn1.get())
    b=int(entn2.get())
    c=a+b
    lbln3.config(text="Result:"+str(c))

def sub():
    a=int(entn1.get())
    b=int(entn2.get())
    c=a-b
    lbln3.config(text="Result:"+str(c))

def mul():
    a=int(entn1.get())
    b=int(entn2.get())
    c=a*b
    lbln3.config(text="Result:"+str(c))

def div():
    a=int(entn1.get())
    b=int(entn2.get())
    c=a/b
    lbln3.config(text="Result:"+str(c))

def clear():
    entn1.delete(0, END)
    entn2.delete(0, END) 
    lbln3.config(text="Result:")

lbln1=Label(win,text="Enter first no:",font=("Arial 18 bold"),fg="blue")
lbln1.place(x=20,y=50)
entn1=Entry(win,font=("Arial 18 bold"),fg="white",bg="red")
entn1.place(x=230,y=50)

lbln2=Label(win,text="Enter second no:",font=("Arial 18 bold"),fg="blue")
lbln2.place(x=20,y=100)
entn2=Entry(win,font=("Arial 18 bold"),fg="white",bg="red")
entn2.place(x=230,y=100)

lbln3=Label(win,text="Result:",font=("Arial 18 bold"),fg="green")
lbln3.place(x=20,y=150)
buttadd=Button(win,text="Add",font=("Arial 18 bold"),fg="blue",bg="aqua",command=add)
buttadd.place(x=30,y=200)

buttsub=Button(win,text="Sub",font=("Arial 18 bold"),fg="blue",bg="yellow",command=sub)
buttsub.place(x=120,y=200)

buttmul=Button(win,text="Mul",font=("Arial 18 bold"),fg="blue",bg="green",command=mul)
buttmul.place(x=250,y=200)

buttdiv=Button(win,text="Division",font=("Arial 18 bold"),fg="blue",bg="pink",command=div)
buttdiv.place(x=370,y=200)

buttclear=Button(win,text="Clear",font=("Arial 18 bold"),fg="blue",bg="red",command=clear)
buttclear.place(x=30,y=280)

#win.geometry("500*300")
win.mainloop()












