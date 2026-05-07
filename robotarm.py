import xarm
from time import sleep

arm = xarm.Controller('USB')
sleep(0.5)
MOVE_TIME = 1500  # changing this doesn't work :(

# servo 6 = base
# servo 5 = shoulder
# servo 4 = elbow
# servo 3 = wrist
# servo 2 = wrist_rotate
# servo 1 = gripper


def move(positions, speed=MOVE_TIME):
    """move multiple servos at once. positions is a list of [servo_id, position]."""
    arm.setPosition(positions, speed, False)
    sleep(2)

def stand_straight(speed=MOVE_TIME):
    move([[2, 500], [3, 500], [4, 500], [5, 500], [6, 500]], speed)
    print("stood straight")
    


def rotate_base_left(amount=200, speed=MOVE_TIME):
    pos = arm.getPosition(6)
    move([[6, pos + amount]], speed)
    print("rotated base left", amount)

def rotate_base_right(amount=200, speed=MOVE_TIME):
    pos = arm.getPosition(6)
    move([[6, pos - amount]], speed)
    print("rotated base right", amount)



def shoulder_up(amount=100, speed=MOVE_TIME):
    pos = arm.getPosition(5)
    move([[5, pos + amount]], speed)
    print("moved shoulder up", amount)

def shoulder_down(amount=100, speed=MOVE_TIME):
    pos = arm.getPosition(5)
    move([[5, pos - amount]], speed)
    print("moved shoulder down", amount)



def elbow_up(amount=200, speed=MOVE_TIME):
    pos = arm.getPosition(4)
    move([[4, pos + amount]], speed)
    print("moved elbow up", amount)

def elbow_down(amount=200, speed=MOVE_TIME):
    pos = arm.getPosition(4)
    move([[4, pos - amount]], speed)
    print("moved elbow down", amount)



def wrist_up(amount=200, speed=MOVE_TIME):
    pos = arm.getPosition(3)
    move([[3, pos + amount]], speed)
    print("moved wrist up", amount)

def wrist_down(amount=200, speed=MOVE_TIME):
    pos = arm.getPosition(3)
    move([[3, pos - amount]], speed)
    print("moved wrist down", amount)



def rotate_wrist_left(amount=200, speed=MOVE_TIME):
    pos = arm.getPosition(2)
    move([[2, pos + amount]], speed)
    print("rotated wrist left", amount)

def rotate_wrist_right(amount=200, speed=MOVE_TIME):
    pos = arm.getPosition(2)
    move([[2, pos - amount]], speed)
    print("rotated wrist right", amount)



def close_gripper(speed=MOVE_TIME):
    move([[1, 1000]], speed)
    print("closed gripper")

def open_gripper(speed=MOVE_TIME):
    move([[1, 0]], speed)
    print("opened gripper")



def relax():
    """turn off all servos to move arm by hand"""
    for i in range(1, 7):
        arm.servoOff(i)


def read_all_positions():
    """print current position of all servos"""
    for i in range(1, 7):
        sleep(0.1)
        print(f"Servo {i}: {arm.getPosition(i)}")


def test_all_servos():
    """move all the servos back and forth for testing"""
    rotate_base_left()
    rotate_base_right()
    shoulder_up() 
    shoulder_down()
    elbow_up()
    elbow_down()
    wrist_up()
    wrist_down()
    rotate_wrist_left()
    rotate_wrist_right()
    close_gripper()
    open_gripper()




# HOLD BASE DOWN or it may go flying

stand_straight()
