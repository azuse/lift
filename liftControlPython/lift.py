import RPi.GPIO as GPIO
from time import sleep

pin_1 = 18
pin_2 = 23
pin_3 = 24   #stop
pin_4 = 25
pin_high1 = 1
pin_high2 = 12
pin_high3 = 16
state = 0
char text_receieved


GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_1,GPIO.OUT)
GPIO.setup(pin_2,GPIO.OUT)
GPIO.setup(pin_3,GPIO.OUT)
GPIO.setup(pin_4,GPIO.OUT)
GPIO.setup(pin_high1,GPIO.OUT)
GPIO.setup(pin_high2,GPIO.OUT)
GPIO.setup(pin_high3,GPIO.OUT)

GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(32,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)

nowLevel = 1

step = 1

def lightAllDim()
{
    GPIO.output(29,GPIO.LOW)
    GPIO.output(31,GPIO.LOW)
    GPIO.output(32,GPIO.LOW)
    GPIO.output(35,GPIO.LOW)
    GPIO.output(36,GPIO.LOW)
    GPIO.output(33,GPIO.LOW)
}

def light(toLevel)
{
    lightAllDim()
    if floor == 1:
        GPIO.output(29,GPIO.HIGH)
    elif floor == 2:
        GPIO.output(31,GPIO.HIGH)
    elif floor == 3:
        GPIO.output(32,GPIO.HIGH)
    elif floor == 4:
        GPIO.output(33,GPIO.HIGH)
    elif floor == 5:
        GPIO.output(35,GPIO.HIGH)
    elif floor == 6:
        GPIO.output(36,GPIO.HIGH)
    else:
        pass
}

def goto(toLevel):
    GPIO.output(pin_high1, HIGH)
    GPIO.output(pin_high2, HIGH)
    GPIO.output(pin_high3, HIGH)
    
    if toLevel = 0 :
        return 0
    else:
        light(toLevel)
        deltaLevel = toLevel - nowLevel
        if deltaLevel > 0:
            GPIO.output(pin_3, HIGH)
            GPIO.output(pin_1, LOW)
            sleep(step)
            nowLevel = toLevel
        else:
            GPIO.output(pin_3, HIGH)
            GPIO.output(pin_1, HIGH)
            sleep(step)
            nowLevel = toLevel
        

    

