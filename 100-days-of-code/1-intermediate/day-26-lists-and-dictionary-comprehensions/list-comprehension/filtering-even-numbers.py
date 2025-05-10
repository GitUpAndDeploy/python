list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# Convert to int
numbers = [int(item) for item in list_of_strings]
# Get evens
result = [number for number in numbers if  number % 2 == 0]
print(result)
