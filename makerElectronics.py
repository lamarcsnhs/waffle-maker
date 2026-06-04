# switch RPi.GPIO to adafruit's libraries

import RPi.GPIO as GPIO
import serial
import time
import robotarm as robot
import mixMotor as mixer
import dispenserMotor as dispenser
from time import sleep

# initialize GPIO
# based on GPIO #, not pin #

# motor pins
motorIN1 = 19
motorIN2 = 12
motorPWM = 25 # controls speed

# linear actuator pins
linearIN1 = 17
linearIN2 = 18

# heat pin
heatPin = 21

# pump pins
pumpPin = 4

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(motorIN1, GPIO.OUT)
GPIO.setup(motorIN2, GPIO.OUT)
GPIO.setup(motorPWM, GPIO.OUT)
GPIO.setup(linearIN1, GPIO.OUT)
GPIO.setup(linearIN2, GPIO.OUT)
GPIO.setup(heatPin, GPIO.OUT)
GPIO.setup(pumpPin, GPIO.OUT)

# PWM setup
pwm = GPIO.PWM(motorPWM, 100)
pwm.start(0)

def spinMotor(direction, speed, duration):
    if direction == "left":
        GPIO.output(motorIN1, GPIO.HIGH)
        # print("spinning left")
        sleep(duration)
        GPIO.output(motorIN2, GPIO.LOW)
    elif direction == "right":
        GPIO.output(motorIN1, GPIO.LOW)
        # print("spinning right")
        sleep(duration)
        GPIO.output(motorIN2, GPIO.HIGH)
    
    pwm.ChangeDutyCycle(speed)
    sleep(duration)

    pwm.ChangeDutyCycle(0)
    GPIO.output(motorIN1, GPIO.LOW)
    GPIO.output(motorIN2, GPIO.LOW)

def moveLinearActuator(direction, duration):
    if direction == "down":
        GPIO.output(linearIN1, GPIO.HIGH)
        print("going down")
        sleep(duration)
        GPIO.output(linearIN1, GPIO.LOW)
        print("went down for", duration, "sec" )
    elif direction == "up":
        GPIO.output(linearIN2, GPIO.HIGH)
        print("going up")
        sleep(duration+1)
        GPIO.output(linearIN2, GPIO.LOW)
        print("went up for", duration+1, "sec" )
    GPIO.output(linearIN1, GPIO.LOW)
    GPIO.output(linearIN2, GPIO.LOW)


def heat(duration):
    GPIO.output(heatPin, GPIO.HIGH)
    print("heating")
    sleep(duration)
    GPIO.output(heatPin, GPIO.LOW)

def pump(duration):
    GPIO.output(pumpPin, GPIO.HIGH)
    sleep(duration)
    GPIO.output(pumpPin, GPIO.LOW)

def preheat(duration):
    # close lid
    moveLinearActuator("down", 14.5)
    sleep(2)

    # heat
    heat(duration)
    sleep(2)

    # open lid
    moveLinearActuator("up", 14.5)
    sleep(2)

def wiggle(loops, duration):
    print("wiggling")
    for x in range(int(loops)):
        spinMotor("left", 37, duration-.01)
        spinMotor("right", 37, duration)

def run():
    # robot.move([[1, 649], [2, 502], [3, 244], [4, 669], [5, 133], [6, 679]], speed=robot.MOVE_TIME)


    # dispenser.dispense(30)
    # sleep(5)
    

    # mixer.mix(30)
    # sleep(5)

    # robot.move_to_pump()
    # sleep(30)

    # close lid
    moveLinearActuator("down", 14.5)
    sleep(2)

    # heat (240)
    heat(250)
    sleep(6)

    # open lid
    moveLinearActuator("up", 14.5)
    sleep(20)

    # spin motor
    spinMotor("left", 37, .18)
    sleep(2)

    # wiggle motor
    wiggle(70, .022)
    sleep(2)    

    # spin motor again
    spinMotor("right", 37, .47)

    
# preheat(60)
# run()
wiggle(30,0.2)

# wiggle(50, .022)