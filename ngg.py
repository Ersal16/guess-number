import random
import sys
import os
import datetime

argv = sys.argv
playing = True
os.system('clear -x')

def settings():
	min = input("minimum: (default 0): ")
	if not min.isdigit():
		min = 0
	else:
		min = int(min)

	max = input("\nmaximum: (default 10): ")
	sys.stdout.write("\033[K")
	if not max.isdigit():
		max = 10
	else:
		max = int(max)
	
	if min>max:
		print("\nsince the minimum is bigger than the maximum they got switched")
		min, max = max, min

	mode = input("\ndifficulty? [easy / normal] (default normal): ")
	mode.lower()
	if not mode == "easy" and not mode == "normal":
		print("\ninvalid value, set to normal")

	return min, max, mode


def main():
	guessed = False
	min, max, mode = settings()
	n = random.randint(min, max)
	while not guessed:
		guess = input(f"\nguess the number! ({min} < {max}): ")
		os.system('clear -x')
		if not guess.isdigit():
			print("only numbers.")
		else:
			guess = int(guess)
			if guess == n:
				guessed = True
				print("\nCORRECT ANSWER !")
			else:
				print("\nnope lol")
				if guess < n:
					print("\nn is bigger than your guess")
				else:
					print("\nn is lower than your guess")

	status = input("\ndo you want to play? again? [1 = yes/0 = no]: ")
	if not status or status == '0':
		global playing
		playing = False
		print('byeeeeeeeee \n\n')


while playing:
	main()
