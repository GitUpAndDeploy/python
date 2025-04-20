print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age <= 12:
    print("Please pay $5.")
    bill = 5
  elif 12 < age <= 18:
    print("Please pay $7.")
    bill = 7
  elif 45 <= age <= 55:
    print("Everything will be okay, please enjoy the ride.")
  elif age > 18:
    print("Please pay $12.")
    bill = 12
  else:
    print("Invalid age. Please enter a valid age.")
    exit()
  # Nested if-else statement
  wants_photo = input("Do you want a photo taken? y or n ")
  if wants_photo == "y":
    print("Your photo costs an extra $3.")
    # Add $3 to the bill
    bill += 3

  print(f"Your final bill is ${bill}.")

else:
    print("Sorry, you have to grow taller before you can ride.")
