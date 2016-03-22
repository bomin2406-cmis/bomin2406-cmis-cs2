def add(x, y):
	return x + y

def output(name, firstNo, secondNo, sumOfNos):
	out = """
Heyya {}!
Did you know???
that {} + {} = {} ?!?!
""". format(name, firstNo, secondNo, sumOfNos)
	return out

def main():
	#INPUT!
	name= raw_input("What's your name?:")
	firstNo= raw_input("Type a number:")
	secondNo= raw_input("Type another one:")

	#PROCESSING!
	sumOfNos= add(int(firstNo), int(secondNo))

	#OUTPUT!!!!
	out = output(name, firstNo, secondNo, sumOfNos)
	print out

main()


