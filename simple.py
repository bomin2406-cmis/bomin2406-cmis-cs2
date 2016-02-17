#Input
n= "Bomin"
x=3
y=4

#Processing
z= int(x) + int(y)

#Input
a=1
b=2

#Processing
c=int(1) * int(2)

#Input
z= "and that"


output = """
Hey {}!
Did you know:
{} + {} = {}
{}
{} * {} = {}
""". format(n, x, y, z, z, a, b, c)


print output


