import RPi.GPIO as GPIO
import time

motorIN1 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(motorIN1,GPIO.OUT)

GPIO.setwarnings(False)
GPIO.output(motorIN1,GPIO.HIGH)
time.sleep(30)
GPIO.output(motorIN1,GPIO.LOW)
time.sleep(1)
