#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [2, 3, 4, 17, 27, 22, 10, 9]


for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)  # Turn all relays off.

try:
    for pin in pinList:
        GPIO.output(pin, GPIO.LOW)
        time.sleep(1)
    GPIO.cleanup()
    print("finished.")

# End program cleanly with keyboard
except KeyboardInterrupt:
    print("complete")

    # Reset GPIO settings
    GPIO.cleanup()
