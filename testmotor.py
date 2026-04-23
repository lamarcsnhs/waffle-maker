import RPi.GPIO as GPIO
import time

motorIN1 = 17
motorIN2 = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(motorIN1,GPIO.OUT)
GPIO.setup(motorIN2,GPIO.OUT)

GPIO.setwarnings(False)
GPIO.output(motorIN2,GPIO.HIGH)
time.sleep(1)
GPIO.output(motorIN2,GPIO.LOW)
time.sleep(1)
