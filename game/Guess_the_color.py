from tkinter import *
import random
from tkinter import messagebox

def guessTheColor():
    colors = ["Red","Blue","Green","Purple","Brown","Black","Cyan","Pink"]
    global score
    score = 0
    global timeremaining
    timeremaining=30

    def startGame(event):  #function to start the game
        if timeremaining == 30:
            countdown()

        nextcolor()   #function to change color

    def countdown(): #initialising countdown function
        global timeremaining
        if timeremaining == 0:
            messagebox.showinfo("Time Remaining","Time is over and Your Score is "+str(score))
            root.after(1000,root.destroy())
            



        if timeremaining > 0:
            timeremaining -= 1

            timeLabel.config(text = "Time Remaining :" +str(timeremaining)) 
            timeLabel.after(1000,countdown)

    def nextcolor():
        global score
        global timeremaining  #making the variables global to access them from anywhere
        if timeremaining >0 :
            e.focus_set()
            if e.get().lower() == colors[1].lower():
                score += 1
            e.delete(0,END)
            random.shuffle(colors)

            label.config(fg = str(colors[1]),text = str(colors[0]))
            scoreLabel.config(text = "score :"+str(score))

    root = Tk()
    root.title("Guess the Game")
    root.geometry("800x650")
    root.resizable(0,0)

    instructions = Label(root,text = "Guess the color of words,and not the word text !",font = ('Monotype Corosive',24))
    instructions.pack()

    scoreLabel = Label(root,text = "Press Enter to Start",font = ('Monotype Corosiva',24))
    scoreLabel.pack()

    timeLabel = Label(root,text = "Time Remaining :" +str(timeremaining),font = ('Monotype Corosiva',24))
    timeLabel.pack()

    label = Label(root,font = ('Monotype Corosiva',60))
    label.pack()

    e = Entry(root)
    root.bind('<Return>',startGame)
    e.pack()
    e.focus_set()

    root.mainloop()