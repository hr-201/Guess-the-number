## Guess the number v 1.1.2
import random

import start as s
import restart as rs 
import create_restart as crs

print("Hi! Let's play a game.\n I come up with a number, and you guess that number.\n")
print("I made a number from -2 to 50.\nPlease enter your number: ")

random_number = random.randrange(0, 50)

s.start(int(input()), random_number, crs, rs, s)