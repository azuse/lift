import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(32,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)

def goto(floor):
    if floor == 1:
        GPIO.output(29,GPIO.HIGH)
        sleep(2)
        GPIO.output(29,GPIO.LOW)
    elif floor == 2:
        GPIO.output(31,GPIO.HIGH)
        sleep(2)
        GPIO.output(31,GPIO.LOW)
    elif floor == 3:
        GPIO.output(32,GPIO.HIGH)
        sleep(2)
        GPIO.output(32,GPIO.LOW)
    elif floor == 4:
        GPIO.output(33,GPIO.HIGH)
        sleep(2)
        GPIO.output(33,GPIO.LOW)
    elif floor == 5:
        GPIO.output(35,GPIO.HIGH)
        sleep(2)
        GPIO.output(35,GPIO.LOW)
    elif floor == 6:
        GPIO.output(36,GPIO.HIGH)
        sleep(2)
        GPIO.output(36,GPIO.LOW)
    else:
        pass

