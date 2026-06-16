import random

# List of 5 predefined words
words = ["python", "hangman", "coding", "laptop", "keyboard"]

# Select a random word
chosen_word = random.choice(words)

# Create hidden word display
display = ["_"] * len(chosen_word)

wrong_guesses = 0
max_wrong_guesses = 6
guessed_letters = []

print(" Welcome to Hangman! 🎮")

while wrong_guesses < max_wrong_guesses and "_" in display:
    print("\nWord:", " ".join(display))
    print("Wrong guesses left:", max_wrong_guesses - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check if letter exists in word
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
        print("Correct! ✅️")
    else:
        wrong_guesses += 1
        print(" Wrong! ❌️")

# Game result
if "_" not in display:
    print("\n🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("\n💀 Game Over!")
    print("The word was:", chosen_word)

