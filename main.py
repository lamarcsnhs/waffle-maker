from GmailAPI import gmail as g
import RPi.GPIO as GPIO
import makerElectronics as me
import time

if __name__=='__main__':
    try:
        # while True:
            # print(g.checkMail())

        me.spinMotor("left",37,1)
        time.sleep(1)
        me.spinMotor("right",31,1)
    except KeyboardInterrupt:
        pass
    finally:
        me.pwm.stop()
        GPIO.cleanup()


        