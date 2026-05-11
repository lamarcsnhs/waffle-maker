import RPi.GPIO as GPIO
import time

HALL_PIN = 4


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(HALL_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        if GPIO.input(HALL_PIN) == GPIO.LOW:
            print("Magnet ON")
        else:
            print("Magnet OFF")
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting.")

finally:
    GPIO.cleanup()