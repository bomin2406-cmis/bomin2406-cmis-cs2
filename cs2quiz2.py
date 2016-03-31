#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a) 2 == 2 (This is TRUE)
#b) 2 == 3 (This is FALSE)
#c) 2 > 3 (This is FALSE)
#
#2) What does 'return' do?
#Return prints the output out.
#
#
#
#3) What are 2 ways indentation is important in python code?
#a)To end a function
#b)To make the commands PART of the function. (for instance, if you don't indent for a return command, that return command will not be part of the function)
#
#

#PART 2: Reading
#Type the values for 12 of the 16 of the variables below.
#
#problem1_a)36
#problem1_b) sq.root of 3
#problem1_c) 0
#problem1_d) -5
#
#problem2_a)TRUE
#problem2_b)FALSE
#problem2_c)FALSE
#problem2_d)FALSE
#
#problem3_a)0.3
#problem3_b)0.5
#problem3_c)0.5
#problem3_d)0.5
#
#problem4_a)7
#problem4_b)5
#problem4_c)0.125
#problem4_d)5
#

#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)

def main():
	#INPUT
	print "Type in 3 different numbers (decimals are okay!)"
	no1 = raw_input("A:")
	no2 = raw_input("B:")
	no3 = raw_input("C:")

	#PROCESSING
	if float(no1) > float(no2) > float(no3) or float(no1) > float(no3) > float(no2):
		out = """The largest number was {}!""".format(no1)
		print out
	elif float(no2) > float(no1) > float(no3) or float(no2) > float(no3) > float(no1):
		out = """The largest number was {}!""".format(no2)
		print out
	elif float(no3) > float(no1) > float(no2) or float(no3) > float(no2) > float(no1):
		out = """The largest number was {}!""".format(no3)
		print out

	elif no1 == no2 or no1 == no3 or no1 == no2 == no3:
		print "You did not follow the directions!!!!"
	elif no2 == no1 or no2 == no3 or no1 == no2 == no3:
		print "You did not follow the directions!!!!"
	elif no3 == no1 or no3 == no2 or no1 == no2 == no3:
		print "You did not follow the directions!!!!"

#OUTPUT
main()
