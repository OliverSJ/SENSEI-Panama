#Authors: Ishta Bhagat and Oliver San Juan

"""
The csv files we are given have the following fields:

event-id,visible,timestamp,location-long,location-lat,
algorithm-marked-outlier,eobs:acceleration-axes,eobs:acceleration-sampling-frequency-per-axis,
eobs:accelerations-raw,eobs:activity,eobs:activity-samples,eobs:battery-voltage,eobs:fix-battery-voltage,
eobs:horizontal-accuracy-estimate,eobs:key-bin-checksum,eobs:speed-accuracy-estimate,eobs:start-timestamp,
eobs:status,eobs:temperature,eobs:type-of-fix,eobs:used-time-to-get-fix,ground-speed,heading,height-above-ellipsoid,
manually-marked-outlier,sensor-type,individual-taxon-canonical-name,tag-local-identifier,individual-local-identifier,
study-name,utm-easting,utm-northing,utm-zone,study-timezone,study-local-timestamp

We do not need all of these columns.  The only fields we need are:

tag-local-identifier 		(column 23) 
time, date 					(column 27)
utm-easting 				(column 30)
utm-northing 				(column 31)
height_above_ellipsoid 		(column 34)


"""

from __future__ import print_function
import csv
import sys

sys.stdout=open('test.csv', 'w')
	
f = open('Chibi_Christmas.csv')
	#with open("test.csv", "a") as myfile:
csv_f = csv.reader(f)
#for row in csv_f:
#	print(', '.join(row))
 # 	print row[24] + row[28] + row[31]+row[32]+row[35]
  		#myfile.write("appended text")
i = csv_f.next()
rest = [row for row in csv_f]
#print rest
desiredColNum = [23, 27, 30, 31, 34]

# for i in rest:
# 	count =0
# 	for j in rest:
# 		if(count in desiredColNum):
# 			print("{}".format(i[count]), end =",")
# 		count=count +1
# 	print("", end="\n")

for i in rest:
	if(i[23] and i[27] and i[30] and i[31] and i[34]):
		print("{}".format(i[23]), end =",")
		print("{}".format(i[27]), end =",")
		print("{}".format(i[30]), end =",")
		print("{}".format(i[31]), end =",")
		print("{}".format(i[34]), end =",")
		print("", end="\n")

