from GmailAPI import gmail as g
import RPi.GPIO as GPIO
import makerElectronics as me
import time
import threading
from wafflesList import waffle_list

# coffee maker code makes 0 sense

"""
Process:
1. Check for new orders
2. Parse orders
3. Make sure waffle iron is rotated correctly 
4. open waffle iron with linear actuator
5. Pour ingredients into waffle iron
6. Close waffle iron
7. Wait for waffle to cook
8. Open waffle iron with linear actuator
9. rotate the bottom iron with motor to drop the waffle

"""

orders = []

def CheckForOrder():
    aOrder = g.checkMail()
    # thisOrder

def orderThread():
    while True:
        o = CheckForOrder()
        print(o)
        orders.append(o)
        print(orders)

if __name__=='__main__':
    try:
        gettingOrders = threading.Thread(target=orderThread)
        gettingOrders.start()

        while True:
            time.sleep(5)

            print(g.checkMail())

        # me.spinMotor("left",37,1)
        # time.sleep(1)
        # me.spinMotor("right",31,1)
    except KeyboardInterrupt:
        pass
    finally:
        me.pwm.stop()
        GPIO.cleanup()



        