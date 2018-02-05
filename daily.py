#!/bin/python3
"""
Flipclock
"""
from datetime import datetime
from time import sleep
import flipclock

def current_time():
    now = datetime.now()
    print('{d:%b}'.format(d=now))
    print('{d.day}'.format(d=now))
    print('{d:%a} {d:%p}'.format(d=now))

def current_day():
    now = datetime.now()
    return now.day
 
def current_meridian():
    now = datetime.now()
    return '{d:%p}'.format(d=now)

if __name__ == '__main__':
    flipclock.set_day(current_day())
    sleep(2)
    flipclock.set_meridian(current_meridian())
