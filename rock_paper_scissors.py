import tkinter as tk
import random
from tkinter import messagebox

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry('350x350')

def user_choice(choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    result = determine_winner(choice, computer_choice)
    display_result(choice, computer_choice, result)

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or (user == 'scissors' and computer == 'paper') or (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def display_result(user, computer, result):
    user_label.config(text=f'You chose: {user}')
    computer_label.config(text=f'Computer chose: {computer}')
    result_label.config(text=result)
    if not messagebox.askyesno("Game over!", "Do you want to play again?"):
        root.destroy()

label1=tk.Label(root, text="INSTRUCTIONS:", font=0)
label2=tk.Label(root, text="Paper beats Rock.")
label3=tk.Label(root, text="Scissors beats paper.")
label4=tk.Label(root, text="Rock beats scissors.")
label5=tk.Label(root, text=" ")
label6=tk.Label(root, text=" ")


user_label = tk.Label(root, text='', font=14)
computer_label = tk.Label(root, text='', font=14)
result_label = tk.Label(root, text='', font=14)

label7=tk.Label(root, text="Please choose:", font=8)
rock_button = tk.Button(root, text="Rock", command=lambda: user_choice('rock'))
paper_button = tk.Button(root, text="Paper", command=lambda: user_choice('paper'))
scissors_button = tk.Button(root, text="Scissors", command=lambda: user_choice('scissors'))

label1.pack()
label2.pack()
label3.pack()
label4.pack()
label5.pack()

user_label.pack()
computer_label.pack()
result_label.pack()

label6.pack()
label7.pack()

rock_button.pack()
paper_button.pack()
scissors_button.pack()

root.mainloop()