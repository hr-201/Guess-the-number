# Function for restart
def restart(restart_or_quit, random_number, crs, rs, s):
	if restart_or_quit == 'r':
		print("I made a new number from 0 to 50.\nPlease enter your number: ")
		s.start(int(input()), random_number, crs, rs, s)
	elif restart_or_quit == 'q':
		exit()
	else:
		print("Command not recognized, enter it again.")

		crs.create_restart(crs, rs, s)