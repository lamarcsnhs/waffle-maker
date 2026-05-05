# switch RPi.GPIO to adafruit's libraries

import RPi.GPIO as GPIO
import time

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
        time.sleep(duration)
        GPIO.output(motorIN2, GPIO.LOW)
    elif direction == "right":
        GPIO.output(motorIN1, GPIO.LOW)
        # print("spinning right")
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
        print("going down")
        time.sleep(duration)
        GPIO.output(linearIN1, GPIO.LOW)
        print("went down for", duration, "sec" )
    elif direction == "up":
        GPIO.output(linearIN2, GPIO.HIGH)
        print("going up")
        time.sleep(duration+1)
        GPIO.output(linearIN2, GPIO.LOW)
        print("went up for", duration+1, "sec" )
    GPIO.output(linearIN1, GPIO.LOW)
    GPIO.output(linearIN2, GPIO.LOW)


def heat(duration):
    GPIO.output(heatPin, GPIO.HIGH)
    print("heating")
    time.sleep(duration)
    GPIO.output(heatPin, GPIO.LOW)

def pump(duration):
    GPIO.output(pumpPin, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(pumpPin, GPIO.LOW)

def preheat(duration):
    # close lid
    moveLinearActuator("down", 14.5)
    time.sleep(2)

    # heat
    heat(duration)
    time.sleep(2)

    # open lid
    moveLinearActuator("up", 14.5)
    time.sleep(2)

def wiggle(loops, duration):
    print("wiggling")
    for x in range(int(loops)):
        spinMotor("left", 37, duration)
        spinMotor("right", 37, duration)
    

def run():
    # close lid
    moveLinearActuator("down", 14.5)
    time.sleep(2)

    # heat (240)
    heat(240)
    time.sleep(6)

    # open lid
    moveLinearActuator("up", 14.5)
    time.sleep(20)

    # spin motor
    spinMotor("left", 37, .37)
    time.sleep(2)

    # wiggle motor
    wiggle(70, .02)
    time.sleep(20)    

    # spin motor again
    spinMotor("right", 37, 1.35)

    # fix spinning it was not doing a 180
    # jiffy was pretty good

    # wiggle before to even out  batter ????
    
run()
# preheat(60)
# wiggle(50, .02)