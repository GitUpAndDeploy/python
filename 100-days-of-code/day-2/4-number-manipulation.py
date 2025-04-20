bmi = 84 / 1.65 ** 2
print(bmi)


# Flooring: Remove all decimal places
print(int(bmi))

# Rounding: Round to the nearest integer
print("Rounding")
print(round(bmi))
print(round(bmi, 2))  # Round to 2 decimal places

# Assignment: Assign the value of bmi to a variable
print("Assignment")
score = 0
print(score)
# Increment score by 1
score += 1
print(score)
# Decrement score by 1
score -= 1
print(score)

# F string: Format the string with 2 decimal places
print("F-strings")
score = 0
height = 1.65
is_winning = True

print(f"Score: {score}, Height: {height}, Is Winning: {is_winning}")

# String formatting: Format the string with 2 decimal places
print("String formatting")
print("Score: %.2f, Height: %.2f, Is Winning: %s" % (score, height, is_winning))

# String formatting with f-string
print("String formatting with f-string")
print(f"Score: {score:.2f}, Height: {height:.2f}, Is Winning: {is_winning}")

# String formatting with format method
print("String formatting with format method")
print("Score: {}, Height: {}, Is Winning: {}".format(score, height, is_winning))



# Ceiling: Round up to the nearest integer
print("Ceiling")
import math
print(math.ceil(bmi))

# Floor division: Divide and remove decimal places
print(84 // 1.65 ** 2)

# Absolute value: Remove negative sign
print(abs(-84))

# Power: Raise to the power of 2
print(84 ** 2)

# Modulus: Remainder of division
print(84 % 2)

# Exponential: Raise to the power of 2
print(2 ** 2)

# Square root: Square root of 84
print(math.sqrt(84))

# Random number generation
import random
print(random.randint(1, 100))  # Random integer between 1 and 100

# Random float generation
print(random.uniform(1, 100))  # Random float between 1 and 100

# Random choice from a list
print(random.choice([1, 2, 3, 4, 5]))  # Random choice from a list

# Random sample from a list
print(random.sample([1, 2, 3, 4, 5], 3))  # Random sample of 3 elements from a list

# Random shuffle a list
data = [1, 2, 3, 4, 5]
random.shuffle(data)  # Shuffle the list in place
print(data)  # Print the shuffled list

# Random seed for reproducibility
random.seed(42)  # Set the seed for reproducibility
