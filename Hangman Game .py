import random

# List of predefined words
words = ["python", "computer", "hangman", "program", "keyboard"]

# Randomly choose a word
word = random.choice(words)

# Create empty display with underscores
guessed_word = ["_"] * len(word)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
attempts = 6

print("Welcome to Hangman!")

# Game loop
while attempts > 0 and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Guessed letters:", guessed_letters)
    print("Remaining attempts:", attempts)

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    # Add guess to listmhl
    guessed_letters.append(guess)

    # Check if guess is correctky ky
    if guess in word:
        print("Correct!")

        # Reveal the letter in the word imp
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong guess!")
        attempts -= 1

# Final resultllrgle
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)

