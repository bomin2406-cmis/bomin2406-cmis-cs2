import random


#running the set for 3 times
#adding up the points you got
def rounds(roundno, pointsearned):
	if roundno == 0:
		out1 = """You got {} round/rounds correct!""".format(pointsearned)
		return out1
	else:
		out2 = """Round {}!""".format(roundno)
		print out2
		pointsearned += eachguess(random.randint(1, 100), 5)
		return rounds(roundno -1, pointsearned)


#within each sets, asking for a guess five times
#too high or too low
#correct or incorrect at the 5th guess
def eachguess(randomized, trials):
	yourguess = int(raw_input("Guess a number:"))
	if yourguess == randomized:
		print "CORRECT~\n"
		return 1
	elif trials == 1:
		print "EW YOU SUCK.\n"
		return 0
	elif yourguess > randomized:
		print "TOO HIGH."
		return eachguess(randomized, trials -1)
	elif yourguess < randomized:
		print "TOO LOW."
		return eachguess(randomized, trials -1)



def main(): 
	print rounds(3, 0)

main()
