from tkinter import *

#creating screen
screen=Tk()
screen.title("Rock-Paper-Scissor Game")
screen.geometry("700x600")
screen.configure(background="black")

lf=LabelFrame(screen,text="ROCK-PAPER-SCISSOR",fg="white",bg="yellow")
lf.pack(pady=20)

screen.mainloop()