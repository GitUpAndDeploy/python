# file = open("../writing-to-files/data.txt") # File path relative to the pwd

# print(file.read())

# file.close()

# Alternative approach, automatically closes the file
with open("../writing-to-files/data.txt") as file:
  print(file.read())

# # Wite to a file in append mode
# with open("../writing-to-files/data.txt", mode="a") as file:
#   file.write("\nHello again")

