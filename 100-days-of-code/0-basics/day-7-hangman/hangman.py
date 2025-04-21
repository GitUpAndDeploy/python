import random
from hangman_words import word_list
from hangman_art import stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
print("Welcome to Hangman!")
for i in range(word_length):
    print("_", end=" ")
print("\n")
display = []
for _ in range(word_length):
    display += "_"
print(display)
while "_" in display and lives > 0:
    print(f"You have {lives} lives left.")
    print(" ".join(display))
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print("You already guessed that letter.")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(stages[lives])
    print(display)
    if "_" not in display:
        print("You win!")
    else:
        print(f"You lose. The word was {chosen_word}.")