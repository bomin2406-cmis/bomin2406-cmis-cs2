def add(a, b): #compute the addition of a and b
	return a+b

def sub(a, b): #compute the difference between a and b
	return a-b 

def mul(a,b): #compute the multiplication of a and b
	return a*b

def div(a,b): #creating formula so then the cpu can divide
	return a/b 

print add(3,4)
print sub(5,3)
print mul(4,4)
print div(2,3)

def hours_from_seconds(a): #convert the hours into minutes
	return a/3600 
print hours_from_seconds(86400)

import math 

def circle_area(a): #compute the area of the circle with the given radius
	return math.pi * (a**2)
print circle_area(5)

def sphere_volume(a):#compute the volume of the sphere with the given radius
	return 1.33333333333 * math.pi * (a**3) 

print sphere_volume(5)

def avg_volume (a,b): #compute the average volume of the spheres
	c= a/2
	d= b/2
	y= 1.3333333333333*math.pi*c*c*c
	z= 1.333333333333*math.pi*d*d*d
	return (y+z)/2
print avg_volume (10,20)

def area(a,b,c): #compute the area of the triangle
    s=(a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5
print area(1,2,2.5)

def right_align(a): #get the text on the right end of the screen
    return(80-len(a))*(" ") + a
print right_align("Hello")

def center(a): #get the text on the center of the screen
    return (40-len(a))*(" ") + a
print center("Hello")

def msg_box(a): #create a message box
    return "+" + ((len(a)+4)*"-") + "+" + "\n" + "|" + (2*" ") + (a)+ (2*" ") + "|" + "\n" + "+" + ((len(a)+4)*"-") + "+"
print msg_box("Hello!")
print msg_box("I eat cats!")




print add(3,4)
print sub(5,3)
print mul(4,4)
print div(2,3)
print hours_from_seconds(86400)
print circle_area(5)
print sphere_volume(5)
print avg_volume (10,20)
print area(1,2,2.5)
print right_align("Hello")
print center("Hello")
print msg_box("Hello!")
print msg_box("I eat cats!")

adding= add(3,4)
minus =sub(5,3)
times =mul(4,4)
dividing = div(2,3)
time = hours_from_seconds(86400)
circlearea = circle_area(5)
volumesphere= sphere_volume(5)
average= avg_volume (10,20)
area1= area(1,2,2.5)
right1= right_align("Hello")
center1= center("Hello")
y= msg_box("Hello!")
msg_box("I eat cats!")


thewholething = (adding, minus, times, dividing, time, circlearea, volumesphere, 


