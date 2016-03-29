def average(x, y):
	return (x + y)/2

def output(name, yourAge, yourMomsAge, avgOfNos):
	out = """
Heyya {}!
Did you know???
that {} + {} = {} ?!?!

So basically,
that's the average of your mom and your age!!!!
""". format(name, yourAge, yourMomsAge, avgOfNos)
	return out

def main():
	#INPUT!
	name= raw_input("What's your name?:")
	yourAge= raw_input("Ok. What's your age?:")
	yourMomsAge= raw_input("What about your mom's?:")

	#PROCESSING!
	avgOfNos= average(int(yourAge), int(yourMomsAge))

	#OUTPUT!!!!
	out = output(name, yourAge, yourMomsAge, avgOfNos)
	print out

main()


