import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.geometry("400x200")

        # Set font sizes
        title_font = ("Times New Roman", 16, "bold")
        button_font = ("Calibri", 12)

        # Set colors
        bg_color = "white"
        button_color = "blue"
        text_color = "black"

        # Configure window background color
        self.master.configure(bg=bg_color)

        # Create and configure widgets
        self.label = tk.Label(self.master, text="Press the button to start the game:", font=title_font, fg=text_color, bg=bg_color)
        self.label.pack()

        self.start_button = tk.Button(self.master, text="Start Game", command=self.start_game, font=button_font, fg=text_color, bg=button_color)
        self.start_button.pack()

    def start_game(self):
        # Set font sizes
        button_font = ("Calibri", 12)

        # Set colors
        bg_color = "white"
        button_color = "blue"
        text_color = "black"

        # Reset the game state
        self.secret_number = random.randint(0, 9)
        self.chances = 3

        self.label.config(text=f'You have {self.chances} chances. Good luck!')
        self.start_button.config(state=tk.DISABLED)

        self.entry_label = tk.Label(self.master, text="Enter any number between 0 and 9:", font=button_font, fg=text_color, bg=bg_color)
        self.entry_label.pack()

        self.entry = tk.Entry(self.master)
        self.entry.pack()

        self.guess_button = tk.Button(self.master, text="Make a Guess", command=self.make_guess, font=button_font, fg=text_color, bg=button_color)
        self.guess_button.pack()

    def make_guess(self):
        user_guess = self.entry.get()

        if user_guess.isdigit():
            user_guess = int(user_guess)

            if user_guess == self.secret_number:
                messagebox.showinfo("Congratulations!", "You guessed it right!")
                self.reset_game()
            else:
                self.chances -= 1
                if self.chances == 0:
                    messagebox.showinfo("Game Over", f"You've run out of chances. The correct number was {self.secret_number}.")
                    self.reset_game()
                else:
                    messagebox.showwarning("Wrong Guess", f"Wrong guess. You have {self.chances} chances left.")
                    self.label.config(text=f'You have {self.chances} chances left. Try again!')
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid number between 0 and 9.")

    def reset_game(self):
        self.label.config(text="Press the button to start the game:")
        self.start_button.config(state=tk.NORMAL)

        if hasattr(self, 'entry_label'):
            self.entry_label.destroy()
            self.entry.destroy()
            self.guess_button.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()






