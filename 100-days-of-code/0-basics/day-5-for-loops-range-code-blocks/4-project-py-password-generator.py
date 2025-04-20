print("Welcome to the PyPassword Generator!")
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
  ]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# Password Components
print("How many letters would you like in your password?")
nr_letters = int(input("Enter number of letters: "))
print("How many symbols would you like?")
nr_symbols = int(input("Enter number of symbols: "))
print("How many numbers would you like?")
nr_numbers = int(input("Enter number of numbers: "))
# Password Generation
password_list = []
# Randomly select letters
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))
# Randomly select symbols
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
# Randomly select numbers
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))
# Shuffle the password list
random.shuffle(password_list)
# Join the password list into a string
password = ""
for char in password_list:
    password += char
# Print the password
print(f"Your password is: {password}")

