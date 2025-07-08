
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Motor():

    def __init__(self,R_L_EN, R_R_EN, R_L_PWM, R_R_PWM,L_L_EN, L_R_EN, L_L_PWM, L_R_PWM,speed =20):
        self.speed=speed
        self.R_L_EN = R_L_EN
        self.R_R_EN = R_R_EN
        self.R_L_PWM = R_L_PWM
        self.R_R_PWM = R_R_PWM
        self.L_L_EN = L_L_EN
        self.L_R_EN = L_R_EN
        self.L_L_PWM = L_L_PWM
        self.L_R_PWM = L_R_PWM
        GPIO.setup(self.R_L_EN,GPIO.OUT)
        GPIO.setup(self.R_R_EN,GPIO.OUT)
        GPIO.setup(self.R_L_PWM,GPIO.OUT)
        GPIO.setup(self.R_R_PWM,GPIO.OUT)
        GPIO.setup(self.L_L_EN,GPIO.OUT)
        GPIO.setup(self.L_R_EN,GPIO.OUT)
        GPIO.setup(self.L_L_PWM,GPIO.OUT)
        GPIO.setup(self.L_R_PWM,GPIO.OUT)
        GPIO.output(self.R_L_EN,GPIO.HIGH)
        GPIO.output(self.L_L_EN,GPIO.HIGH)
        GPIO.output(self.R_R_EN,GPIO.HIGH)
        GPIO.output(self.L_R_EN,GPIO.HIGH)
        self.pwmLM_L = GPIO.PWM(self.L_L_PWM, 100);
        self.pwmLM_L.start(0);
        self.pwmLM_R = GPIO.PWM(self.L_R_PWM, 100);
        self.pwmLM_R.start(0);
        self.pwmRM_L = GPIO.PWM(self.R_L_PWM, 100);
        self.pwmRM_L.start(0);
        self.pwmRM_R = GPIO.PWM(self.R_R_PWM, 100);
        self.pwmRM_R.start(0);


    def moveFwd(self,flagF):
        if flagF == False:

            for i in range(0,self.speed,10):
                self.pwmLM_R.ChangeDutyCycle(i)
                self.pwmLM_L.ChangeDutyCycle(0)
                self.pwmRM_R.ChangeDutyCycle(i)
                self.pwmRM_L.ChangeDutyCycle(0)
                sleep(0.2)
            FlagF=True
        else:
            self.pwmRM_R.ChangeDutyCycle(self.speed)
            self.pwmRM_L.ChangeDutyCycle(0)
            self.pwmLM_L.ChangeDutyCycle(0)
            self.pwmLM_R.ChangeDutyCycle(self.speed)


    def stop(self, flagS):

        if flagS == True:

            for i in range(self.speed,-1,-10):
                self.pwmLM_R.ChangeDutyCycle(i)
                self.pwmLM_L.ChangeDutyCycle(0)
                self.pwmRM_R.ChangeDutyCycle(i)
                self.pwmRM_L.ChangeDutyCycle(0)
                sleep(0.2)
        else:
            self.pwmRM_L.ChangeDutyCycle(0)
            self.pwmRM_R.ChangeDutyCycle(0)
            self.pwmLM_L.ChangeDutyCycle(0)
            self.pwmLM_R.ChangeDutyCycle(0)
    def turnRight(self, power):
        high = self.speed
        pwmVal = high - (abs(power)*high/2)
        self.pwmRM_R.ChangeDutyCycle(high+20)
        self.pwmLM_R.ChangeDutyCycle(pwmVal)
    def turnLeft(self, power):
        high = self.speed
        pwmVal = high - (abs(power)*high/2)
        self.pwmLM_R.ChangeDutyCycle(high+20)
        self.pwmRM_R.ChangeDutyCycle(pwmVal)

    def moveRev(self,flagF):
        if flagF == False:

            for i in range(0,self.speed,10):
                self.pwmLM_R.ChangeDutyCycle(0)
                self.pwmLM_L.ChangeDutyCycle(i)
                self.pwmRM_R.ChangeDutyCycle(0)
                self.pwmRM_L.ChangeDutyCycle(i)
                sleep(0.2)
            FlagF=True
        else:
            self.pwmRM_R.ChangeDutyCycle(0)
            self.pwmRM_L.ChangeDutyCycle(self.speed)
            self.pwmLM_L.ChangeDutyCycle(self.speed)
            self.pwmLM_R.ChangeDutyCycle(0)


    def rotateRight(self, power):
        high = 20
        pwmVal = (abs(power)*high)
        self.pwmLM_R.ChangeDutyCycle(pwmVal)
        self.pwmRM_L.ChangeDutyCycle(pwmVal)
    def rotateLeft(self, power):
        high = 20
        pwmVal = (abs(power)*high)
        self.pwmRM_R.ChangeDutyCycle(pwmVal)
        self.pwmLM_L.ChangeDutyCycle(pwmVal)





