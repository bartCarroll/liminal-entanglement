import os
import random
import pygame


def rsrc(n):
    return os.path.join(os.path.dirname(__file__), n)


# Boundary Selection
select_boundary1 = pygame.mixer.Sound(rsrc("sounds/select_boundary1.ogg"))
select_boundary2 = pygame.mixer.Sound(rsrc("sounds/select_boundary2.ogg"))
boundary_selection = [select_boundary1, select_boundary2]

# Try Again
try_again1 = pygame.mixer.Sound(rsrc("sounds/try_again.mp3"))
boundary_beyond_try_again = pygame.mixer.Sound(rsrc("sounds/boundary_beyond_try_again.ogg"))
try_again = [try_again1, boundary_beyond_try_again]

type_your_boundary = pygame.mixer.Sound(rsrc("sounds/type_your_boundary.ogg"))
type_your_answer = pygame.mixer.Sound(rsrc("sounds/type_your_answer1.ogg"))


def play_random_try_again():
    random.choice(try_again)


def play_random_boundary_selection():
    random.choice(boundary_selection).play()


def play_type_your_boundary():
    type_your_boundary.play()


def play_type_your_answer():
    type_your_answer.play()



