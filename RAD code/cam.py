import StringIO
import subprocess
import os
import time
import datetime
from PIL import Image
from pymongo import MongoClient

client = MongoClient("mongodb://dylonhill18:hillsrock101@testcluster-shard-00-0$
db = client.testing
client.drop_database("testing")
time.sleep(1)
timestamp = datetime.datetime.now()

threshold = 75
sensitivity = 200
forceCapture = True
forceCaptureTime = 60 * 60 # Once an hour
filepath = "/home/pi/picam"
filenamePrefix = "capture"
diskSpaceToReserve = 400 * 1024 * 1024 # Keep 4 gb free on disk
cameraSettings = ""

saveWidth   = 1296
saveHeight  = 972
saveQuality = 15 # Set jpeg quality (0 to 100)

# Test-Image settings
testWidth = 100
testHeight = 75

# this is the default setting, if the whole image should be scanned for changed p$
testAreaCount = 1
testBorders = [ [[1,testWidth],[1,testHeight]] ]

debugMode = False # False or True

# Capture a small test image (for motion detection)
def captureTestImage(settings, width, height):
    command = "raspistill %s -w %s -h %s -t 200 -e bmp -n -o -" % (settings, widt$
    imageData = StringIO.StringIO()
    imageData.write(subprocess.check_output(command, shell=True))
    imageData.seek(0)
    im = Image.open(imageData)
    buffer = im.load()
    imageData.close()
    return im, buffer

image1, buffer1 = captureTestImage(cameraSettings, testWidth, testHeight)

# Reset last capture time
lastCapture = time.time()

while (True):

    # Get comparison image
    image2, buffer2 = captureTestImage(cameraSettings, testWidth, testHeight)

    # Count changed pixels
    changedPixels = 0
    takePicture = False

    if (debugMode): # in debug mode, save a bitmap-file with marked changed pixel$
        debugimage = Image.new("RGB",(testWidth, testHeight))
        debugim = debugimage.load()

    for z in xrange(0, testAreaCount): # = xrange(0,1) with default-values = z wi$
        for x in xrange(testBorders[z][0][0]-1, testBorders[z][0][1]): # = xrange$
            for y in xrange(testBorders[z][1][0]-1, testBorders[z][1][1]):   # = $
                if (debugMode):
                    debugim[x,y] = buffer2[x,y]
                    if ((x == testBorders[z][0][0]-1) or (x == testBorders[z][0][$
                        # print "Border %s %s" % (x,y)
                        debugim[x,y] = (0, 0, 255) # in debug mode, mark all bord$
                # Just check green channel as it's the highest quality channel
                pixdiff = abs(buffer1[x,y][1] - buffer2[x,y][1])
                if pixdiff > threshold:
                    changedPixels += 1
                    if (debugMode):
                        debugim[x,y] = (0, 255, 0) # in debug mode, mark all chan$
                # Save an image if pixels changed
                if (changedPixels > sensitivity):
                         takePicture = True # will shoot the photo later
                if ((debugMode == False) and (changedPixels > sensitivity)):
                    break  # break the y loop
            if ((debugMode == False) and (changedPixels > sensitivity)):
                break  # break the x loop
        if ((debugMode == False) and (changedPixels > sensitivity)):
            break  # break the z loop

    #if (debugMode):
     #   debugimage.save(filepath + "/debug.bmp") # save debug image as bmp
       # print "debug.bmp saved, %s changed pixel" % changedPixels
    # else:
    #     print "%s changed pixel" % changedPixels

    # Check force capture
    if forceCapture:
        if time.time() - lastCapture > forceCaptureTime:
            takePicture = True
    if takePicture:
        lastCapture = time.time()
       # saveImage(cameraSettings, saveWidth, saveHeight, saveQuality, diskSpaceT$

    # Swap comparison buffers
    image1 = image2
    buffer1 = buffer2

    if takePicture:
        status = 1
        print status
    else:
        status = 0
        print status

    db.makerspace.insert(
        {"timestamp": timestamp,
        "occupancystatus": status,
        "indentifier": 1
        }
        )
     makerspacedata = db.makerspace.find(
        {"indetifier": 1
        }
        )
    print (makerspacedata)
