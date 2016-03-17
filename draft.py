#the raw input (Asking for the guess)

import random

def randomize(first, second):
    return random.randint(first, second)

def differenceOfGuessAndTarget(g,t):
    return abs(g-t)

def main():
    miniNo = raw_input("What is the minimum number?:")
    maxiNo = raw_input("What is the maximum number?:")
    output = """I'm thinking of a number from {} to {}.""".format(miniNo, maxiNo)
    print output
    guess= raw_input("What do you think it is?:")

    target = randomize(int(miniNo), int(maxiNo))
    difference= abs(int(guess) - int(target))

    print output
    if int(guess) == target:
        msg = "YOU GOT IT!"
    if int(guess) > target:
        msg = ("You are over by ", abs(int(guess) - target)
    if int(guess) < int(target):
        msg = ("It's under by ", abs(int(guess) - target)

    output= """The target was {}.
Your guess was {}.
{}.
""".format(target, guess, msg)

main()


