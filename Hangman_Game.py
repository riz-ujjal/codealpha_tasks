#  Hangman Game

import random

def play_hangman():

    word_list = ["python", "algorithm", "variable", "developer", "keyboard"]

    secret_word = random.choice(word_list)

    guessed_letters = []
    attempts_left = 6

    display_word = ["_"] * len(secret_word)

    print("Welcome to Hangman!")
    print("Try to guess the secret word letter by letter.")

    while attempts_left > 0 and "_" in display_word:

        print("\n" + "=" * 30)
        print("Word to guess: " + " ".join(display_word))
        print(f"Attempts remaining: {attempts_left}")
        print("Letters guessed: " + ", ".join(guessed_letters))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")

        elif guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")

        elif guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
            guessed_letters.append(guess)

            for index in range(len(secret_word)):
                if secret_word[index] == guess:
                    display_word[index] = guess

        else:
            print(f"Sorry, '{guess}' is not in the word.")
            guessed_letters.append(guess)
            attempts_left -= 1

    print("\n" + "=" * 30)
    if "_" not in display_word:
        print(f"Congratulations! You guessed the word: '{secret_word}'!")
    else:
        print(f"Game Over! You ran out of attempts. The word was: '{secret_word}'.")

if __name__ == "__main__":
    play_hangman()