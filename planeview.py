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

print "hello!"

#setup lights
scene = getSceneManager()
light1 = Light.create()
light1Color = Color("#ffffff")
light1.setColor(light1Color)
light1.setAmbient(light1Color)
light1.setEnabled(True)


#Constants
upperLeftEasting = 624030.0137255481		#Provided by jgw file
upperLeftNorthing = 1015207.0834458455		#Provided by jgw file
resWidth = 32064
resHeight = 30780
pixelSize = 0.18

#Create plane with specified width and height
plane = PlaneShape.create(100, 100) 

#Set the upper corner
plane.setPosition(Vector3(50, -50, -3))

#testing where corners are
upperCornerSphere = SphereShape.create(1.0, 3)
upperCornerSphere.setPosition(0,0,-3)

lowerCornerSphere = SphereShape.create(1.0, 3)
lowerCornerSphere.setPosition(100,-100,-3)


print "---map loaded..."

plane.setEffect("textured -d 50Island.png -v emissive")

#Calculate the bottom right UTM coordinates for our file
lowerRightEasting = (pixelSize * resWidth) + upperLeftEasting
lowerRightNorthing = upperLeftNorthing - (pixelSize * resHeight) 

#Calculate the total distances
totalDistanceX = lowerRightEasting - upperLeftEasting
totalDistanceY = lowerRightNorthing - upperLeftNorthing


print "---open file..."

#testing
f = open('test.csv')
csv_f = csv.reader(f)

i = csv_f.next()
rest = [row for row in csv_f]

fixedZ = -2

for i in rest:
	if(i[2] and i[3]):
		testLeftEasting = float(i[2])
		testLeftNorthing = float(i[3])
		sphere = SphereShape.create(1.0, 3)

		#Calculate the distance
		distanceX = testLeftEasting - upperLeftEasting
		distanceY = upperLeftNorthing - testLeftNorthing

		#Convert the distance into a ratio to be graphed
		adjustedX = (distanceX/totalDistanceX) * 100
		adjustedY = (distanceY/totalDistanceY) * 100

		#color by time
		time = i[4]
		timeTokens1 = time.split(" ")
		timeTokens2 = timeTokens1[1].split(":")
		print timeTokens2[0]
		
		timeCat = int(int(timeTokens2[0])/4)
		effectStr = "textured -v emissive -d %d.png" % timeCat #hack... 

		sphere.setPosition(Vector3(adjustedX, adjustedY, fixedZ))
		#sphere.setEffect("colored -d red -v emissive")
		sphere.setEffect(effectStr)
		print "creating sphere at ( %.5f, %.5f, %.5f )" % (adjustedX, adjustedY, fixedZ)



print "done"

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
