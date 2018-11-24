import RPi.GPIO as GPIO
from time import sleep
import sys
import signal
import serial

class lift:
    ser = serial.Serial('/dev/ttyUSB0', 9600,timeout=1)
    ser.write(b'0')
    sleep(1)
    ser.write(b'1')
    sleep(1)
    ### led pin
    led_1 = 15
    led_2 = 23
    led_3 = 29
    led_4 = 31
    led_5 = 33
    led_6 = 37
    nowLevel = 1

    step = 2
    
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)


        GPIO.setup(self.led_1,GPIO.OUT)
        GPIO.setup(self.led_2,GPIO.OUT)
        GPIO.setup(self.led_3,GPIO.OUT)
        GPIO.setup(self.led_4,GPIO.OUT)
        GPIO.setup(self.led_5,GPIO.OUT)
        GPIO.setup(self.led_6,GPIO.OUT)

        for sig in [signal.SIGINT, signal.SIGHUP, signal.SIGTERM]:
            signal.signal(sig, self.shutdownFunction)


    def shutdownFunction(self, signalnum, frame):
        print("")
        print("shutting down")
        self.stop()
        self.ser.close()
        self.lightAllDim()
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

        if toLevel == 0 :
            self.ser.write(b'b')
            response = self.ser.readall()
            print(response)
            print("stopped(maybe")
        else:
            self.light(toLevel)
            deltaLevel = toLevel - self.nowLevel
            if deltaLevel > 0:
                print("going up")
                self.ser.write(b'w')

                sleep(self.step)
                response = self.ser.readall()
                print(response)

                self.nowLevel = toLevel
                self.stop()
            else:
                print("going down")
                self.ser.write(b's')

                sleep(self.step)
                response = self.ser.readall()
                print(response)

                self.nowLevel = toLevel
                self.stop()
            
    def stop(self):
        print("info : before stop gpio state")
        self.goto(0)
        print("info : after stop gpio state")

if __name__ == "__main__":
    if(sys.argv[1] == "up"):
        l = lift()
        l.goto(6)
    elif(sys.argv[1] == "down"):
        l = lift()
        l.goto(1)
    elif(sys.argv[1] == "stop"):
        l = lift()
        l.stop()
    
    GPIO.cleanup()

            

        

