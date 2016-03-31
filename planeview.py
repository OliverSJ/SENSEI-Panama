#Authors: James Hwang, Oliver San Juan, and Ishta Bhagat

"""
	The information for the
	A: 0.1800000000
	D: 0.0000000000
	B: 0.0000000000
	E: -0.1800000000
	C: 624030.0137255481 	<--upper left easting
	F; 1015207.0834458455 	<--- upper left northing

	To find the ratio:
		d/totald * 100

	Dimension of the picture:
		32064 x 30780

"""

from omega import *
from cyclops import *
import csv

#Constants
upperLeftEasting = 624030.0137255481		#Provided by jgw file
upperLeftNorthing = 1015207.0834458455		#Provided by jgw file
resWidth = 32064
resHeight = 30780
pixelSize = 0.18

#Create plane with specified width and height
plane = PlaneShape.create(100, 100)

#Set the upper corner
plane.setPosition(Vector3(0, 0, -3))

plane.setEffect("textured -v emissive -d 50Island.png")

#Calculate the bottom right UTM coordinates for our file
lowerRightEasting = (pixelSize * resWidth) + upperLeftEasting
lowerRightNorthing = (pixelSize * resHeight) + upperLeftEasting

#Calculate the total distances
totalDistanceX = lowerRightEasting - upperLeftEasting
totalDistanceY = lowerRightNorthing - upperLeftNorthing

#testing
f = open('test.csv')
csv_f = csv.reader(f)

i = csv_f.next()
rest = [row for row in csv_f]

for i in rest:
	count =0
	#Grab each row
	for j in rest:
		testLeftEasting = float(j[2])
		testLeftNorthing = float(j[3])
		sphere = SphereShape.create(0.36, 3)

		#Calculate the distance
		distanceX = upperLeftEasting - testLeftEasting
		distanceY = upperLeftNorthing- testLeftNorthing

		#Convert the distance into a ratio to be graphed
		adjustedX = (distanceX/totalDistanceX) * 100
		adjustedY = (distanceY/totalDistanceY) * 100

		sphere.setPosition(Vector3(adjustedX, adjustedY, 0))
		sphere.setEffect("colored -d red")

# testLeftEasting = 627407.233983497
# testLeftNorthing = 1012918.6367208124

# sphere = SphereShape.create(0.36, 3)

# #Calculate the distance
# distanceX = upperLeftEasting - testLeftEasting
# distanceY = upperLeftNorthing- testLeftNorthing

# #Convert the distance into a ratio to be graphed
# adjustedX = (distanceX/totalDistanceX) * 100
# adjustedY = (distanceY/totalDistanceY) * 100

# sphere.setPosition(Vector3(adjustedX, adjustedY, 0))
# sphere.setEffect("colored -d red")


#Example code to color the monkeys' positions
# for i in range(0, 100):
# sphere = SphereShape.create(0.36, 3) #radius
# sphere.setPosition(Vector3(-1, 1.8, -2)) #x, y, z
# sphere.setEffect("colored -d red")

#print latlon

#Use this as an example for seeing where the sphere will show up
# sphere = SphereShape.create(0.5, 3)
# sphere.setPosition(Vector3(-1, 1.8, -4))
# sphere.setEffect("colored -d blue")
