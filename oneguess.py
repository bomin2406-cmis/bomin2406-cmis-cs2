
def output(target, guess, ):
    out = """
The target was {}.
Your guess was {}.
That's under by {}.
""".format(name, x, y, z)
    return out


def main():
    miniNo= raw_input("What is the minimum number?:")
    maxiNo= raw_input("What is the maximum number?:")
main()


def output(miniNo, maxiNo):
    out = """
I'm thinking of a number from {} to {}.
""".format(miniNo, maxiNo)

def main():
    guess= raw_input("What do you think it is?:")
main()


import random

def randomize(first, second):
    return random.randint(first, second)

def differenceOfGuessAndTarget(g,t):
    return abs(g-t)

def output(target, guess):
    out = """
The target was {}.
Your guess was {}.
That's under by {}.
""".format(target, guess)

def main():
    target= randomize(miniNo, maxiNo)
    d= differenceOfGuessAndTarget(guess,target)
    out= output(target, guess, d)
    print out
main()




