import RPi.GPIO as GPIO
import time

motorIN1 = 6
motorIN2 = 22

GPIO.setmode(GPIO.BCM)

GPIO.setup(motorIN1,GPIO.OUT)
GPIO.setup(motorIN2,GPIO.OUT)

GPIO.setwarnings(False)


def mix(duration):
    GPIO.output(motorIN1,GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(motorIN1,GPIO.LOW)
    time.sleep(1)
#pump while mixing

mix(30)