myName = "Bomin" #My first name
print myName #print my first name
myAgeInYears = 17.1 #My age in years
print myAgeInYears # print my age in years
myHeightInMeters = 1.6 #My height in meters
print myHeightInMeters #print my height in meters
sideOfSquareInMeters = 9 #One side of my square in meters
print sideOfSquareInMeters #print one side of my square in meters
lengthOfRectangleInMeters = 3 #The length of my rectangle in meters
heightOfRectangleInMeters = 2 #The height of my rectangle in meters
print lengthOfRectangleInMeters #print the length of my rectangle in meters
print heightOfRectangleInMeters #print the height of my rectangle in meters

monthsInYear = 12 #How many months there are in a year
myAgeInMonths = myAgeInYears * monthsInYear #compute my age in months
print myAgeInMonths #print my age in months (that's been computed previously)

myAgeOfDeath = 100 #How old I'm going to be when I die
yearsLeftToLive = myAgeOfDeath - myAgeInYears #compute how many years left for me to live
print yearsLeftToLive #print the years left for me to live (that's been computed previously)

feetInMeter = 3.28084 #How many feet in a meter
myHeightInFeet = myHeightInMeters * feetInMeter #compute my height in feet
print myHeightInFeet #print my height in feet (that's been computed previously)

averageHeightKoreaInMeters = 1.6 #average height of Korean 16-year old girls
differenceHeightWithAverage = averageHeightKoreaInMeters - myHeightInMeters #compute the difference between my height and the average height (of Korean 16-year old girls)
print differenceHeightWithAverage #print the difference between my height and the average one (it's been computed previously)

areaOfSquare = sideOfSquareInMeters ** 2 #compute area of my square
print areaOfSquare #print the area of my square (that's been computed previously)

volumeOfCube = sideOfSquareInMeters ** 3 #compute volume of my cube (with square sides)
halfTheVolumeCube = volumeOfCube / 2 #compute half of the volume of my cube (with square sides)
print halfTheVolumeCube #print half of the volume of my cube 

oneNinthOfArea = areaOfSquare / 9 #compute one ninth of the area of my square
print oneNinthOfArea #print one ninth of the area of my square

print "My name is ",myName,"."" I am ",myAgeInYears," years old."" I think I'll die when I am ",myAgeOfDeath," years old." " I have ",yearsLeftToLive," years left to live."" My height in meters is ",myHeightInMeters,"." #print a message using 5 of the variables I've created

print "My name is ",myName,". I am ",myAgeInYears," years old." " I think I'll die when I am ",myAgeOfDeath," years old." " I have ",yearsLeftToLive," years left to live." " My height in meters is ",myHeightInMeters,". In feet, my height is ",myHeightInFeet,". If one side of a square is " ,sideOfSquareInMeters, ", area of this square is ",areaOfSquare,". If it is not a square, and is a cube, then the volume is ",volumeOfCube," meters cubed." " Half of that volume would be ",halfTheVolumeCube," meters cubed." #print a second message using 10 of the variables I've created

winkingSmileyFaces = ";)" #winking smiley face as a string
tenthousandOfThem = ";)" * 10000 #compute 10000 of the winking smiley faces
print tenthousandOfThem
