# from GmailAPI import gmail as g
# import RPi.GPIO as GPIO
# import makerElectronics as me
import time
import orderParser as op

if __name__=='__main__':
    try:
        # while True:
        #     print(g.checkMail())
        print(op.parse_order("Waffle"))

    except KeyboardInterrupt:
        exit


        