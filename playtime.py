def countup(n):
	if n >= 10:
		print "BAB"
	else:
		print n
		countup(n+1)

def countup_up_from(start, stop):
	if start >= stop:
		print "SHOOOOO"
	else:
		print start
		countup_up_from(start + 1, stop)
		
def countdown_from(start, stop):
	if start <= stop:
		print "BOOM"
	else:
		print start
		countdown_from(start -1, stop)


def main():
	countup_up_from(1, 20)
	countdown_from(20, 1)
main()





















def adder(number):
	return runningtotal + number


intro = "Running total : 0"
def output1(sumOfNos):
	out = """
The sum is {}.""".format(sumOfNos)

def output2(added):
	out = """
Next Number: {}
""".format(added)


def adder(number):
	print intro
	
	no = float(raw_input("Next number:"))
	if no == "":
		print output1
	else:
		added = adder(no)
		print output2



def main():
	print intro
	
	no = float(raw_input("Next number:"))
	if no == "":
		print output1
	else:
		added = adder(no)
		print output2

main()
		





