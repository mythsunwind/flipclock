import RPi.GPIO as GPIO
from gpiozero import Motor
from time import sleep

pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
motor = Motor(26, 19)


def rotate(time):
    motor.forward(0.9)
    sleep(time)
    motor.stop()


def get_state():

    pin_state = GPIO.input(pin)
    if pin_state == False:
        print("AM")
        return "AM"
    else:
        print("PM")
        return "PM"
