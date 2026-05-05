import xarm
from time import sleep

arm = xarm.Controller('USB')

arm.setPosition([[1, arm.getPosition(1)]], 100, True)
sleep(0.5)

MOVE_TIME = 400000  # ms, increase to move slower

def move(positions, speed=MOVE_TIME):
    """Move multiple servos at once. positions is a list of [servo_id, position]."""
    arm.setPosition(positions, speed, True)



def stand_straight(speed=MOVE_TIME):
    move([[2, 500], [3, 500], [4, 500], [5, 500], [6, 500]], speed)



def rotate_base_left(amount=200, speed=MOVE_TIME):
    pos = arm.getPosition(6)
    move([[6, pos + amount]], speed)

def rotate_base_right(amount=200, speed=MOVE_TIME):
    pos = arm.getPosition(6)
    move([[6, pos - amount]], speed)



def shoulder_up(amount=200, speed=MOVE_TIME):
    pos = arm.getPosition(5)
    move([[5, pos + amount]], speed)

def shoulder_down(amount=200, speed=MOVE_TIME):
    pos = arm.getPosition(5)
    move([[5, pos - amount]], speed)



def elbow_up(amount=200, speed=MOVE_TIME):
    pos = arm.getPosition(4)
    move([[4, pos + amount]], speed)

def elbow_down(amount=200, speed=MOVE_TIME):
    pos = arm.getPosition(4)
    move([[4, pos - amount]], speed)



def wrist_up(amount=200, speed=MOVE_TIME):
    pos = arm.getPosition(3)
    move([[3, pos + amount]], speed)

def wrist_down(amount=200, speed=MOVE_TIME):
    pos = arm.getPosition(3)
    move([[3, pos - amount]], speed)



def wrist_rotate_left(amount=200, speed=MOVE_TIME):
    pos = arm.getPosition(2)
    move([[2, pos + amount]], speed)

def wrist_rotate_right(amount=200, speed=MOVE_TIME):
    pos = arm.getPosition(2)
    move([[2, pos - amount]], speed)



def close_gripper(speed=MOVE_TIME):
    move([[1, 1000]], speed)

def open_gripper(speed=MOVE_TIME):
    move([[1, 0]], speed)



def relax():
    """Turn off all servos so you can move the arm by hand."""
    for i in range(1, 7):
        arm.servoOff(i)

def read_all_positions():
    """Print current position of all servos."""
    for i in range(1, 7):
        sleep(0.1)
        print(f"Servo {i}: {arm.getPosition(i)}")



stand_straight()