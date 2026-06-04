import RPi.GPIO as GPIO
import time

motorIN1 = 10
motorIN2 = 26

GPIO.setmode(GPIO.BCM)

GPIO.setup(motorIN1, GPIO.OUT)
GPIO.setup(motorIN2, GPIO.OUT)

# Reverse direction
# GPIO.output(motorIN1, GPIO.LOW)

def dispense(duration):
    GPIO.output(motorIN2, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(motorIN2, GPIO.LOW)

# dispense(260)
GPIO.output(motorIN2, GPIO.LOW)

GPIO.cleanup()