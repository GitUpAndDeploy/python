guests = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]
# This program randomly selects a guest to pay the bill from a list of guests.
# Importing the random module to use its functions
import random

# Method 1: Using random.choice() to select a random guest
# Randomly select a guest from the list of guests
random_guest = random.choice(guests)
# Print the selected guest
print(random_guest)

# Method 2: Using random.randint() to select a random index
# Randomly select an index from the list of guests
# Print the guest at the randomly selected index
print(guests[random.randint(0, len(guests) - 1)])

# Method 3: Using random.sample() to select a random sample
# Randomly select a sample of 1 guest from the list of guests
random_sample = random.sample(guests, 1)
# Print the guest in the random sample
print(random_sample[0])

# Method 4: Using random.shuffle() to shuffle the list and select the first guest
# Shuffle the list of guests
random.shuffle(guests)
# Print the first guest in the shuffled list
print(guests[0])

# Method 5: Using random.choices() to select a guest with replacement
# Randomly select a guest from the list of guests with replacement
random_choice = random.choices(guests, k=1)
# Print the guest in the random choice
print(random_choice[0])
