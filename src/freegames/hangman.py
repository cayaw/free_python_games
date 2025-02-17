# ASCII hangman
# submitting 2/17/25
# Caya Wilcox OSC Project

import random

def choose_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'developer', 'software']
    return random.choice(words)


def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def draw_hangman(attempts):
    stages = [
        "",
        "head",
        "body",
        "left arm",
        "right arm",
        "left leg",
        "right leg"
    ]
    print(f"Drawing: {stages[6 - attempts]}")
    if attempts == 6:
        print(f"  _________ \n"
              f"  |       | \n"
              f"  |      ( ) \n"
              f"  | \n"
              f"  | \n"
              f"  | \n"
              f"  | \n"
              f"  | \n"
              f"_____\n")
    elif attempts == 5:
        print(f"  _________ \n"
              f"  |       | \n"
              f"  |      ( ) \n"
              f"  | \n"
              f"  | \n"
              f"  | \n"
              f"  | \n"
              f"  | \n"
              f"_____ \n")
    elif attempts == 4:
        print(f"  _________ \n"
              f"  |       | \n"
              f"  |      ( ) \n"
              f"  |       | \n"
              f"  |       |\n"
              f"  | \n"
              f"  | \n"
              f"  | \n"
              f"_____\n")
    elif attempts == 3:
        print(f"  _________ \n"
              f"  |       | \n"
              f"  |      ( ) \n"
              f"  |     / |  \n"
              f"  |       | \n"
              f"  | \n"
              f"  | \n"
              f"  | \n"
              f"_____ \n")
    elif attempts == 2:
        print(f"  _________ \n"
              f"  |       | \n"
              f"  |      ( ) \n"
              f"  |     / | \\ \n"
              f"  |       | \n "
              f"  | \n"
              f"  | \n"
              f"  | \n"
              f"_____ \n")
    elif attempts == 1:
        print(f"  _________ \n"
              f"  |       | \n"
              f"  |      ( ) \n"
              f"  |     / | \\ \n"
              f"  |       | \n"
              f"  |      / \n "
              f"  | \n"
              f"  | \n"
              f"_____ \n")
    elif attempts == 0:
        print(f"  _________ \n"
              f"  |       | \n"
              f"  |      ( ) \n"
              f"  |     / | \\ \n"
              f"  |       | \n"
              f"  |      / \\ \n"
              f"  | \n"
              f"  | \n"
              f"_____ \n")

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")
            draw_hangman(attempts)

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            return

    print("\nGame over! The word was:", word)


if __name__ == "__main__":
    hangman()


