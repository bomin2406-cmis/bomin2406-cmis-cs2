myName = "Bomin"
print myName 
myAgeInYears = 17.1
print myAgeInYears
myHeightInMeters = 1.6
print myHeightInMeters
sideOfSquareInMeters = 9
print sideOfSquareInMeters
lengthOfRectangleInMeters = 3
heightOfRectangleInMeters = 2
print lengthOfRectangleInMeters
print heightOfRectangleInMeters

monthsInYear = 12
myAgeInMonths = myAgeInYears * monthsInYear
print myAgeInMonths 

myAgeOfDeath = 100
yearsLeftToLive = myAgeOfDeath - myAgeInYears
print yearsLeftToLive

feetInMeter = 3.28084
myHeightInFeet = myHeightInMeters * feetInMeter
print myHeightInFeet

averageHeightKoreaInMeters = 1.6
differenceHeightWithAverage = averageHeightKoreaInMeters - myHeightInMeters 
print differenceHeightWithAverage 

areaOfSquare = sideOfSquareInMeters ** 2
print areaOfSquare

volumeOfCube = sideOfSquareInMeters ** 3
halfTheVolumeCube = volumeOfCube / 2
print halfTheVolumeCube

oneNinthOfArea = areaOfSquare / 9
print oneNinthOfArea

print "My name is" + " " + str(myName) + "." " " "I am" + " " + str(myAgeInYears) + " " + "years old." " " + "I think I'll die when I am" + " " + str(myAgeOfDeath) + "." " " "I have" + " " + str(yearsLeftToLive) + " " + "years left to live." " " "My height in meters is" + " " + str(myHeightInMeters) + "."

print "My name is" + " " + str(myName) + "." " " "I am" + " " + str(myAgeInYears) + " " + "years old." " " + "I think I'll die when I am" + " " + str(myAgeOfDeath) + "." " " "I have" + " " + str(yearsLeftToLive) + " " + "years left to live." " " "My height in meters is" + " " + str(myHeightInMeters) + "." "In feet, my height is" " " + str(myHeightInFeet) + "." "If one side of a square is " + str(sideOfSquareInMeters) + "," "area of this square is " + str(areaOfSquare) + "." "If it is not a square, and is a cube, then the volume is " + str(volumeOfCube) + "units squared." " " "Half of that volume would be " + str(halfTheVolumeCube) + "."
