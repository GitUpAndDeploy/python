print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age <= 12:
    print("Please pay $5.")
    bill = 5
  elif age > 12 and age <= 18:
    print("Please pay $7.")
    bill = 7
  else:
    print("Please pay $12.")
    bill = 12
  # Nested if-else statement
  wants_photo = input("Do you want a photo taken? y or n ")
  if wants_photo == "y":
    print("Your photo costs an extra $3.")
    # Add $3 to the bill
    bill += 3

  print(f"Your final bill is ${bill}.")

else:
    print("Sorry, you have to grow taller before you can ride.")
