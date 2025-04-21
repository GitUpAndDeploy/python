import random
# Create a deck of cards

def create_deck():
    """Creates a deck of cards."""
    # Cards and suits
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    deck = []
    for suit in suits:
        for card in cards:
            deck.append(card + " of " + suit)
    return deck

# Function to deal a card
def deal_card():
    """Returns a random card from the deck."""
    return random.choice(create_deck())
