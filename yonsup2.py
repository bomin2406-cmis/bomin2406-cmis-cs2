	
import random

#randomizing between 1 and 100
target = int(random.randint(1, 10))	


#round #
def countdown_round(roundnow):
	roundnow = roundnow - 1
	if roundnow == 0:
		print "You got " + str(points) + "of these right!!"
	else:
		print \n "Round " + str(roundnow)

	




def no_game():

#round #
	roundnow = 3
	countdown_round(roundnow)

#asks for the number
	no = int(raw_input("What is the number?:"))

#is it high or low
	if no > target:
		print "It's too high!"
		no_game()
	elif no < target:
		print "It's too low!"
		no_game()
	elif no == target:
		print "YOU GOT IT RIGHT MAN"

#points
	

def main():
	no_game()

main()
