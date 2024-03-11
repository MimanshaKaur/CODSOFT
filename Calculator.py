from tkinter import *

#creating screen
screen=Tk()
screen.title("CALCULATOR")
screen.geometry("450x600")
screen.configure(background="black")

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def clears():
    global expression
    expression= ""
    input_text.set("")

def res():
    global expression
    result= str(eval(expression))
    input_text.set(result)
    expression= ""

#creating calculator
expression= ""
input_text= StringVar()

lf=LabelFrame(screen)
lf.pack(side=TOP)

output=Entry(lf,textvariable=input_text,font=("cursive",25),background="darkgray",width=20,justify=RIGHT)
output.pack(pady=20,padx=20)

#creating button area
button_frame=Frame(screen,width=350,height=380,background="black",borderwidth=10)
button_frame.pack()

#creating buttons
nine=Button(button_frame,text=9,font=("cursive",20),width=5,height=2,fg="white",bg="red",command= lambda: btn_click(9))
nine.grid(row=1,column=3,padx=7,pady=7)

eight=Button(button_frame,text=8,font=("cursive",20),width=5,height=2,fg="white",bg="red",command= lambda: btn_click(8))
eight.grid(row=1,column=2,padx=7,pady=7)

seven=Button(button_frame,text=7,font=("cursive",20),width=5,height=2,fg="white",bg="red",command= lambda: btn_click(7))
seven.grid(row=1,column=1,padx=7,pady=7)

six=Button(button_frame,text=6,font=("cursive",20),width=5,height=2,fg="white",bg="red",command= lambda: btn_click(6))
six.grid(row=2,column=3,padx=7,pady=7)

five=Button(button_frame,text=5,font=("cursive",20),width=5,height=2,fg="white",bg="red",command= lambda: btn_click(5))
five.grid(row=2,column=2,padx=7,pady=7)

four=Button(button_frame,text=4,font=("cursive",20),width=5,height=2,fg="white",bg="red",command= lambda: btn_click(4))
four.grid(row=2,column=1,padx=7,pady=7)

three=Button(button_frame,text=3,font=("cursive",20),width=5,height=2,fg="white",bg="red",command= lambda: btn_click(3))
three.grid(row=3,column=3,padx=7,pady=7)

two=Button(button_frame,text=2,font=("cursive",20),width=5,height=2,fg="white",bg="red",command= lambda: btn_click(2))
two.grid(row=3,column=2,padx=7,pady=7)

one=Button(button_frame,text=1,font=("cursive",20),width=5,height=2,fg="white",bg="red",command= lambda: btn_click(1))
one.grid(row=3,column=1,padx=7,pady=7)

ac=Button(button_frame,text="AC",font=("cursive",20),width=5,height=2,fg="white",bg="orange",command= clears)
ac.grid(row=4,column=1,padx=7,pady=7)

zero=Button(button_frame,text=0,font=("cursive",20),width=5,height=2,fg="white",bg="red",command= lambda: btn_click(0))
zero.grid(row=4,column=2,padx=7,pady=7)

equal=Button(button_frame,text="=",font=("cursive",20),width=5,height=2,fg="white",bg="orange",command= res)
equal.grid(row=4,column=3,padx=7,pady=7)

divide=Button(button_frame,text="÷",font=("cursive",20),width=5,height=2,fg="black",bg="yellow",command= lambda:btn_click("/"))
divide.grid(row=1,column=4,padx=7,pady=7)

multiply=Button(button_frame,text="x",font=("cursive",20),width=5,height=2,fg="black",bg="yellow",command= lambda: btn_click("*"))
multiply.grid(row=2,column=4,padx=7,pady=7)

minus=Button(button_frame,text="-",font=("cursive",20),width=5,height=2,fg="black",bg="yellow",command= lambda: btn_click("-"))
minus.grid(row=3,column=4,padx=7,pady=7)

plus=Button(button_frame,text="+",font=("cursive",20),width=5,height=2,fg="black",bg="yellow",command= lambda: btn_click("+"))
plus.grid(row=4,column=4,padx=7,pady=7)

screen.mainloop()