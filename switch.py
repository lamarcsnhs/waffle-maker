from gpiozero import OutputDevice, DigitalInputDevice
from time import sleep, time

# H-bridge control pins

IN1 = OutputDevice(17, active_high=True, initial_value=False)
IN2 = OutputDevice(27, active_high=True, initial_value=False)


# Valve feedback pins
# White wire -> Pi GND
# Green wire -> GPIO 22
# Yellow wire -> GPIO 23

open_feedback = DigitalInputDevice(22, pull_up=True)
closed_feedback = DigitalInputDevice(23, pull_up=True)

TIMEOUT = 10
HOLD_TIME = 6

def stop_valve():
    IN1.off()
    IN2.off()

def drive_open_direction():
    IN1.on()
    IN2.off()

def drive_closed_direction():
    IN1.off()
    IN2.on()

def is_open():
    # With pull_up=True, feedback wire touching GND reads inactive/False
    # gpiozero DigitalInputDevice.value is 0 when connected to ground.
    return open_feedback.value == 0

def is_closed():
    return closed_feedback.value == 0

def get_position():
    if is_open() and not is_closed():
        return "OPEN"

    if is_closed() and not is_open():
        return "CLOSED"

    if not is_open() and not is_closed():
        return "MOVING / BETWEEN"

    return "ERROR: BOTH FEEDBACK WIRES ACTIVE"


def wait_until_open():
    start = time()
    while not is_open():
        if time() - start > TIMEOUT:
            stop_valve()
            raise TimeoutError("Valve did not report OPEN within timeout.")
        sleep(0.05)

def wait_until_closed():
    start = time()
    while not is_closed():
        if time() - start > TIMEOUT:
            stop_valve()
            raise TimeoutError("Valve did not report CLOSED within timeout.")
        sleep(0.05)

def move_to_open():
    print("Switching toward OPEN...")
    drive_open_direction()
    wait_until_open()
    stop_valve()
    print("Done. Position:", get_position())
 
def move_to_closed():
    print("Switching toward CLOSED...")
    drive_closed_direction()
    wait_until_closed()
    stop_valve()
    print("Done. Position:", get_position())


try:
    print("Starting position:", get_position())
    if get_position() == "OPEN":
        print(f"Leaving OPEN for {HOLD_TIME} seconds...")
        sleep(HOLD_TIME)
        move_to_closed()

    elif get_position() == "CLOSED":
        print(f"Leaving CLOSED for {HOLD_TIME} seconds...")
        sleep(HOLD_TIME)
        move_to_open()

    else:
        print("Position unclear. Moving to OPEN first...")
        move_to_open()
        print(f"Leaving OPEN for {HOLD_TIME} seconds...")
        sleep(HOLD_TIME)
        move_to_closed()

finally:
    stop_valve()
    print("Motor stopped.")

