from art import logo
# Blind auction program

# Step 1: Create a dictionary to store the bids
bids = {}
max_bid = 0

# Step 2: Create a function to add a bid to the dictionary
def add_bid(name, bid):
    bids[name] = bid

# Step 3: Create a function to find the highest bid
def highest_bidder(bids):
    max_bid = 0
    winner = ""
    for key in bids:
        if bids[key] > max_bid:
            max_bid = bids[key]
            winner = key
    print(f"The winner is {winner} with a bid of ${max_bid}")

print("Welcome to the secret auction program!")

# Step 4: Create a loop to get bids from users
while True:
    print(logo)
    print("Welcome to the secret auction program!")
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    add_bid(name, bid)
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if more_bidders == "no":
        print("\n" * 100)
        print(logo)
        highest_bidder(bids)
        break
    elif more_bidders == "yes":
        print("\n" * 100)
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
