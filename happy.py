def clapYourHands():
    print "clap clap"
def stompYourFeet():
    print "stomp stomp"
    
def main():
    happyOrNot = raw_input("Are you happy? (type either yes or no):") == "yes"
    knowItOrNot = raw_input("Do you know it though..? (type either yes or no:") == "yes"
    
    if happyOrNot and knowItOrNot:
        print "YAYYYYY"

main()

def main():
    happyOrNot = raw_input("Are you happy? (type either yes or no):") == "no"
    knowItOrNot = raw_input("Do you know it though..? (type either yes or no:") == "no"

    if happyOrNot or knowItOrNot:
        print "ew"
main()
