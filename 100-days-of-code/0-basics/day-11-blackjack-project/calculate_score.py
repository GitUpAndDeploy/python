# Function to calculate the score of a hand
# Aces are worth 11 or 1, face cards are worth 10, and all other cards are worth their number
# The score of a hand is the sum of the values of its cards
# If the score exceeds 21, the hand is worth 0
# If the hand contains an Ace, it is worth 1 if the score exceeds 21
# If the hand contains an Ace and the score does not exceed 21, it is worth 11
# If the hand contains no Aces, it is worth 0 if the score exceeds 21
# If the hand contains no Aces and the score does not exceed 21, it is worth the score
def calculate_score(hand):
    """Calculates the score of a hand."""
    score = 0
    for card in hand:
        if card[0] in ["J", "Q", "K"]:
            score += 10
        elif card[0] == "A":
            if score + 11 > 21:
                score += 1
            else:
                score += 11
        else:
            score += int(card[0])
    return score
