#Authors: Oliver San Juan, Jillian Aurisano

"""

This file is responsible for taking the utm and height information from the csv file and then converting it into
x, y, and z coordinates for omegalib. This file makes the assumption that the necessary information is found in the follwing
columns:

utm-easting 				(column 30)
utm-northing 				(column 31)
height_above_ellipsoid 		(column 34)

Furthermore, the program will get the name of the file that the user wants to write to on the command line. 

"""

from __future__ import print_function
import csv
import sys

def calculateXY (utmE, utmN):
    utmE1 = 624030.0137255481  #0.18/(float(10260)/32064) * 10260
    utmN1 = 1015207.0834458455 #.18/(float(9850)/30780) * 9850
    utmE2 = 629801.5337255481  #624030.0137255481 + 32064.0 * .18
    utmN2 = 1009666.6834458455 #1015207.0834458455 - 30780.0 * .18
    totalW = 5771.52
    totalH = 5540.4

    x = (utmE-utmE1)/(utmE2-utmE1) * totalW
    y = (utmN2-utmN)/(utmN2-utmN1) * totalH

    return (x, y)

#Constants for the desired column values
eastingColumn = 30
northingColumn = 31
heightColumn = 23

prevMin = -1
currMin = -1        #currMin will always store the minute value of every valid iteration
prevUtmE = -1
prevUtmN = -1
prevHeight = -1

#Get the name of the file that the user wants to write to from the command line
fileToWrite = sys.argv[1]

#Redirect standard output to write to that file
sys.stdout=open(fileToWrite, 'w')
	
f = open('allChibi.csv')

csv_f = csv.reader(f)
i = csv_f.next()
rest = [row for row in csv_f]

#print rest

for i in rest:
	#Strings have boolean values in python. Empty strings are evaluated to false. 
	#Parse lines that only have complete data
	if(i[eastingColumn] and i[northingColumn] and i[heightColumn]):
            
            string = i[34].split()
            string = string[1].split(":")

            #Get the current iteration's minute
            currMin = int(string[1])

            if(prevMin < 1):
                #assign prevMin to currMin because this is the first iteration
                prevMin = currMin

            elif(prevMin != currMin):

                #We are on a different burst and it's time to store it to the CSV
                xy = calculateXY(float(prevUtmE), float(prevUtmN))
                print("{}".format(xy[0]), end =",")
                print("{}".format(xy[1]), end =",")
                print("{}".format(prevHeight), end = "\n")

                #Move prevMin to currMin
                prevMin = currMin
            


            prevUtmE = i[eastingColumn]
            prevUtmN = i[northingColumn]
            prevHeight = i[heightColumn]
