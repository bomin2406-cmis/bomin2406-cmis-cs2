import random



#1. introduction
def intro():
	name = raw_input("So. What's your name..?:")
	out = """There's someone here, at this hospital full of patients and doctors...tensed up. They are all staring at one thing, and it is, a bomb. The countdown has started: 1 minute remaining. There's no time to spare. That person in the middle is holding it - everything, EVERYTHING depends on that person. 
{}. That's you.""".format(name)
	print out



#3. first cut!!!
def cut1():
	print "You are looking at the bomb right now. There are three circuits attached on the bomb. Right? And, they are: red, blue, and green."

	cut1 = raw_input("Type the color of the circuit that you would like to cut, ALL IN LOWER CASE:")
	if cut1 == "red":
		cut1 = 1
		print cut1
		return cut1
	elif cut1 == "blue":
		cut1 = 2
		print cut1
		return cut1
	elif cut1 == "green":
		cut1 = 3
		print cut1
		return cut1


#4. dead or alive???!!!
def deadoralive(cut1, explosion):
	if cut1 == explosion:
		print "BOOM. YOU'RE DEAD."
	else:
		print "YAAASSSSS YOU ARE ALIVE. YAS YAS BUT BUT THE BOMB THOUGH. the timer's still running.....!"





def main():
	explosion = random.randint(1, 3)
	print explosion
	intro()
	examplevariablename = cut1()
	print examplevariablename
	deadoralive(examplevariablename, explosion)	

main()
