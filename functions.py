def add(a, b): #compute the addition of a and b
	return a+b

def sub(a, b): #compute the difference between a and b
	return a-b 

def mul(a,b): #compute the multiplication of a and b
	return a*b

def div(a,b): #compute the division of a and b 
	return a/b 



def hours_from_seconds(a): #convert the hours into minutes
	return a/3600 


import math 

def circle_area(a): #compute the area of the circle with the given radius
	return math.pi * (a**2)

def sphere_volume(a):#compute the volume of the sphere with the given radius
	return 1.33333333333 * math.pi * (a**3) 

def avg_volume (a,b): #compute the average volume of the spheres
	c= a/2
	d= b/2
	y= sphere_volume(c)
	z= sphere_volume(d)
	return (y+z)/2


def area(a,b,c): #compute the area of the triangle
    s=(a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5


def right_align(a): #get the text on the right end of the screen
    return(80-len(a))*(" ") + a


def center(a): #get the text on the center of the screen
    return (40-len(a))*(" ") + a


def msg_box(a): #create a message box
    return "+" + ((len(a)+4)*"-") + "+" + "\n" + "|" + (2*" ") + (a)+ (2*" ") + "|" + "\n" + "+" + ((len(a)+4)*"-") + "+"



#Defining one additional variable for each of the functions I made

add1= add(1,2)
add2= add(2,3)
sub1= sub(6,5)
sub2= sub(10,9)
mul1= mul(1,2)
mul2= mul(2,3)
div1= div(6,2)
div2= div(4,2)
hours1= hours_from_seconds(18000)
hours2= hours_from_seconds(7200)
circle1= circle_area(3)
circle2= circle_area(4)
sphere1= sphere_volume(6)
sphere2= sphere_volume(7)
avg1= avg_volume (30,40)
avg2= avg_volume (50,60)
area1= area(3,4,5)
area2= area(6,8,10)
align1= right_align("Oink")
align2= right_align("Oink Oink")
center1= center("Stop")
center2= center("STTOOOPPPPP")
box1= msg_box("BRUNO SUCKS")
box2= msg_box("LALALALLALALALA")



print msg_box(str(add1))
print msg_box(str(add2))
print msg_box(str(sub1))
print msg_box(str(sub2))
print msg_box(str(mul1))
print msg_box(str(mul2))
print msg_box(str(div1))
print msg_box(str(div2))
print msg_box(str(hours1))
print msg_box(str(hours2))
print msg_box(str(circle1))
print msg_box(str(circle2))
print msg_box(str(sphere1))
print msg_box(str(sphere2))
print msg_box(str(avg1))
print msg_box(str(avg2))
print msg_box(str(area1))
print msg_box(str(area2))
print msg_box(str(align1))
print msg_box(str(align2))
print msg_box(str(center1))
print msg_box(str(center2))
print msg_box(str(box1))
print msg_box(str(box2))



