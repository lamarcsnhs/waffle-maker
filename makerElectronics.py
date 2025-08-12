#switch RPi.GPIO to adafruit's libraries

import RPi.GPIO as GPIO
import time

#initialize GPIO
#Based on GPIO #, not pin #
#Motor Pins
motorIN1 = 16
motorIN2 = 12
motorPWM = 25 #Controls Speed
#Heat Pins
heatPin = 23
#Pump Pins
pumpPin = 4

#GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(motorIN1, GPIO.OUT)
GPIO.setup(motorIN2, GPIO.OUT)
GPIO.setup(motorPWM, GPIO.OUT)
GPIO.setup(heatPin, GPIO.OUT)
GPIO.setup(pumpPin, GPIO.OUT)

#PWM setup
pwm = GPIO.PWM(motorPWM, 100)
pwm.start(0)

def spinMotor(direction, speed, duration):
    if direction == "left":
        GPIO.output(motorIN1, GPIO.HIGH)
        GPIO.output(motorIN2, GPIO.LOW)
    elif direction == "right":
        GPIO.output(motorIN1, GPIO.LOW)
        GPIO.output(motorIN2, GPIO.HIGH)
    
    pwm.ChangeDutyCycle(speed)
    time.sleep(duration)

    pwm.ChangeDutyCycle(0)
    GPIO.output(motorIN1, GPIO.LOW)
    GPIO.output(motorIN2, GPIO.LOW)

def heat(duration):
    GPIO.output(heatPin, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(heatPin, GPIO.LOW)

def pump(duration):
    GPIO.output(pumpPin, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(pumpPin, GPIO.LOW)