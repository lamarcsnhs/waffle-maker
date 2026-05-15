import RPi.GPIO as GPIO
import time

motorIN1 = 5
motorIN2 = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(motorIN1,GPIO.OUT)
GPIO.setup(motorIN2,GPIO.OUT)

GPIO.setwarnings(False)

def switch(direction, duration):
    if(direction == "right"):
        GPIO.output(motorIN1,GPIO.HIGH)
        time.sleep(duration)
        GPIO.output(motorIN1,GPIO.LOW)
        time.sleep(1)
    elif(direction == "left"):
        GPIO.output(motorIN2,GPIO.HIGH)
        time.sleep(duration)
        GPIO.output(motorIN2,GPIO.LOW)
        time.sleep(1)

switch("right", 6)