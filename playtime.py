def countup(n):
	if n >= 10:
		print "BAB"
	else:
		print n
		countup(n+1)

def countup_up_from(start, stop):
	if start == stop:
		print "BAB"
	else:
		print start
		countup(start+1)

def main():
	countup_up_from(2, 15)
	return

main()
