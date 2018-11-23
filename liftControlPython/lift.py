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
        GPIO.setup(self.pin_1,GPIO.OUT)
        GPIO.setup(self.pin_2,GPIO.OUT)
        GPIO.setup(self.pin_3,GPIO.OUT)
        GPIO.setup(self.pin_4,GPIO.OUT)
        GPIO.setup(self.pin_high1,GPIO.OUT)
        GPIO.setup(self.pin_high2,GPIO.OUT)
        GPIO.setup(self.pin_high3,GPIO.OUT)

        GPIO.setup(self.led_1,GPIO.OUT)
        GPIO.setup(self.led_2,GPIO.OUT)
        GPIO.setup(self.led_3,GPIO.OUT)
        GPIO.setup(self.led_4,GPIO.OUT)
        GPIO.setup(self.led_5,GPIO.OUT)
        GPIO.setup(self.led_6,GPIO.OUT)

        nowLevel = 1

        step = 1

    def lightAllDim(self):
        GPIO.output(self.led_1,GPIO.LOW)
        GPIO.output(self.led_2,GPIO.LOW)
        GPIO.output(self.led_3,GPIO.LOW)
        GPIO.output(self.led_5,GPIO.LOW)
        GPIO.output(self.led_6,GPIO.LOW)
        GPIO.output(self.led_4,GPIO.LOW)


    def light(self, floor):
        self.lightAllDim()
        if floor == 1:
            GPIO.output(self.led_1,GPIO.HIGH)
        elif floor == 2:
            GPIO.output(self.led_2,GPIO.HIGH)
        elif floor == 3:
            GPIO.output(self.led_3,GPIO.HIGH)
        elif floor == 4:
            GPIO.output(self.led_4,GPIO.HIGH)
        elif floor == 5:
            GPIO.output(self.led_5,GPIO.HIGH)
        elif floor == 6:
            GPIO.output(self.led_6,GPIO.HIGH)
        else:
            pass

    def goto(self, toLevel):
        GPIO.output(self.pin_high1, GPIO.HIGH)
        GPIO.output(self.pin_high2, GPIO.HIGH)
        GPIO.output(self.pin_high3, GPIO.HIGH)
        
        if toLevel == 0 :
            return 0
        else:
            self.light(toLevel)
            deltaLevel = toLevel - self.nowLevel
            if deltaLevel > 0:
                GPIO.output(self.pin_3, GPIO.HIGH)
                GPIO.output(self.pin_1, GPIO.LOW)
                sleep(step)
                nowLevel = toLevel
            else:
                GPIO.output(self.pin_3, GPIO.HIGH)
                GPIO.output(self.pin_1, GPIO.HIGH)
                sleep(step)
                self.nowLevel = toLevel
            

        

