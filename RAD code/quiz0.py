import time
import RPi.GPIO as GPIO

GPIO.setmode (GPIO.BCM)
GPIO.setup (4, GPIO.OUT)
GPIO.setup (1, GPIO.IN pull_up_down=GPIO.PUD_UP)


 while True:
    ledblink (2)
    ledblink (3)
    input_state = GPIO.input (1)
    if input_state == True:
        ledblink(3);
    else:
        GPIO.OUTPUT (4, GPIO.LOW)

def ledblink(t):
     GPIO.OUTPUT (4, GPIO.HIGH)
     time.sleep (t)
     GPIO.OUTPUT (4, GPIO.LOW)
     time.sleep (t)
