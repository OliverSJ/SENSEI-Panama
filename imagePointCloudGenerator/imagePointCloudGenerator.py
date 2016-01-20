import Image;
import png;
import struct;

filename = "newpng.xyzb"                        #output filename
picname = "Yoshi.png"                           #picture filename
image = Image.open(picname)                     #open the image
pixInfo = image.load()                          #loads pixel data into pixInfo
(i,_) = image.size                              #gives x-size
(_,j) = image.size                              #gives y-size
f = open(filename, 'wb')
for x in range(i-1,-1,-1):                       #iterate through all pixels in reverse
    for y in range(j-1,-1,-1):
        z = 0                                   #z will remain 0 for now
                                                #later we will get it from
                                                #terrain map
        r = float(pixInfo[x, y][0])             #r value from tuple
        r = r/255.0
        g = float(pixInfo[x, y][1])             #g value from tuple
        g = g/255.0
        b = float(pixInfo[x, y][2])             #b value from tuple
        b = b/255.0
        a = float(pixInfo[x, y][3])             #a value from tuple
        a = a/255.0
        dataBytes = struct.pack('ddddddd', x, y, z, r, g, b, a) #pack it into a struct
        f.write(dataBytes)                      #write to the output file
f.close()                                       #close output file
