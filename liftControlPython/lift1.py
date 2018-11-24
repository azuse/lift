import RPi.GPIO as GPIO
from time import sleep
import sys
import signal



class lift:
    ### lift control pin
    pin_1 = 12   #方向 -
    pin_3 = 32   #脱机 -
    pin_high1 = 26 #脉冲 +
    pin_high2 = 18 #脱机 +
    pin_high3 = 36 #方向 +
    state = 0

    ### led pin
    led_1 = 15
    led_2 = 23
    led_3 = 29
    led_4 = 31
    led_5 = 33
    led_6 = 37

    nowLevel = 1

    step = 0
    
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin_1,GPIO.OUT)
        GPIO.setup(self.pin_3,GPIO.OUT)
        GPIO.setup(self.pin_high1,GPIO.OUT)
        GPIO.setup(self.pin_high2,GPIO.OUT)
        GPIO.setup(self.pin_high3,GPIO.OUT)

        GPIO.setup(self.led_1,GPIO.OUT)
        GPIO.setup(self.led_2,GPIO.OUT)
        GPIO.setup(self.led_3,GPIO.OUT)
        GPIO.setup(self.led_4,GPIO.OUT)
        GPIO.setup(self.led_5,GPIO.OUT)
        GPIO.setup(self.led_6,GPIO.OUT)

        for sig in [signal.SIGINT, signal.SIGHUP, signal.SIGTERM]:
            signal.signal(sig, self.shutdownFunction)
        GPIO.output(self.pin_high2, GPIO.HIGH)

        print("GPIO initialed: ")
        self.printPin()

    def printPin(self):
        print("pin_1 : " + str(GPIO.input(self.pin_1)))
        print("pin_3 : " + str(GPIO.input(self.pin_3)))
        print("pin_high1 : " + str(GPIO.input(self.pin_high1)))
        print("pin_high2 : " + str(GPIO.input(self.pin_high2)))
        print("pin_high3 : " + str(GPIO.input(self.pin_high3)))
        print("")
        print()

    def shutdownFunction(self, signalnum, frame):
        print("")
        print("shutting down")
        self.stop()
        GPIO.cleanup()
        exit(-1)

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
        GPIO.output(self.pin_high2, GPIO.LOW)
        
        if toLevel == 0 :
            
            print("stopped(maybe")
        else:
            self.light(toLevel)
            deltaLevel = toLevel - self.nowLevel
            if deltaLevel > 0:
                GPIO.output(self.pin_3, GPIO.HIGH)
                GPIO.output(self.pin_1, GPIO.LOW)
                sleep(self.step)
                self.nowLevel = toLevel
            else:
                GPIO.output(self.pin_3, GPIO.HIGH)
                GPIO.output(self.pin_1, GPIO.HIGH)
                sleep(self.step)
                self.nowLevel = toLevel

        print("gpio changed :")
        self.printPin()
    
    def stop(self):
        print("info : before stop gpio state")
        self.printPin()
        self.goto(0)
        print("info : after stop gpio state")
        self.printPin()

if __name__ == "__main__":
    if(sys.argv[1] == "up"):
        l = lift()
        l.goto(6)
    elif(sys.argv[1] == "down"):
        l = lift()
        l.goto(1)
    elif(sys.argv[1] == "stop") :
        l = lift()
        l.stop()
    sleep(100)
    GPIO.cleanup()

            

        

