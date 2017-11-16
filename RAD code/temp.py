import RPi.GPIO as GPIO
import dht11
import time
import datetime
from pymongo import MongoClient

client = MongoClient("mongodb://dylonhill18:hillsrock101@testcluster-shard-00-00-odrn0.mongodb.net:27017,testcluster-shard-00-01-odrn0.mongodb.net:27017,testcluster-shard-00-02-odrn0.mongodb.net:27017/test?ssl=true&replicaSet=testcluster-shard-0&authSource=admin")
db = client.testing
client.drop_database("testing")
time.sleep(1)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
timestamp = datetime.datetime.now()

# read data using pin 17
instance = dht11.DHT11(pin=17)


while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Temperature: %d F" % ((result.temperature * (9/5) + 32)))
        print("Humidity: %d %%" % result.humidity)
        db.makerspace.insert({"timestamp": timestamp,"lightstatus": result,"identifier": 1})
        makerspacedata = db.makerspace.find({"identifier": 1})
        print (makerspacedata)
    time.sleep(5)
