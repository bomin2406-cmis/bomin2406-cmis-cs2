#ADDER
def adder(no, runningtotal):
    if no == "":
        return runningtotal

    else:
        runningtotal = float(no) + runningtotal
        no = raw_input("Running total: " + str(runningtotal) + "\nNext number: ")
        return adder(no, runningtotal)

def main():
    out = adder(0, 0)
    print "The sum is " + str(out)
main()




#BIGGEST

def biggest(BIG):
#Here, previousno is basically the biggest number you typed UNTIL NOW.
	no = raw_input("Next number:")
	if no == "":
		return BIG

	else:
		if no >= BIG:
			BIG = no
			print biggest(BIG)
		elif no < BIG:
			print biggest(BIG)
	
		

biggest(-float('Inf'))
	








