#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [2, 3, 4, 17, 27, 22, 10, 9]

UNLOCK_TIME = 30

GPIO_PINS = {
    'door_lock': 2,
    'lights_1': 3,
    'lights_2': 4
}

# Turn all relays off.
for i in pinList:
    # Set all GPIO Pints to Output
    GPIO.setup(i, GPIO.OUT)
    # Set all relays to open
    GPIO.output(i, GPIO.HIGH)


def unlock_door():
    GPIO.output(GPIO_PINS['door_lock'])
    GPIO.output(GPIO_PINS['lights_1'])
    GPIO.output(GPIO_PINS['lights_2'])
    time.sleep(UNLOCK_TIME)
