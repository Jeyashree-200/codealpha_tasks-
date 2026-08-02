import random

# List of words
words = ["python", "apple", "computer", "coding", "school"]

# Randomly choose a word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum wrong attempts
attempts = 6

print("=" * 40)
print("      WELCOME TO HANGMAN")
print("=" * 40)

while attempts > 0:

    display = ""

    # Display guessed letters and underscores
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check if word is completed
    if "_" not in display:
        print("\nCongratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Enter only one alphabet.")
        continue

    # Already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct Guess!")
    else:
        attempts -= 1
        print("Wrong Guess!")
        print("Remaining Attempts:", attempts)

else:
    print("\n💀 Game Over!")
    print("The word was:", word)
