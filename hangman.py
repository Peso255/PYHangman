import os
from random import choice

WORDFILE = 'words.txt'
MAXLIVES = 10
BARRIER = '########################################'

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

words = open(WORDFILE).read().split()
answer = choice(words)
letters = []
lives = MAXLIVES
response = ""
while lives:
    reveal = []
    for letter in answer:
        if letter in letters:
            reveal.append(letter)
        else:
            reveal.append("-")
    if "".join(reveal) == answer:
        break
    cls()
    print("\n\n{}".format(BARRIER))
    print("\n{}".format(response))
    print("You have {} lives.".format(lives))
    if letters:
        print("\nHere are the letters you've used:")
        print(", ".join(letters))
    else:
        print("\n\n")
    print("\n" + "".join(reveal))
    print("\n{}\n".format(BARRIER))
    guess = input("What is your guess? ")
    if not (len(guess) == 1 and guess.isalpha() and guess.islower()):
        response = "Guess must be one lowercase letter."
    elif guess in letters:
        response = "You've already guessed that."
    elif guess in answer:
        response = "Correct!"
        letters.append(guess)
        reveal.append(guess)
    else:
        response = "Sorry, your guess isn't in the word."
        lives -= 1
        letters.append(guess)
cls()
if lives > 0:
    response = "win!"
else:
    response = "lose."
print("\n\n{}\n\n\n".format(BARRIER))
print("You {}\nThe answer was {}.".format(response, answer))
print("\n\n\n\n{}\n".format(BARRIER))
