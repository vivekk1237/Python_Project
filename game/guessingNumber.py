import tkinter as tk
from tkinter import messagebox as tkMessageBox
import random
 
def guessing():
	# Create a new window
	window = tk.Tk()
	
	# Set the dimensions of the created window
	window.geometry("600x400")
	
	# Set the background color of the window
	window.config(bg="#065569")
	
	window.resizable(width=False,height=False)
	
	# Set Window Title
	window.title('Number Guessing Game')

	
	# The code for the buttons and text and other 
	# interactive UI elements go here 
	global TARGET, RETRIES,score
	
	TARGET = random.randint(0, 100)
	RETRIES = 0
	score=0
	
	

	def ask_quit():
		global score
		if tkMessageBox.askokcancel("Quit", "You want to quit now?"):
			window.after(1000,window.destroy())
		else:
			new_game()
	
	def update_result(text):
		result.configure(text=text)
	
	# Create a new game
	def new_game():
		guess_button.config(state='normal')
		global TARGET, RETRIES
		TARGET = random.randint(0, 100)
		RETRIES = 0
		update_result(text="Guess a number between\n 0 and 100")
	
	# Continue the ongoing game or end it
	def play_game():
		global RETRIES,score
	
		choice = int(number_form.get())

		if RETRIES<=10:
		
			if choice != TARGET:
				RETRIES += 1
			
				result = "Wrong Guess!! Try Again"
				if TARGET < choice:
					hint = "The required number is less than {}".format(choice)
				else:
					hint = "The required number lies between {} and 100".format(choice)
				result += "\n\nHINT :\n" + hint
			
			else:
				result = "You guessed the correct number after {} retries".format(RETRIES)
				score+=1
				guess_button.configure(state='disabled')
				result += "\n" + "Click on Play to start a new game"

		else:
			result = "You take more than 10 retries"
			guess_button.configure(state='disabled')
			result += "\n" + "Click on Play to start a new game"
		
		update_result(result)
	
	# Heading of our game
	title = tk.Label(window,text="Guessing Game",font=("Arial",24),fg="#fffcbd",bg="#065569")
	
	# Result and hints of our game
	result = tk.Label(window, text="Click on Play to start a new game", font=("Arial", 12, "normal", "italic"),fg = "White", bg="#065569", justify=tk.LEFT)
	
	# Play Button
	play_button = tk.Button(window, text="Play Game", font=("Arial", 14, "bold"), fg = "Black", bg="#29c70a", command=new_game)
	
	# Guess Button
	guess_button = tk.Button(window,text="Guess",font=("Arial",13), state='disabled', fg="#13d675",bg="Black", command=play_game)
	
	# Exit Button
	exit_button = tk.Button(window,text="Exit Game",font=("Arial",14), fg="White", bg="#b82741", command=ask_quit)
	
	
	# Entry Fields
	guessed_number = tk.StringVar()
	number_form = tk.Entry(window,font=("Arial",11),textvariable=guessed_number)
	
	
	# Place the labels
	
	title.place(x=170, y=50)
	result.place(x=180, y=210)
	
	# Place the buttons
	exit_button.place(x=300,y=320)
	guess_button.place(x=350, y=147) 
	play_button.place(x=170, y=320)
	
	# Place the entry field
	number_form.place(x=180, y=150)

	
	
	# Start the window
	window.mainloop()