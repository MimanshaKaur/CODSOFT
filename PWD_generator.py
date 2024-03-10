from tkinter import *
import random

#creating screen
screen= Tk()
screen.title("Password Generator")
screen.geometry("550x300")

def password():
    pwd.delete(0,END)
    l=int(entry.get())
    x=''
    lower=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    digit=['0','1','2','3','4','5','6','7','8','9']
    symbol=['!','@','#','$','%','^','&','.',',','/','?','*','|','(',')','<','>','=','~','+','-',':',';']
    elements=lower+upper+digit+symbol
    for i in range(0,l):
        x=x+(random.choice(elements))
    pwd.insert(0,x)

lf=LabelFrame(screen,text="Enter the length of Password",font=("cursive",15))
lf.pack(pady=20)

entry=Entry(lf,font=("cursive",16),background="lightgray")
entry.pack(pady=20,padx=20)

pwd=Entry(screen,text='',font=("cursive",20),background="gray")
pwd.pack(padx=20,pady=20)

frame=Frame(screen)
frame.pack(pady=20)

gen_button=Button(frame,text="Generate Password",font=("cursive",12),background="red",command=password)
gen_button.pack(pady=0)
screen.mainloop()
