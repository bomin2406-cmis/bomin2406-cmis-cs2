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
	out = guess
	print out

	target = randomize(int(miniNo), int(maxiNo))
	difference= differenceOfGuessAndTarget(int(guess),int(target))

	output= """The target was {}.
	Your guess was {}.
	That's under by {}.
	""".format(target, guess, difference)
main()

#the second part

def output(target, guess, d):
    out = """
The target was {}.
Your guess was {}.
That's under by {}.
""".format(target, guess, d)

def main():
    target= randomize(miniNo, maxiNo)
    d= differenceOfGuessAndTarget(guess,target)
    out= output(target, d)
    print out
main()
