import random

#3. first cut!!!
def firstcut(explosion):
	print "You are looking at the bomb right now. There are three circuits attached on the bomb. Right? And, they are: red, blue, and green."

	cut1 = raw_input("Type the color of the circuit that you would like to cut:")
	if cut1 == "red":
		cut1 = 1
	elif cut1 == "blue":
		cut1 = 2
	elif cut1 == "green":
		cut1 = 3

	if cut1 > int(explosion) or cut1 < int(explosion) or cut1 == int(explosion):
		sureornot = raw_input("HA. You sure about that? (yes/no):")
		if sureornot == "yes" and sureornot == "no":
			cut1 = raw_input("NO YOU'RE NOT. OF COURSE YOU AREN'T SURE... Type the color again...:")

	if cut1 == "red":
		cut1 = 1
		return cut1
	elif cut1 == "blue":
		cut1 = 2
		return cut1
	elif cut1 == "green":
		cut1 = 3
		return cut1




def main():
	import random
	explosion = str(random.randint(1, 3))
	print explosion
	cut1 = firstcut(explosion)

main()
