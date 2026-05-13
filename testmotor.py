import RPi.GPIO as GPIO
import time

motorIN1 = 5
motorIN2 = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(motorIN1,GPIO.OUT)
GPIO.setup(motorIN2,GPIO.OUT)

GPIO.setwarnings(False)

GPIO.output(motorIN1,GPIO.HIGH)
time.sleep(6)
GPIO.output(motorIN1,GPIO.LOW)
time.sleep(6)
