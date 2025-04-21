# This is a simple function that takes a first and last name as input and returns the formatted name in title case.
def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name.""" # Docstring
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

# Example usage of the function
print("Welcome to the name formatter!")
f_name = input("What is your first name? ")
l_name = input("What is your last name? ")
formatted_name = format_name(f_name, l_name)
print(f"Your name is {formatted_name}.")
