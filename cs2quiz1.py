#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
# It is called the assignment operator, and it is used for defining a variable. We insert a value into the variable "bucket."
#
#
#2 3pts) Write a technical definition for 'function'
#Function is a named sequence of statements that performs a computation.
#
#
#3 1pt) What does the keyword "return" do?
#Return calls a function; it gives the output, as it processes with the given input.
#
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1: integer (1, 2)
#	2: float (1.2, 3.456566)
#	3: string ("Me" "You")
#	4: tuple ("Bomin", 5, 6.777)
#	5: boolean (True, False)
#
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
#Function definition is what we defined the function as, or, what we encoded the function in ways how the function runs. When we call a function, we are actually processing the function, requesting for an output with what we inserted as an input.
#
#
#
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1: Coding
#	2: Processing
#	3: Output
#
#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi

import math
def areaTOdiameter(x):
    return 2*(int(x)/math.pi)**1/2

def addDiameters(x,y,z):
    return x + y + z


def output(c1, c2, c3, added):
    out = """
Circle Diameter
c1 {}
c2 {} 
cs {}
TOTALS {}
""".format(c1, c2, c3, added)
    return out


def main():
    a= raw_input("Area of the 1st circle:")
    b= raw_input("Area of the 2nd circle:")
    c= raw_input("Area of the 3rd circle:")
    c1= areaTOdiameter(a)
    c2= areaTOdiameter(b)
    c3= areaTOdiameter(c)
    added= addDiameters(c1, c2, c3)
    out = output(c1, c2, c3, added)
    print out

main() 

