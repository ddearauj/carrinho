import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class Motor:
    'The motor class, will control on/off status'

    on = False
    PIN_NUMBER = 18
    GPIO.setup(PIN_NUMBER, GPIO.OUT)

    GPIO.setwarnings(False)

    def __init__(self):
        self.on = False

    def turnOn(self):
        GPIO.output(self.PIN_NUMBER, GPIO.HIGH)
        self.on = True

    def turnOff(self):
        GPIO.output(self.PIN_NUMBER, GPIO.LOW)
        self.on = False


    def controller(self):
        command = ''
        command = input("Type in the motor command ")
        if (command == 'on'):
            if(self.on):
                print("Motor is already running")
            else:
                self.turnOn()
        if (command == "off"):
            if(self.on):
                self.turnOff()
            else:
                print("Motor is already off")
