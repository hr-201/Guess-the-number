## Guess the number v 1.0
import random

random_number = random.randrange(0, 50)

print("Hi! Let's play a game.\n I come up with a number, and you guess that number.\n")
print("I made a number from 0 to 50.\nPlease enter your number: ")

user_number = int(input())

if user_number == random_number:
	print("Yeah! You guessed.")
else:
	print("Oh no, next time you will definitely succeed.")