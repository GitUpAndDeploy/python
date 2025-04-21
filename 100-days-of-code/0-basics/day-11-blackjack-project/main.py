from art import logo
from gameplay import play_blackjack

# Main game loop
# The player can choose to play a game of Blackjack or not
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print(logo)
    play_blackjack()
