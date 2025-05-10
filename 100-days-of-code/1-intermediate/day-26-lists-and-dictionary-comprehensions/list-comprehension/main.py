# numbers = [1, 2, 3]
# new_numbers = [number+1 for number in numbers]

# print(new_numbers)

# ####
# name = "Abhishek"
# new_list = [letter for letter in name]

# print(new_list)


# range_list = [number*2 for number in range(1,5)]
# print(range_list)

# Conditional list comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# short_names = [item for item in names if len(item) < 5]
# print(short_names)

upper_names = [ item.upper() for item in names if len(item) > 5]
print(upper_names)
