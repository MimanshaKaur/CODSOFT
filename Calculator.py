from tkinter import *

#creating screen
screen=Tk()
screen.title("CALCULATOR")
screen.geometry("450x550")
screen.configure(background="black")

def number():
    n=9
    return n

#creating calculator
input_text=StringVar()

lf=LabelFrame(screen)
lf.pack(pady=20)

result=Entry(lf,text='',font=("cursive",20),background="darkgray")
result.pack(pady=20,padx=20)

button_frame=Frame(screen,width=350,height=380,bg="red")
button_frame.pack()

button9=Button(lf,text=9,fg="white",bg="black",command= number)







'''choice=0
while(choice==0):
    a=int(input("Enter First Number: "))
    b=int(input("Enter Second Number: "))
    print("<-----CHOOSE THE OPERATOR TO PERFORM FOLLOWING OPERATIONS----->")
    print("(+) ---> FOR ADDITION")
    print("(-) ---> FOR SUBTRACTION")
    print("(*) ---> FOR MULTIPLICATION")
    print("(/) ---> FOR DIVISION")
    o=input("ENTER THE OPERATOR :")
    if(o=='+'):
        print("RESULT= ",a+b)
    elif(o=='-'):
        print("RESULT= ",a-b)
    elif(o=='*'):
        print("RESULT= ",a*b)
    elif(o=='/'):
        print("RESULT= ",a/b)
    else:
        print("INVALID CHOICE !!!")
    print("Do You Want To Continue?")
    c=input("Enter YES/NO : ")
    if(c=="YES" or c=="yes"):
        choice=0
    else:
        choice=1'''
screen.mainloop()