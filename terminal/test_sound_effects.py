import time
from itertools import cycle

import SoundEffects


def mainloop():
    try_again_itr = cycle(SoundEffects.try_again)
    boundary_select_itr = cycle(SoundEffects.boundary_selection)
    while True:
        SoundEffects.play_sound(next(try_again_itr))
        SoundEffects.play_sound(next(boundary_select_itr))


def main():
    mainloop()


if __name__ == "__main__":
    main()
