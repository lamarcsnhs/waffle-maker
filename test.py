from GmailAPI import gmail as g
# import RPi.GPIO as GPIO
# import makerElectronics as me
import time

if __name__=='__main__':
    try:
        while True:
            print(g.checkMail())

    except KeyboardInterrupt:
        exit


        