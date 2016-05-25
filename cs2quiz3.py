#Section 1: Terminology

#POINTS- 1/1
# 1) What is a recursive function?
#It is a function that re-runs the fuction until the base case of the function is processed.
#
#

#POINTS- 1/1
# 2) What happens if there is no base case defined in a recursive function?
#the re-running of the function (by the recursive section) would not be stopped (continuously run through!)
#
#

#POINTS- 1/1
# 3) What is the first thing to consider when designing a recursive function?
#the base case
#
#

#pts- 1/1
# 4) How do we put data into a function call?
#using the parameters.
#
# 

#pts 1/1
# 5) How do we get data out of a function call?
#by returning
#
#


# 4
#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables a1-d3.

#a1 =2
#a2 =6
#a3 =-1

#b1 =2
#b2 =0
#b3 =1

#c1=    -2                                                                       
#c2 =4
#c3 =11

#d1 =-2
#d2 =1
#d3 =3



#
#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.


# +2 base case is present (MUST BE LABELED) -- 2
# +2 recursive case is present (MUST BE LABELED) --2
# +1 base case returns sum/ct (or equivalent) --1
# +2 recursive case filters even numbers --2
# +1 recursive case increments sum and ct correctly --0
# +1 recursive case returns correct recursive call --0
# +1 main function present AND called  --1
def avgofodds(number, total):
	n = raw_input("n: ")
	if n == "":	
		out = """The average of the odd numbers is {}""".format(total)
		print out		
	else:
		if not float(n) % 2:
			total += float(n)
			number += 1
			average = total / number
			adderofodds(average)
		else:
			adderofodds(average)
	


def main():
	adderofodds(0, 0)

main()
			 








