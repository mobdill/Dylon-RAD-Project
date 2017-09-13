import RPi.GPIO as gpio
import time

gpio.setmode (gpio.BCM)
gpio.setup (4, gpio.OUT)

for i in range (0, 10000):

    gpio.output(4, True)
    time.sleep(2)
    gpio.output(4, False)
    time.sleep(2)
gpio.cleanup()


