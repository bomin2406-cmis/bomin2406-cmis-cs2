

import random


def guess_the_no():
#round #
	roundno = 3
	points = 0


	print "Round number " + str(roundno)

#randomizing between 1 and 100
	target = random.randint(1, 100)
	
#asks for the number
	no = int(raw_input("What is the number?:"))

#is it high or low
	if no > target:
		print "It's too high!"
	elif no < target:
		print "It's too low!"
	elif no == target:
		return "YOU GOT IT RIGHT MAN"
		points = points + 1



#how many points u have
	print "You got " + str(points) + "of these right!!"
	 
