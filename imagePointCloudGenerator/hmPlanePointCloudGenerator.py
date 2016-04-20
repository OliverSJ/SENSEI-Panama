import Image;
import png;
import struct;

#computed using img
def computeIMGUTMtoHMXY (imgx, imgy):
    #Images UTM Coordinates
    startIMGUTMX = 624030.0137255481
    startIMGUTMY = 1015207.0834458455

    #Height Maps UTM Coordinates
    startHMUTMX = 624079.8465020715
    lastHMUTMX = 629752.8465020715
    startHMUTMY = 1015157.5668793379
    lastHMUTMY = 1009715.5668793379

    imgResRatioX = 0.18/(float(10260)/32064)
    imgResRatioY = 0.18/(float(9850)/30780)

    utmX = startIMGUTMX + (imgx*imgResRatioX)
    utmY = startIMGUTMY - (imgy*imgResRatioY)

    hmx = int(((utmX-startHMUTMX)/(lastHMUTMX-startHMUTMX) * 5673))
    hmy = int(((utmY-startHMUTMY)/(lastHMUTMY-startHMUTMY) * 5442))
    return (hmx, hmy)
    
    
imgResRatioX = 0.18/(float(10260)/32064)            #calculation for how far pixels are apart in
                                                    #meters
imgResRatioY = 0.18/(float(9850)/30780)             #calculation for how far pixels are apart in
                                                    #meters
filename = "hmColorHigh.xyzb"                       #output filename
hm = "heightMap.png"                                #height map filename
pic = "32Island.png"                                #picture filename
hmImage = Image.open(hm)                            #open the height map
hmImage = hmImage.transpose(Image.FLIP_TOP_BOTTOM)
picImage = Image.open(pic)                          #open the picture
picImage = picImage.transpose(Image.FLIP_TOP_BOTTOM)
hmPixInfo = hmImage.load()                          #loads pixel data of height map
picPixInfo = picImage.load()                        #loads pixel data of picture
(hi,_) = hmImage.size                               #gives x-size
(_,hj) = hmImage.size                               #gives y-size
(i,_) = picImage.size                               #gives x of image
(_,j) = picImage.size                               #gives y of image
f = open(filename, 'wb')                            #opens the output file and gives option
                                                    #write in binary
for x in range(i):                                  #iterate through all pixels in reverse
    for y in range(j):
        utmXY = computeIMGUTMtoHMXY(x, y)
        hmX = utmXY[0]
        hmY = utmXY[1]
        if (hmX >= 0 and hmX < 5673 and hmY >= 0 and hmY < 5442):
            if hmPixInfo[hmX, hmY] != 0:
                z = 0.6*float(hmPixInfo[hmX, hmY])  #z will remain 0 for now
                                                    #later we will get it from
                                                    #terrain map
                r = float(picPixInfo[x, y][0])      #r value from tuple
                r = r/255.0
                g = float(picPixInfo[x, y][1])      #g value from tuple
                g = g/255.0
                b = float(picPixInfo[x, y][2])      #b value from tuple
                b = b/255.0
                #a = float(pixInfo[x, y][3])        #a value from tuple
                #a = a/255.0
                a = 1.0
                dataBytes = struct.pack('ddddddd', imgResRatioX*x, imgResRatioY*y, z, r, g, b, a) #pack it into a struct
                f.write(dataBytes)                      #write to the output file
f.close()                                           #close output file
