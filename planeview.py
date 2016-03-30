#Authors: James Hwang, Oliver San Juan, and Ishta Bhagat 

"""

	A: 0.1800000000
	D: 0.0000000000
	B: 0.0000000000
	E: -0.1800000000
	C: 624030.0137255481 <--upper left easting
	F; 1015207.0834458455 <--- upper left northing


	627407.233983497,1012918.6367208124

"""

from omega import *
from cyclops import *
import utm

#Create plane with specified width and height
plane = PlaneShape.create(100, 100)

#Set the upper corner
plane.setPosition(Vector3(0, 0, -3))

plane.setEffect("textured -v emissive -d 50Island.png")


#Example code to color the monkeys' positions
# for i in range(0, 100):
# sphere = SphereShape.create(0.36, 3) #radius
# sphere.setPosition(Vector3(-1, 1.8, -2)) #x, y, z
# sphere.setEffect("colored -d red")


#Calculate the origin UTM to lat/long

#Convert the origin points to latitude and longitude
latlon = utm.to_latlon(624030.0137255481, 1015207.0834458455, 17, 'P')
latOrigin = latlon[0]
lonOrigin = latlon[1]


#First datapoint 
datapoint = utm.to_latlon(627427.8989302963,1013560.8472266255, 17, 'P')
latOne = datapoint[0]
lonOne = datapoint[1]

#Print it out
sphere = SphereShape.create(0.36, 3) #radius
sphere.setPosition(Vector3(lonOne-lonOrigin, latOne-latOrigin, 0)) #x, y, z
sphere.setEffect("colored -d red")

print latOne
print lonOne
print (lonOne-lonOrigin)
print (latOne-latOrigin)



#print latlon

#Use this as an example for seeing where the sphere will show up
# sphere = SphereShape.create(0.5, 3)
# sphere.setPosition(Vector3(-1, 1.8, -4))
# sphere.setEffect("colored -d blue")






