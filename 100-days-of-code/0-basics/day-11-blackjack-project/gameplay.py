from deck_of_cards import deal_card
from calculate_score import calculate_score
from compare_dealer_vs_player import compare
# Function to play a game of Blackjack
# The player and the computer are dealt two cards each
# The player can choose to hit (get another card) or stand (keep their current hand)
# The player can hit as many times as they want until they choose to stand or go over 21
# The computer must hit until their score is at least 17
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
def play_blackjack():
    """Plays a game of Blackjack."""
    player_hand = [deal_card(), deal_card()]
    computer_hand = [deal_card(), deal_card()]
    game_over = False
    while not game_over:
        player_score = calculate_score(player_hand)
        computer_score = calculate_score(computer_hand)
        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Computer's first card: {computer_hand[0]}")
        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
            if should_continue == "y":
                player_hand.append(deal_card())
            else:
                game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)
    print(f"   Your final hand: {player_hand}, final score: {player_score}")
    print(f"   Computer's final hand: {computer_hand}, final score: {computer_score}")
    print(compare(player_score, computer_score))
