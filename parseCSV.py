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
for i in rest:
	count =0
	for j in rest:
		if(count in desiredColNum):
			print("{}".format(i[count]), end =",")
		count=count +1
	print("", end="\n")

