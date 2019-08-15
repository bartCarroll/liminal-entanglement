import os
import random
import threading

from playsound import playsound


def rsrc(n):
    return os.path.join(os.path.dirname(__file__), n)


speaker_lock = threading.Lock()

# Boundary Selection
select_boundary1 = rsrc("sounds/select_boundary1.mp3")
select_boundary2 = rsrc("sounds/select_boundary2.mp3")
boundary_selection = [select_boundary1, select_boundary2]

# Try Again
try_again1 = rsrc("sounds/try_again.mp3")
boundary_beyond_try_again = rsrc("sounds/boundary_beyond_try_again.mp3")
try_again = [try_again1, boundary_beyond_try_again]

type_your_boundary = rsrc("sounds/type_your_boundary.mp3")
type_your_answer = rsrc("sounds/type_your_answer1.mp3")


def play_random_try_again():
    t = threading.Thread(target=play_sound, args=(random.choice(try_again), ))
    t.start()


def play_random_boundary_selection():
    t = threading.Thread(target=play_sound, args=(random.choice(boundary_selection), ))
    t.start()


def play_type_your_boundary():
    play_sound(type_your_boundary)


def play_type_your_answer():
    play_sound(type_your_answer)


def play_sound(the_sound):
    with speaker_lock:
        playsound(the_sound)

