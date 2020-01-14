# Function for start
def start(user_number, random_number, crs, rs, s):
	if user_number == random_number:
		print("Yeah! You guessed.")
	else:
		if user_number > random_number:
			print("Oh no, but your number was more than conceived. " + "Next time you will definitely succeed.\n")

			print("For restart enter 'r', but if you want to exit enter 'q'")
			crs.create_restart(random_number, crs, rs, s)
		else:
			print("Oh no, but your number was less than conceived. " + "Next time you will definitely succeed.\n")

			print("For restart enter 'r', but if you want to exit enter 'q'")
			crs.create_restart(random_number, crs, rs, s)