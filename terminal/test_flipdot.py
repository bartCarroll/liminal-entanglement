#! /usr/bin/env python

import time

from effects import DisplayEffects
from flipdot import client, display
from itertools import cycle

d = display.Display(28, 14,
                    panels={
                        2: ((0, 0), (28, 7)),
                        1: ((0, 7), (28, 7)),
                    })


def transition(d):
    DisplayEffects.random_transition(d)


def mainloop(d):
    transitions_iter = cycle(DisplayEffects.transitions)
    images_iter = cycle(DisplayEffects.static_images)
    while True:
        #next(transitions_iter)(d)
        #time.sleep(1)
        #next(images_iter)(d)
        DisplayEffects.display_burning_man(d)
        time.sleep(3)


def main():
    d.connect(client.UDPClient("127.0.0.1", 9999))

    try:
        mainloop(d)
    finally:
        d.disconnect()


if __name__ == "__main__":
    main()
