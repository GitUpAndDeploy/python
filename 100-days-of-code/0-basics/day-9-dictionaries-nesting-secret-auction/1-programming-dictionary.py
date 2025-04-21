# Dictionaries are used to store data values in key:value pairs.

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}
# You can access the items in a dictionary by referring to its key name.
# print(programming_dictionary["Bug"])

# Looping through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])