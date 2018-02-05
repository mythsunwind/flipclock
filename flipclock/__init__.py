from . import motors
from time import sleep

def set_meridian(expected):
    if(motors.meridian.get_state() != expected):
        while motors.meridian.get_state() != expected:
            motors.meridian.rotate(2)
        motors.meridian.rotate(1)

def rotate_days():
    motors.days.rotate(2.5)

def set_day(expected):
    rotate_days()
    if(motors.days.get_state() != expected):
        while expected not in motors.days.get_state():
            sleep(2)
            rotate_days()
