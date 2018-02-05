#!/bin/python3
"""
Flipclock
"""
from datetime import datetime
import flipclock

def current_meridian():
    now = datetime.now()
    return '{d:%p}'.format(d=now)

if __name__ == '__main__':
    flipclock.set_meridian(current_meridian())
