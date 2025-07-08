# Write your code here :-)
print('Code starteds')
import RPi.GPIO as GPIO
import webcam
from time import sleep
import motor
import joystick
import cv2
import data
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

print('Enteirng Loop')
val = 0
flagF = False
flagS = False
flagShare = False
motor1 = motor.Motor(2,3,4,17,6,13,19,26)


while True:


    xbuttstate = joystick.buttX()
    lstk = joystick.buttlstk()
    obuttstate = joystick.buttO()
    shareButtonState = joystick.buttShare()
    if shareButtonState ==1 and flagShare == False:
        img = webcam.getImg(False, size=[240,120])
        data.saveData(img, lstk)
        flagShare = True
    elif shareButtonState ==1 and flagShare == True:
        data.saveLog()
        flagShare =False

    if xbuttstate!=0:
        print('x')
        motor1.moveFwd(flagF)
        if lstk <0:

            motor1.turnRight(lstk)
        elif lstk>0:
            print("Left Bruh")
            motor1.turnLeft(lstk)
        flagF = True
        flagS = True


    elif obuttstate!=0:
        motor1.moveRev(flagF)
        if lstk <0:

            motor1.turnRight(lstk)
        elif lstk>0:
            print("Left Bruh")
            motor1.turnLeft(lstk)
        flagF = True
        flagS = True

    elif lstk>0:
        motor1.rotateRight(lstk)

    elif lstk<0:
        motor1.rotateLeft(lstk)

    else:
        motor1.stop(flagS)

        flagS=False
        flagF=False
    cv2.waitKey(1)