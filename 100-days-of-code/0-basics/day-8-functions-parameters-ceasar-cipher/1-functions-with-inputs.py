# def greet():
#   print("Hello")
#   print("How are you John?")
#   print("Isn't it a beautiful day?")

# greet()


# def greet_with_name(name):
#   print(f"Hello {name}")
#   print(f"How are you {name}?")
#   print("Isn't it a beautiful day?")

# greet_with_name("John")


# Multiple inputs
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")

# Positional arguments
# greet_with("John", "London")

# Keyword arguments
greet_with(location="London", name="John")