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














def adder(stuff, total):
    if stuff == "":
        return total
    else:
        total += float(stuff) 
        stuff = raw_input("Running total: " + str(total) + "\nNext number: ")
        return adder(stuff, total)

def main():
    out = adder(0, 0)
    print "The sum is " + str(out)
main()





def adder2(total):
	total = 0
	print "Running total " + str(number)
	innum = raw_input("Next number: ")
	if innum == '':
		print "Running total " + str(innum)
	else:
		total += float(innum)
		adder2(total)



def adder(no, runningtotal):

	if no == "":
		print "Running total " + str(runningtotal)
		exit()
	else:
		runningtotal += float(no)
		print "Running total " + str(runningtotal)
		no = raw_input("Next number: ")
		

def main():
#	adder(0, 0)
	adder2(0)
main()


