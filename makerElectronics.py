import RPi.GPIO as GPIO
import time

# motor pins
motorIN1 = 19
motorIN2 = 12
motorPWM = 25

# linear actuator pins
linearIN1 = 17
linearIN2 = 18

# heat pin
heatPin = 21

# pump pin
pumpPin = 4

# hall effect sensor pin
HALL_PIN = 2

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
GPIO.setup(HALL_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# PWM setup
pwm = GPIO.PWM(motorPWM, 100)
pwm.start(0)


def stopMotor():
    pwm.ChangeDutyCycle(0)
    GPIO.output(motorIN1, GPIO.LOW)
    GPIO.output(motorIN2, GPIO.LOW)

def spinMotor(direction, speed, duration):
    if direction == "left":
        GPIO.output(motorIN1, GPIO.HIGH)
        GPIO.output(motorIN2, GPIO.LOW)
    elif direction == "right":
        GPIO.output(motorIN1, GPIO.LOW)
        GPIO.output(motorIN2, GPIO.HIGH)

    pwm.ChangeDutyCycle(speed)

    start = time.time()
    while time.time() - start < duration:
        if GPIO.input(HALL_PIN) == GPIO.HIGH:
            print("magnet detected, stopping motor")
            break
        time.sleep(0.01)

    stopMotor()

def moveLinearActuator(direction, duration):
    if direction == "down":
        GPIO.output(linearIN1, GPIO.HIGH)
        print("going down")
        time.sleep(duration)
        GPIO.output(linearIN1, GPIO.LOW)
        print("went down for", duration, "sec")
    elif direction == "up":
        GPIO.output(linearIN2, GPIO.HIGH)
        print("going up")
        time.sleep(duration + 1)
        GPIO.output(linearIN2, GPIO.LOW)
        print("went up for", duration + 1, "sec")
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
    moveLinearActuator("down", 14.5)
    time.sleep(2)
    heat(duration)
    time.sleep(2)
    moveLinearActuator("up", 14.5)
    time.sleep(2)

def wiggle(loops, duration):
    print("wiggling")
    for x in range(int(loops)):
        spinMotor("left", 37, duration)
        spinMotor("right", 37, duration)

def run():
    # # close lid
    # moveLinearActuator("down", 14.5)
    # time.sleep(2)

    # # heat
    # heat(260)
    # time.sleep(6)

    # # open lid
    # moveLinearActuator("up", 14.5)
    # time.sleep(20)

    # spin motor
    spinMotor("left", 37, 2)
    time.sleep(2)

    # wiggle motor
    wiggle(70, .02)
    time.sleep(2)

    # spin motor again
    spinMotor("right", 37, 2)


try:
    run()

except KeyboardInterrupt:
    print("Interrupted.")

finally:
    stopMotor()
    pwm.stop()
    GPIO.cleanup()