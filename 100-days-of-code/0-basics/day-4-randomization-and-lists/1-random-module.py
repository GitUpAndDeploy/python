import random

# Generate a random integer between 1 and 10
random_integer = random.randint(1, 10)
print(random_integer)

# Generate a random float between 0 and 1
random_float = random.random()
print(random_float)

# Generate a random float between 0 and 5
random_float_5 = random.uniform(0, 5)
print(random_float_5)

# Generate a random float between 0 and 1 and multiply by 100
random_float_100 = random.random() * 100
print(random_float_100)

# Generate a random float between 0 and 5 and multiply by 100
random_float_5_100 = random.uniform(0, 5) * 100
print(random_float_5_100)

# Generate a random float between 1 and 10 and multiply by 100
random_float_1_10_100 = random.uniform(1, 10) * 100

# Print heads or tails
random_choice = random.choice(["Heads", "Tails"])
print(random_choice)
