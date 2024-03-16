from tkinter import *
import random
import time
#creating screen
screen=Tk()
screen.title("Rock-Paper-Scissor Game")
screen.geometry("800x650")
screen.resizable(0,0)
screen.configure(background="#bde0fe")

def user_choice(item):
    global ctr
    while(ctr==0):
        global choice
        choice=item
        input_choice.set(choice)
        choice=""
        global ch
        l=["ROCK","PAPER","SCISSOR"]
        ch=random.choice(l)
        global comp_ch
        comp_ch.set(ch)
        ch=""
        count="0"
        tie=0
        user_win=0
        comp_win=0
        i=input_choice.get()
        c=comp_ch.get()
        while(count=="0"):
            output.delete(0,END)
            if((i=="ROCK" and c=="ROCK") or (i=="PAPER" and c=="PAPER") or (i=="SCISSOR" and c=="SCISSOR")):
                res="TIE"
            if((i=="ROCK" and c=="SCISSOR") or (i=="PAPER" and c=="ROCK") or (i=="SCISSOR" and c=="PAPER")):
                res="USER WINS"
            if((c=="ROCK" and i=="SCISSOR") or (c=="PAPER" and i=="ROCK") or (c=="SCISSOR" and i=="PAPER")):
                res="COMPUTER WINS"
            output.insert(0,res)
            res=""
            count=count+"1"
        ctr=ctr+1
    choice=""
    ch=""
def replay():
    global ctr
    ctr=0
    choice=""
    ch=""
    input_choice.set(choice)
    comp_ch.set(ch)
    output.delete(0,END)

def close():
    screen.quit()

choice=""
ch=""
ctr=0
input_choice=StringVar()
comp_ch=StringVar()
lf=Label(screen,text="ROCK-PAPER-SCISSOR",font=("cursive",15,"bold"),bg="#219ebc",fg="#fff",width="30")
lf.pack(pady=20)

f0=Frame(screen,bg="#bde0fe")
f0.pack(pady=20)

f1=Frame(f0,width="250",height=150,bg="#a2d2ff")
f1.grid(row=1,column=1, padx=20)

f11=Label(f1,text="USER's CHOICE: \n Please Make Your Selection",font=("cursive",11,"bold"),bg="#e35053",fg="#fff",width="25")
f11.pack(padx=10,pady=10)

f12=Button(f1,text="ROCK",font=("cursive",12,"bold"),bg="#ff337e",fg="black",width="20",command=lambda: user_choice("ROCK"))
f12.pack(padx=20,pady=10)

f13=Button(f1,text="PAPER",font=("cursive",12,"bold"),bg="#ff337e",fg="black",width="20",command=lambda: user_choice("PAPER"))
f13.pack(padx=20,pady=10)

f14=Button(f1,text="SCISSOR",font=("cursive",12,"bold"),bg="#ff337e",fg="black",width="20",command=lambda: user_choice("SCISSOR"))
f14.pack(padx=20,pady=10)

entry1=Entry(f1,textvariable=input_choice,font=("cursive",16,"bold"),background="black",fg="#fff",justify=CENTER)
entry1.pack(padx=20,pady=10)

f2=Label(f0,text="V/S",font=("cursive",15,"bold"),bg="#a2d2ff",fg="#fff",width="5")
f2.grid(row=1,column=2,padx=20)

f3=Frame(f0,width="250",bg="#a2d2ff",height="250")
f3.grid(row=1,column=3,padx=20)

f31=Label(f3,text="COMPUTER's CHOICE\n",font=("cursive",14,"bold"),bg="#e35053",fg="#fff",width="22")
f31.pack(padx=10,pady=10)

f32=Label(f3,text="ROCK",font=("cursive",14,"bold"),bg="#ff337e",fg="black",width="20")
f32.pack(padx=20,pady=10)

f33=Label(f3,text="PAPER",font=("cursive",14,"bold"),bg="#ff337e",fg="black",width="20")
f33.pack(padx=20,pady=10)

f34=Label(f3,text="SCISSOR",font=("cursive",14,"bold"),bg="#ff337e",fg="black",width="20")
f34.pack(padx=20,pady=10)

entry2=Entry(f3,textvariable=comp_ch,font=("cursive",16,"bold"),background="black",fg="#fff",justify=CENTER)
entry2.pack(padx=20,pady=10)

lf2=LabelFrame(screen,text="RESULT",font=("cursive",16,"bold"),width="300",background="#bde0fe")
lf2.pack(padx=50)

output=Entry(lf2,textvariable=' ',font=("cursive",16,"bold"),background="#219ebc",fg="black",justify=CENTER)
output.pack(pady=5,padx=50)

frame4=Frame(screen,bg="#a2d2ff")
frame4.pack(pady=20)

replay_btn=Button(frame4,text="REPLAY GAME",font=("cursive",16,"bold"),width="35",background="#219ebc",fg="#fff",command=replay)
replay_btn.grid(row=1,padx=20,pady=8)

close_btn=Button(frame4,text="CLOSE GAME",font=("cursive",16,"bold"),width="25",background="#219ebc",fg="#fff",command=close)
close_btn.grid(row=2,padx=20,pady=10)
screen.mainloop()