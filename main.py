from GmailAPI import gmail as g
import RPi.GPIO as GPIO
import makerElectronics as me

if __name__=='__main__':
    try:
        while True:
            print(g.checkMail())
    except KeyboardInterrupt:
        pass
    finally:
        me.pwm.stop()
        GPIO.cleanup()