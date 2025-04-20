# This is a simple tip calculator program that calculates the total bill amount
# including the tip and splits it among a given number of people.
# The program prompts the user for the total bill amount, the tip percentage,
# and the number of people to split the bill. It then calculates the tip amount,
# the total bill with tip, and the amount each person should pay. The final
# amount is formatted to 2 decimal places for better readability.

print("Welcome to the tip calculator!")
# Get the total bill amount from the user
total_bill = float(input("What was the total bill? $"))
# Check if the total bill is valid
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
# Check if the tip percentage is valid
people = int(input("How many people to split the bill? "))
# Calculate the tip amount
tip = total_bill * tip_percentage / 100
# Calculate the total bill with tip
total_bill_with_tip = total_bill + tip
bill_per_person = total_bill_with_tip / people
# Format the bill per person to 2 decimal places
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_amount}")
