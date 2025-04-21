try:
  age = int(input("Enter your age: "))
except ValueError:
  print("Invalid input. Please enter a number(integer).")
  age = int(input("Enter your age: "))

if age < 0:
  raise ValueError("Age cannot be negative")
elif age < 18:
  print(f"You can drive at age {age}")
else:
  print("You can drive.")
