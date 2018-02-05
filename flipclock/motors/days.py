import RPi.GPIO as GPIO
from gpiozero import Motor
from time import sleep

pin1 = 12
pin2 = 7
pin3 = 8
pin4 = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

motor = Motor(27, 17)

def rotate(time):
    motor.forward(1)
    sleep(time)
    motor.stop()

def get_state():
    pin1_state = GPIO.input(pin1)
    pin2_state = GPIO.input(pin2)
    pin3_state = GPIO.input(pin3)
    pin4_state = GPIO.input(pin4)
    if pin1_state == False:
        return [31]
    elif pin2_state == False:
        return [29, 30]
    elif pin3_state == False:
        return [1]
    elif pin4_state == False:
        return [2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                12, 13, 14, 15, 16, 17, 18, 19,
                20, 21, 22, 23, 24, 25, 26]
    else:
        return [27, 28]
