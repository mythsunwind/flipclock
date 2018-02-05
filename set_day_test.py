#!/bin/python3
"""
Flipclock
"""
from datetime import datetime
from time import sleep
import flipclock

def current_day():
    now = datetime.now()
    return now.day

if __name__ == '__main__':
    flipclock.set_day(current_day())
 
