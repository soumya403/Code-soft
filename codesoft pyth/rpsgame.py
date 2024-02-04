import tkinter as tk
from tkinter import messagebox
import random

# Game choices
CHOICES = ["Rock", "Paper", "Scissors"]

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        self.root.geometry("600x400")  # Set window size

        # Set background color
        self.root.configure(bg='#f0f0f0')

        self.player_a_choice = None
        self.player_b_choice = None

        # Label for title
        title_label = tk.Label(root, text="Rock-Paper-Scissors Game", font=("Arial", 18, "bold"), bg='#f0f0f0')
        title_label.pack(pady=10)

        # Entry widget for player's choice
        self.choice_entry = tk.Entry(root, font=("Arial", 14))
        self.choice_entry.pack(pady=10)

        # Play button with some styling
        self.play_button = tk.Button(root, text="Play", command=self.play_game, font=("Arial", 14), bg='#4CAF50', fg='white')
        self.play_button.pack(pady=10)

        # Label for displaying result
        self.result_Label = tk.Label(root, text="", font=("Arial", 14), bg='#f0f0f0')
        self.result_Label.pack(pady=10)

        # Reset button with some styling
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_game, font=("Arial", 14), bg='#f44336', fg='white')
        self.reset_button.pack(pady=10)

    def play_game(self):
        player_a_choice = self.choice_entry.get().capitalize()
        if player_a_choice not in CHOICES:
            messagebox.showwarning("Invalid Choice", "Please enter Rock, Paper, or Scissors.")
            return

        self.player_a_choice = player_a_choice
        self.player_b_choice = random.choice(CHOICES)
        result_text = f"Player A: {self.player_a_choice}\nPlayer B: {self.player_b_choice}\n"
        result_text += self.get_game_result()
        self.result_Label.config(text=result_text)

    def get_game_result(self):
        if self.player_a_choice == self.player_b_choice:
            return "It's a tie!"
        elif (
            (self.player_a_choice == "Rock" and self.player_b_choice == "Scissors")
            or (self.player_a_choice == "Paper" and self.player_b_choice == "Rock")
            or (self.player_a_choice == "Scissors" and self.player_b_choice == "Paper")
        ):
            return "Player A wins!"
        else:
            return "Player B wins!"

    def reset_game(self):
        self.choice_entry.delete(0, tk.END)
        self.result_Label.config(text="")
        self.player_a_choice = None
        self.player_b_choice = None

# Create the game window
root = tk.Tk()

# Start the game
game = RockPaperScissorsGame(root)

# Run the game loop
root.mainloop()
