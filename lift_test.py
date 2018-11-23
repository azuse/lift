import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)

GPIO.output(29,GPIO.HIGH)
GPIO.output(31,GPIO.LOW)
GPIO.output(33,GPIO.LOW)
sleep(10)

GPIO.cleanup()
