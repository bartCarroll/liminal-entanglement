#! /usr/bin/env python

import time

from effects import Effects
from flipdot import client, display


d = display.Display(28, 14,
                    panels={
                        2: ((0, 0), (28, 7)),
                        1: ((0, 7), (28, 7)),
                    })


def transition(d):
    Effects.rand(d)


def mainloop(d):
    # Effects.heart(d)
    # Effects.dot(d)
    # time.sleep(0.5)
    Effects.big_hypno(d)
    Effects.crazy_blocks(d)
    #Effects.crazy_blocks(d)
    #animations.blink_text(d, "Hello")
    #animations.scroll_text(d, "The quick brown fox jumped over the lazy dog.")
    #animations.scroll_text(d, "THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG.", font=animations.SmallFont)
    # transition(d)

    Effects.hypno_squares(d)
    time.sleep(1)


def main():
    d.connect(client.UDPClient("127.0.0.1", 9999))

    try:
        # intro(d)
        while True:
            mainloop(d)
    finally:
        d.disconnect()


if __name__ == "__main__":
    main()
