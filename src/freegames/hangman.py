import turtle
import random
# import nltk

# from nltk.corpus import words

# from nltk.corpus import words

# nltk.download('words')

def choose_word():
    # word_list = [word for word in words.words() if len(word) < 10]
    # return random.choice(word_list).lower()
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
    print(f"Drawing: {stages[6 - attempts]}")  # put Turtle logic here

t = turtle.Turtle()
t.circle(50)
turtle.done()

def draw_text(text, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(text, align="center", font=("Arial", 20, "normal"))

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")
    # display this

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


