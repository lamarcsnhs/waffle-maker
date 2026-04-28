#switch RPi.GPIO to adafruit's libraries

import RPi.GPIO as GPIO
import time

#initialize GPIO
#Based on GPIO #, not pin #
#Motor Pins
motorIN1 = 19
motorIN2 = 12
motorPWM = 25 #Controls Speed
#linear actuator pins
linearIN1 = 17
linearIN2 = 18
#Heat Pins
heatPin = 21
#Pump Pins
pumpPin = 4

#GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(motorIN1, GPIO.OUT)
GPIO.setup(motorIN2, GPIO.OUT)
GPIO.setup(motorPWM, GPIO.OUT)
GPIO.setup(linearIN1, GPIO.OUT)
GPIO.setup(linearIN2, GPIO.OUT)
GPIO.setup(heatPin, GPIO.OUT)
GPIO.setup(pumpPin, GPIO.OUT)

#PWM setup
pwm = GPIO.PWM(motorPWM, 100)
pwm.start(0)

def spinMotor(direction, speed, duration):
    if direction == "left":
        GPIO.output(motorIN1, GPIO.HIGH)
        print('spinning left')
        time.sleep(duration)
        GPIO.output(motorIN2, GPIO.LOW)
    elif direction == "right":
        GPIO.output(motorIN1, GPIO.LOW)
        print('spinning right')
        time.sleep(duration)
        GPIO.output(motorIN2, GPIO.HIGH)
    
    pwm.ChangeDutyCycle(speed)
    time.sleep(duration)

    pwm.ChangeDutyCycle(0)
    GPIO.output(motorIN1, GPIO.LOW)
    GPIO.output(motorIN2, GPIO.LOW)

def moveLinearActuator(direction, duration):
    if direction == "down":
        GPIO.output(linearIN1, GPIO.HIGH)
        print('going down')
        time.sleep(duration)
        GPIO.output(linearIN1, GPIO.LOW)
        print('went down for', duration, 'sec' )
    elif direction == "up":
        GPIO.output(linearIN2, GPIO.HIGH)
        print('going up')
        time.sleep(duration+1)
        GPIO.output(linearIN2, GPIO.LOW)
        print('went up for', duration+1, 'sec' )
    GPIO.output(linearIN1, GPIO.LOW)
    GPIO.output(linearIN2, GPIO.LOW)


def heat(duration):
    GPIO.output(heatPin, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(heatPin, GPIO.LOW)

def pump(duration):
    GPIO.output(pumpPin, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(pumpPin, GPIO.LOW)

def preheat(duration):
    GPIO.output(heatPin, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(heatPin, GPIO.LOW)

def run():
    # close lid
    moveLinearActuator("down", 14.5)
    time.sleep(2)

    # heat
    heat(230)
    time.sleep(6)

    # open lid
    moveLinearActuator("up", 14.5)
    time.sleep(2)

    # spin motor
    spinMotor("left", 37, .36)
    time.sleep(20)

    # wip: wiggle motor
# stay longer flat for it to cool before we flip
# let it stay flipped for longer to let gravity work
# fix spinning it was not doing a 180
# jiffy was pretty
# preheat

    # spin motor again
    spinMotor("right", 37, 1.25)
    
run()