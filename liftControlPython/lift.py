import RPi.GPIO as GPIO
from time import sleep

class lift:
    ### lift control pin
    pin_1 = 12
    pin_2 = 16
    pin_3 = 18   #stop
    pin_4 = 22
    pin_high1 = 26
    pin_high2 = 32
    pin_high3 = 36
    state = 0

    ### led pin
    led_1 = 15
    led_2 = 23
    led_3 = 29
    led_4 = 31
    led_5 = 33
    led_6 = 37

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(lift.pin_1,GPIO.OUT)
        GPIO.setup(lift.pin_2,GPIO.OUT)
        GPIO.setup(lift.pin_3,GPIO.OUT)
        GPIO.setup(lift.pin_4,GPIO.OUT)
        GPIO.setup(lift.pin_high1,GPIO.OUT)
        GPIO.setup(lift.pin_high2,GPIO.OUT)
        GPIO.setup(lift.pin_high3,GPIO.OUT)

        GPIO.setup(lift.led_1,GPIO.OUT)
        GPIO.setup(lift.led_2,GPIO.OUT)
        GPIO.setup(lift.led_3,GPIO.OUT)
        GPIO.setup(lift.led_4,GPIO.OUT)
        GPIO.setup(lift.led_5,GPIO.OUT)
        GPIO.setup(lift.led_6,GPIO.OUT)

        nowLevel = 1

        step = 1

    def lightAllDim():
        GPIO.output(lift.led_1,GPIO.LOW)
        GPIO.output(lift.led_2,GPIO.LOW)
        GPIO.output(lift.led_3,GPIO.LOW)
        GPIO.output(lift.led_5,GPIO.LOW)
        GPIO.output(lift.led_6,GPIO.LOW)
        GPIO.output(lift.led_4,GPIO.LOW)


    def light(floor):
        lightAllDim()
        if floor == 1:
            GPIO.output(lift.led_1,GPIO.HIGH)
        elif floor == 2:
            GPIO.output(lift.led_2,GPIO.HIGH)
        elif floor == 3:
            GPIO.output(lift.led_3,GPIO.HIGH)
        elif floor == 4:
            GPIO.output(lift.led_4,GPIO.HIGH)
        elif floor == 5:
            GPIO.output(lift.led_5,GPIO.HIGH)
        elif floor == 6:
            GPIO.output(lift.led_6,GPIO.HIGH)
        else:
            pass

    def goto(toLevel):
        GPIO.output(lift.pin_high1, GPIO.HIGH)
        GPIO.output(lift.pin_high2, GPIO.HIGH)
        GPIO.output(lift.pin_high3, GPIO.HIGH)
        
        if toLevel == 0 :
            return 0
        else:
            light(toLevel)
            deltaLevel = toLevel - nowLevel
            if deltaLevel > 0:
                GPIO.output(lift.pin_3, GPIO.HIGH)
                GPIO.output(lift.pin_1, GPIO.LOW)
                sleep(step)
                nowLevel = toLevel
            else:
                GPIO.output(lift.pin_3, GPIO.HIGH)
                GPIO.output(lift.pin_1, GPIO.HIGH)
                sleep(step)
                nowLevel = toLevel
            

        

