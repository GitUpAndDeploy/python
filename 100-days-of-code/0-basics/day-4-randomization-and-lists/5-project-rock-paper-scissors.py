# Rock, paper, scissors game
import random
# List of options
options = ["rock", "paper", "scissors"]
# Get user input
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
# Check if user input is valid
if user_choice not in options:
    print("Invalid choice. Please try again.")
else:
    # Generate computer choice
    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")
    # Determine winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")
# This code is a simple implementation of the Rock, Paper, Scissors game.
