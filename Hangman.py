import random

words = ["python", "hangman", "coding", "laptop", "keyboard"]

chosen_word = random.choice(words)

display = ["_"] * len(chosen_word)

wrong_guesses = 0
max_wrong_guesses = 6
guessed_letters = []

print(" Welcome to Hangman! 🎮")

while wrong_guesses < max_wrong_guesses and "_" in display:
    print("\nWord:", " ".join(display))
    print("Wrong guesses left:", max_wrong_guesses - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
        print("Correct! ✅️")
    else:
        wrong_guesses += 1
        print(" Wrong! ❌️")

if "_" not in display:
    print("\n🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("\n💀 Game Over!")
    print("The word was:", chosen_word)
