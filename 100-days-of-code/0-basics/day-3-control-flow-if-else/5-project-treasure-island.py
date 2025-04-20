# Treasure Island Game
# This is a simple text-based adventure game where the player has to make choices to find treasure.
# The player will be presented with a series of choices, and based on their choices, they will either win or lose the game.
# The game is structured as a series of nested if-else statements, where each choice leads to a different outcome.
# The game starts with a welcome message and a brief description of the mission.
# The player is prompted to make a choice at each step, and their input is processed to determine the next step.
# The game ends with a message indicating whether the player has won or lost.
print("Welcome to the treasure island.")
print("Your mission is to find the treasure.")
# Take the first input
first_choice = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'.\n").lower()

if first_choice == "left":
    # Take the second input
    second_choice = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()

    if second_choice == "wait":
        # Take the third input
        third_choice = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()

        if third_choice == "red":
            print("It's a room full of fire. Game Over.")
        elif third_choice == "yellow":
            print("You found the treasure! You Win!")
        elif third_choice == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
