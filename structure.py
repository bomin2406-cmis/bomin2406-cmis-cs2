def add(x,y):
    return 1.2 * ((x+y)/2)

def output(name, x, y, z):
    out = """
Hello sir!
So,,, your name is {}?
You know, 
if you eat {} fried chicken legs and {} bags of candies,
you would suffer {} years with health issues?
Yup. Be wise.
""".format(name, x, y, z)
    return out


def main():
    name= raw_input("What's your name?:")
    x= raw_input("Type a BIG number:")
    y= raw_input("Type a BIGGER number:")
    z= add(int(x), int(y))
    out = output(name, x, y, z)
    print out

main() 


    

