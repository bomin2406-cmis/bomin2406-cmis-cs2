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
def biggest(no, BIG):
	if no >= BIG:
		BIG = no
		no = raw_input("Next number:")
		print biggest(no, BIG)
	elif no == "":
		return BIG
biggest(no, BIG)

		
def main():
	biggest(0, 0)
	print "The biggest number is " + str(BIG)
main()












