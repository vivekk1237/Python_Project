from flask import Flask,render_template,url_for,redirect
import speech_recognition as sr
import pyttsx3
import datetime
from tkinter import *
import tkinter.font as font
import random

app=Flask(__name__,template_folder='template')



@app.route("/")
def home():
    return render_template('home.html')


@app.route("/voiceerror")
def speech():
    initial()
    while True:
            
        r=sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            wishMe()
            speak("ok I am ready You can Speak now")
            audio = r.listen(source,phrase_time_limit=4)

        try:
            MyText=r.recognize_google(audio,language='en-in')
            string=str(MyText)
            if(string.count("login")>0):
                speak("ok got it")
                return redirect(url_for("login"))
            elif(string.count("learn")>0):
                speak("ok got it")
                return redirect(url_for("learn"))
            elif(string.count("play")>0):
                speak("ok got it")
                return redirect(url_for("play"))
            elif(string.count("why")>0):
                speak("ok got it")
                return redirect(url_for("why"))
            elif(string.count("about")>0):
                speak("ok got it")
                return redirect(url_for("about"))
            elif(string.count("home")>0):
                speak("ok got it")
                return redirect(url_for("home"))
            else:
                tell="I can't find any matching content"
                speak(tell)
                flash("I can't find any matching content")
                return render_template('home.html')
                
                

        except Exception as e:
            speak(e)
            flash("Some Error Occurred")
            return render_template('home.html')

def initial():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  
    return engine
def speak(audio):
    engine=initial()
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")  
  
    else:
        speak("Good Evening Sir !") 


@app.route("/play")
def play():
    return render_template('play.html')

@app.route("/learn")
def learn():
    return render_template('learn.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/why")
def why():
    return render_template('why.html')

@app.route("/login")
def login():
    return render_template('login.html')
     
@app.route("/rps")
def rps():
    global player_score, computer_score
    root = Tk()
    root.title("Rock Paper Scissors Game")
    app_font = font.Font(size = 12)
    root.config(bg = '#FFE873')
    root.geometry('700x300')

    player_score = 0
    computer_score = 0
    options = [('rock', 0), ('paper', 1), ('scissors', 2)]

    #Displaying Game Title
    Label(text = 'Simple Game', font = font.Font(size = 20), bg = '#FFE873').pack()
    Label(text = 'Rock Paper Scissors', font = font.Font(size = 20), bg = '#FFE873').pack()



    # define function to choice player input
    def player_choice(player_input):
        global player_score, computer_score

        computer_input = get_computer_choice()

        player_choice_label.config(text = 'Your Selected : ' + player_input[0])
        computer_choice_label.config(text = 'Computer Selected : ' + computer_input[0])

        if player_input == computer_input:
            winner_label.config(text = "Tie")
        elif (player_input[1]-computer_input[1]) % 3 == 1:
            player_score += 1
            winner_label.config(text="You Won!!!")
            player_score_label.config(text = 'Your Score : ' + str(player_score))
        else:
            computer_score += 1
            winner_label.config(text="Computer Won!!!")
            computer_score_label.config(text='Your Score : ' + str(computer_score))

    #Function to Randomly Select Computer Choice
    def get_computer_choice():
        return random.choice(options)


    #Label to display, who wins each time
    winner_label = Label(text = "Let's Start the Game...", fg = 'green', bg = '#FFE873', font = font.Font(size = 13), pady = 8)
    winner_label.pack()

    input_frame = Frame(root, bg = '#FFE873')
    input_frame.pack()

    #Displaying player options
    player_options = Label(input_frame, text = "Your Options : ", font = app_font, fg = 'grey', bg = '#FFE873')
    player_options.grid(row = 0, column = 0, pady = 8)

    rock_btn = Button(input_frame, text = 'Rock', width = 15, bd = 0, bg = 'pink', pady = 5, command = lambda: player_choice(options[0]))
    rock_btn.grid(row = 1, column = 1, padx = 8, pady = 5)

    paper_btn = Button(input_frame, text = 'Paper', width = 15, bd = 0, bg = 'silver', pady = 5, command = lambda: player_choice(options[1]))
    paper_btn.grid(row = 1, column = 2, padx = 8, pady = 5)

    scissors_btn = Button(input_frame, text = 'Scissors', width = 15, bd = 0, bg = 'light blue', pady = 5, command = lambda: player_choice(options[2]))
    scissors_btn.grid(row = 1, column = 3, padx = 8, pady = 5)

    #Displaying Score and players choise
    score_label = Label(input_frame, text = 'Score : ', font = app_font, fg = 'grey', bg = '#FFE873')
    score_label.grid(row = 2, column = 0)

    player_choice_label = Label(input_frame, text = 'Your Selected : ---', font = app_font, bg = '#FFE873')
    player_choice_label.grid(row = 3, column = 1, pady = 5)

    player_score_label = Label(input_frame, text = 'Your Score : 0', font = app_font, bg = '#FFE873')
    player_score_label.grid(row = 3, column = 2, pady = 5)

    computer_choice_label = Label(input_frame, text = 'Computer Selected : ---', font = app_font, fg = 'black', bg = '#FFE873')
    computer_choice_label.grid(row = 4, column = 1, pady = 5)

    computer_score_label = Label(input_frame, text = 'Computer Score : 0', font = app_font, fg = 'black', bg = '#FFE873')
    computer_score_label.grid(row = 4, column = 2, padx = (10,0), pady = 5)

    root.mainloop()
    return redirect(url_for("play"))

if __name__=='__main__':
    app.run(debug=True)