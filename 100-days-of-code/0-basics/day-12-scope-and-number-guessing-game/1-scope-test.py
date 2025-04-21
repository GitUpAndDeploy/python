# enemies = 1

# def increase_enemies():
#   enemies = 4
#   print(f"Enemies inside function: {enemies}")

# increase_enemies()
# print(f"Enemies outside function: {enemies}")


enemies = 1
# # Bad method of using global variables
# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"Enemies inside function: {enemies}")
# increase_enemies()
# print(f"Enemies outside function: {enemies}")

# Preferred method of using global variables
def increase_enemies(enemies):
    print(f"Enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies(enemies)
print(f"Enemies outside function: {enemies}")
