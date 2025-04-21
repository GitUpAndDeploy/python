# Function to compare the scores of the player and the computer
# The player wins if their score is higher than the computer's score
# The player loses if their score is lower than the computer's score
# The player wins if the computer's score exceeds 21
# The player loses if their score exceeds 21
# The player wins if they have a Blackjack (21) and the computer does not
# The player loses if the computer has a Blackjack (21) and the player does not
# The player wins if they have a Blackjack (21) and the computer's score is 0
# The player loses if the computer has a Blackjack (21) and the player's score is 0
# The player wins if they have a Blackjack (21) and the computer's score is not 0
# The player loses if the computer has a Blackjack (21) and the player's score is not 0
def compare(player_score, computer_score):
    """Compares the scores of the player and the computer."""
    if player_score > 21 and computer_score > 21:
        return "You went over. You lose!"
    if player_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack!"
    elif player_score == 0:
        return "Win with a Blackjack!"
    elif player_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Opponent went over. You win!"
    elif player_score > computer_score:
        return "You win!"
    else:
        return "You lose!"
