import art
import random
from game_data import data

# Get a random account
def get_random_account():
    """Get a random account from the data."""
    return random.choice(data)

# Format the data in the required format
def format_data(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}."

# Check if user's guess is correct
def check_answer(guess, a_follower_count, b_follower_count):
    """Check if the guess is correct."""
    if a_follower_count > b_follower_count:
        return guess == "a"
    else:
        return guess == "b"
    
# Main function to run the game
def game():
    print(art.logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()
    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()
        while account_a == account_b:
            account_b = get_random_account()
        print(f"Compare A: {format_data(account_a)}")
        print(art.vs)
        print(f"Against B: {format_data(account_b)}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}.")

if __name__ == "__main__":
    game()
