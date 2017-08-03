# Python 3

from random import choice

words = open('words.txt').read().split()
answer = choice(words)
letters = []
lives = 10
response = ""
playerwin = False
# print(answer)
while lives:
    reveal = []
    for letter in answer:
        if letter in letters:
            reveal.append(letter)
        else:
            reveal.append("-")
    if "".join(reveal) == answer:
        break
    print("\n\n########################################")
    print("\n" + response)
    print("You have", lives, "lives.")
    if letters:
        print("\nHere are the letters you've used:")
        print(", ".join(letters))
    else:
        print("\n\n")
    print("\n" + "".join(reveal))
    print("\n########################################\n")
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
if lives > 0:
    print("\n\n########################################\n\n\n")
    print("You win!\nThe answer was", answer + ".")
    print("\n\n\n\n########################################\n")
else:
    print("\n\n########################################\n\n\n")
    print("You lose.\nThe answer was", answer + ".")
    print("\n\n\n\n########################################\n")
