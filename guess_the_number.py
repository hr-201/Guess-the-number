## Guess the number v 1.1.2
from random import randrange

print("Hi! Let's play a game.\n I come up with a number, and you guess that number.\n")
print("I made a number from 0 to 50.\nPlease enter your number: ")

user_number = int(input())

random_number = randrange(0, 50)

# Function for restart or quit in this program
def restart_or_quit():
	print("For restart enter 'r', but if you want to exit enter 'q'")

	restart_or_quit = input()

	if restart_or_quit == 'r':
		print("Please enter your number: ")
		user_number = int(input()) 

		start(user_number, random_number)

	# In this branch will exit the program
	elif restart_or_quit == 'q':
		exit()
	else:
		print("Command not recognized, enter it again.")

		restart_or_quit()

# Function for start this program
def start(user_number, random_number):
	if user_number == random_number:
			print("Yeah! You guessed.")
	# In this branch, the program restarts
	else:
		if user_number > random_number:
			print("Oh no, but your number was more than conceived. " + "Next time you will definitely succeed.\n")

			restart_or_quit()
		else:
			print("Oh no, but your number was less than conceived. " + "Next time you will definitely succeed.\n")

			restart_or_quit()

start(user_number, random_number)