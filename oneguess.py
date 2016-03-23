#the raw input (Asking for the guess)

import random

def randomize(first, second):
	return random.randint(first, second)

def differenceOfGuessAndTarget(g,t):
	return abs(g-t)

def main():
	miniNo = raw_input("What is the minimum number?:")
	maxiNo = raw_input("What is the maximum number?:")
	output = """I'm thinking of a number from {} to {}.""".format(miniNo, maxiNo)
	print output
	guess= raw_input("What do you think it is?:")

	target = randomize(int(miniNo), int(maxiNo))
	difference= abs(int(guess) - int(target))


	output= """The target was {}.
Your guess was {}.
""".format(target, guess)
	print output
	if int(guess) == target:
		print "YOU GOT IT!"
	elif int(guess) > target:
		print "You are over by ", str(abs(int(guess) - target))
	elif int(guess) < int(target):
		print "It's under by ", str(abs(int(guess) - target))


main()




