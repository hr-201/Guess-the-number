## Guess the number v 1.1.2
import random

random_number = random.randrange(0, 50)

# Function for start
def start(user_number):
	if user_number == random_number:
		print("Yeah! You guessed.")
	else:
		if user_number > random_number:
			print("Oh no, but your number was more than conceived. " + "Next time you will definitely succeed.\n")

			print("For restart enter 'r', but if you want to exit enter 'q'")
			create_restart()
		else:
			print("Oh no, but your number was less than conceived. " + "Next time you will definitely succeed.\n")

			print("For restart enter 'r', but if you want to exit enter 'q'")
			create_restart()
			
# Function for restart
def restart(restart_or_quit):
	if restart_or_quit == 'r':
		print("I made a new number from 0 to 50.\nPlease enter your number: ")
		start(int(input()))
	elif restart_or_quit == 'q':
		exit()
	else:
		print("Command not recognized, enter it again.")

		create_restart()

# Function for created restar in functions
def create_restart():
	restart_or_quit = input()
	restart(restart_or_quit)


print("Hi! Let's play a game.\n I come up with a number, and you guess that number.\n")
print("I made a number from 0 to 50.\nPlease enter your number: ")

start(int(input()))