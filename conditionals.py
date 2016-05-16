import random


# RULES
#	conditional execution-1
def rules():
	print "HI! I MADE THIS GAME! AND I AM BOMIN!"
	rulesorno = raw_input("You wanna hear the rules? (yes/no):")
	if rulesorno == "yes" or rulesorno == "no":
		print "You have to know anyways, so yeah. You CANNOT write in capital letters. ALL of them should be LOWERCASED."

	


#introduction
#	conditional execution-2
def intro():
	name = raw_input("So. What's your name..?:")

	if name == "Innhye":
		print "GAME OVER"
		exit()

	out = """Clock is ticking. Patients, doctors, staffs,,,,they are all standing still, 
staring at one thing,,,, and it is, a bomb. The countdown has started: 30 seconds remaining... There's no time to spare. 
There's a person in the middle, at this hospital full of patients and doctors...tensed up. That person is holding it - everything, EVERYTHING depends on that person. 

{}. That's you.""".format(name)
	print out





#3. first cut!!!
def firstcut():
	print "You are looking at the bomb right now. There are three circuits attached on the bomb. Right? And, they are: red, blue, and green."

	cut1 = raw_input("Type the color of the circuit that you would like to cut:")
	if cut1 == "red":
		cut1 = 1
		return cut1
	elif cut1 == "blue":
		cut1 = 2
		return cut1
	elif cut1 == "green":
		cut1 = 3
		return cut1


	if cut1 >= int(explosion) or cut1 <= int(explosion):
		sureornot = raw_input:("HA. You sure about that? (yes/no):")
		if sureornot == "yes" and sureornot == "no":
			cut1 = raw_input:("NO YOU'RE NOT. OF COURSE YOU AREN'T SURE... Type the color again...:")

	
	




#4. dead or alive???!!!
#		alternative execution -1
def deadoralive1(cut1, explosion):
	if str(cut1) == explosion:
		print "BOOM. YOU'RE DEAD."
		exit()
	else:
		print "YAAASSSSS YOU ARE ALIVE. YAS YAS BUT BUT THE BOMB THOUGH. the timer's still running.....!"






#5. second cut!!!!!!!
def secondcut():
	print "\nNow you have two circuits left. One will stop the timer, and another one will make it explode...what's your choice?"

	cut2 = raw_input("Type the color of the circuit that you would like to cut, ALL IN LOWER CASE:")
	if cut2 == "red":
		cut2 = 1
		return cut2
	elif cut2 == "blue":
		cut2 = 2
		return cut2
	elif cut2 == "green":
		cut2 = 3
		return cut2






#6. deadoralive 2!!!!
#		alternative execution -2
def deadoralive2(cut2, explosion):
	if str(cut2) == explosion:
		print "BOOM. YOU'RE DEAD."
	else:
		print "The timer. is. stopped. YOU'RE ALIVE! EVERYONE IS ALIVE! GOOD JOB!!!"




                                                                                      

#main
def main():
	import random
	explosion = str(random.randint(1, 3))
	intro()
	cut1 = firstcut()
	deadoralive1(cut1, explosion)	
	cut2 = secondcut()
	deadoralive2(cut2, explosion)
main()
