from random import randint

dice_images = ["[1]", "[2]", "[3]", "[4]", "[5]", "[6]"]
dice_num = randint(1, 6)

# Incorrect code: Index is from 0 to 5 and not 1 to 6.
# print(dice_images[dice_num])

# Correct code
print(dice_images[dice_num - 1])
