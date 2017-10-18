from pymongo import MongoClient
import RPi.GPIO as GPIO
import time
import os
import datetime

client = MongoClient("mongodb://dylonhill18:hillsrock101@testcluster-shard-00-00-odrn0.mongodb.net:27017,testcluster-shard-00-01-odrn0.mongodb.net:27017,testcluster-shard-00-02-odrn0.mongodb.net:27017/test?ssl=true&replicaSet=testcluster-shard-0&authSource=admin")
db = client.testing
client.drop_database("testing")
time.sleep(1)

DEBUG = 1
GPIO.setmode(GPIO.BCM)
timestamp = datetime.datetime.now()

def RCtime (RCpin):
        reading = 0
        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
        time.sleep(1)

        GPIO.setup(RCpin, GPIO.IN)

        while (GPIO.input(RCpin) == GPIO.LOW):
                reading += 1
        if reading < 5000:
                status = "on"
        else:
                status = "off"

        return status
while True:
        #print RCtime(4)
        db.makerspace.insert(
                {"timestamp": timestamp,
                "lightstatus": RCtime(4),
                "identifier": 1
                }
                )
        makerspacedata = db.makerspace.find(
                {"identifier": 1
                }
                )
        print (makerspacedata)
