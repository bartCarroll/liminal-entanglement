import time
from itertools import cycle

import pygame

from effects import SoundEffects


def mainloop():
    for sound in SoundEffects.idle_sounds:
        s = pygame.mixer.Sound(sound)
        s.play()
        time.sleep(5)
        SoundEffects.fadeout(2000)
        time.sleep(2)

def main():
    mainloop()


if __name__ == "__main__":
    main()
