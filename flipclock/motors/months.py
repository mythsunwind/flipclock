import RPi.GPIO as GPIO
from gpiozero import Motor
from time import sleep

def rotate():
    motor = Motor(26, 19)
    motor.forward(0.5)
    sleep(4.5)
    motor.stop()

def get_state():
    GPIO.setmode(GPIO.BCM)
    input1 = 24
    input2 = 25
    GPIO.setup(input1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(input2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    input1_state = GPIO.input(input1)
    input2_state = GPIO.input(input2)
    if input1_state == False:
        return 1
    elif input2_state == False:
        return 2
    else:
        return 0

#MONTHS_NAME = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUL', 'JUN', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
#MONTHS_STAT = [0, 2, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0]
