import StringIO
import subprocess
import os
import time
import datetime
from PIL import Image
from pymongo import MongoClient
import RPi.GPIO as GPIO


client = MongoClient("mongodb://dylonhill18:hillsrock101@testcluster-shard-00-0$
db = client.testing
client.drop_database("testing")
time.sleep(1)
timestamp = datetime.datetime.now()

DEBUG = 1
GPIO.setmode(GPIO.BCM)

threshold = 75
sensitivity = 200
forceCapture = True
forceCaptureTime = 60 * 60 # Once an hour
filepath = "/home/pi/picam"
filenamePrefix = "capture"
diskSpaceToReserve = 400 * 1024 * 1024 # Keep 4 gb free on disk
cameraSettings = ""

# settings of the photos to save
saveWidth   = 1296
saveHeight  = 972
saveQuality = 15 # Set jpeg quality (0 to 100)

# Test-Image settings
testWidth = 100
testHeight = 75
testAreaCount = 1
testBorders = [ [[1,testWidth],[1,testHeight]] ]
debugMode = False # False or True

# Capture a small test image (for motion detection)
def captureTestImage(settings, width, height):
    command = "raspistill %s -w %s -h %s -t 200 -e bmp -n -o -" % (settings, wi$
    imageData = StringIO.StringIO()
    imageData.write(subprocess.check_output(command, shell=True))
    imageData.seek(0)
    im = Image.open(imageData)
    buffer = im.load()
    imageData.close()
    return im, buffer

# Get first image
image1, buffer1 = captureTestImage(cameraSettings, testWidth, testHeight)

# Reset last capture time
lastCapture = time.time()

def RCtime (RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(1)

    GPIO.setup(RCpin, GPIO.IN)

    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    if reading < 5000:
        light = "on"
    else:
        light = "off"
    if status == 0 and light == "on":
        print ("turn lights off")
while (True):

    # Get comparison image
    image2, buffer2 = captureTestImage(cameraSettings, testWidth, testHeight)

    # Count changed pixels
    changedPixels = 0
    takePicture = False

    if (debugMode): # in debug mode, save a bitmap-file with marked changed pix$
        debugimage = Image.new("RGB",(testWidth, testHeight))
        debugim = debugimage.load()

    for z in xrange(0, testAreaCount): # = xrange(0,1) with default-values = z $
        for x in xrange(testBorders[z][0][0]-1, testBorders[z][0][1]): # = xran$
            for y in xrange(testBorders[z][1][0]-1, testBorders[z][1][1]):   # $
                if (debugMode):
                    debugim[x,y] = buffer2[x,y]
                    if ((x == testBorders[z][0][0]-1) or (x == testBorders[z][0$
                        # print "Border %s %s" % (x,y)
                        debugim[x,y] = (0, 0, 255) # in debug mode, mark all bo$
                # Just check green channel as it's the highest quality channel
                pixdiff = abs(buffer1[x,y][1] - buffer2[x,y][1])
                if pixdiff > threshold:
                    changedPixels += 1
                    if (debugMode):
                        debugim[x,y] = (0, 255, 0) # in debug mode, mark all ch$
                # Save an image if pixels changed
                if (changedPixels > sensitivity):
                    takePicture = True # will shoot the photo later
                if ((debugMode == False) and (changedPixels > sensitivity)):
                    break  # break the y loop
        if forceCapture:
        if time.time() - lastCapture > forceCaptureTime:
            takePicture = True

    if takePicture:
        lastCapture = time.time()
       # saveImage(cameraSettings, saveWidth, saveHeight, saveQuality, diskSpac$

    # Swap comparison buffers
    image1 = image2
    buffer1 = buffer2

    if takePicture:
        status = 1
    else:
        status = 0
 db.makerspace.insert(
        {"timestamp": timestamp,
        "lightstatus": RCtime(4),
        "occupancystatus": status,
        "indentifier": 1
        }
        )
    makerspacedata = db.makerspace.find(
        {"indetifier": 1
        }
        )
    print (makerspacedata)
