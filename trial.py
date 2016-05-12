import random
def f():
	if random.random() > 0.5:
		result = True
	else:
		result = False
	return result

def main():
	f()
	if result:
		print "It's true"

main()
