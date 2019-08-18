import time
from itertools import cycle

from effects import SoundEffects


def mainloop():
    try_again_itr = cycle(SoundEffects.try_again)
    boundary_select_itr = cycle(SoundEffects.boundary_selection)
    while True:
        next(try_again_itr).play()
        time.sleep(5)
        next(boundary_select_itr).play()
        time.sleep(5)


def main():
    mainloop()


if __name__ == "__main__":
    main()
