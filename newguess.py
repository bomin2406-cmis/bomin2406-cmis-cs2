import random

def rounds(roundno, pointsearned):
	if roundno == 0:
		out1 = """I got {} rounds correct.""".format(pointsearned)
		return out1
	else:
		out2 = """Round {}""".format(roundno)
		print out2
		pointsearned += eachguess(random.randint(1, 100), 5)
		return rounds(roundno -1, pointsearned)

def eachguess(randomized, trials):
	yourguess = int(raw_input("Guess a number:"))
	if yourguess == randomized:
		print "CORRECT\n"
		return 1
	elif trials == 1:
		print "You are not good at this game."
		return 0
	elif yourguess > randomized:
		print "TOO HIGH."
		return eachguess(randomized, trials -1)
	elif yourguess < randomized:
		print "TOO LOW."
		return eachguess(randomized, trials -1)



def main():
	print rounds(1, 0)

main()
