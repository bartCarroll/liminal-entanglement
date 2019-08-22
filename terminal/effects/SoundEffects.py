import os
import random
import pygame


#pygame.init()
pygame.mixer.init()

def rsrc(n):
    return os.path.join(os.path.dirname(__file__), n)

categories = {
    'love': pygame.mixer.Sound(rsrc("sounds/love.ogg")),
    'death': pygame.mixer.Sound(rsrc("sounds/death.ogg")),
    'time': pygame.mixer.Sound(rsrc("sounds/time.ogg")),
    'space': pygame.mixer.Sound(rsrc("sounds/space.ogg")),
    'life': pygame.mixer.Sound(rsrc("sounds/life.ogg"))
}

# Boundary Selection
select_boundary1 = pygame.mixer.Sound(rsrc("sounds/select_boundary1.ogg"))
select_boundary2 = pygame.mixer.Sound(rsrc("sounds/select_boundary2.ogg"))
boundary_selection = [select_boundary1, select_boundary2]

# Try Again
try_again1 = pygame.mixer.Sound(rsrc("sounds/try_again.ogg"))
boundary_beyond_try_again = pygame.mixer.Sound(rsrc("sounds/boundary_beyond_try_again.ogg"))
try_again = [try_again1, boundary_beyond_try_again]

type_your_boundary = pygame.mixer.Sound(rsrc("sounds/type_your_boundary.ogg"))
type_your_answer = pygame.mixer.Sound(rsrc("sounds/type_your_answer1.ogg"))

# Idle Sounds
crystal_bowls1 = rsrc("sounds/crystal_bowls1.ogg")
crystal_bowls1 = rsrc("sounds/crystal_bowls1.ogg")
weird_bubbles = rsrc("sounds/weird_bubbles.ogg")
idle_sounds = [crystal_bowls1, crystal_bowls1, weird_bubbles]


def play_random_try_again():
    random.choice(try_again)


def play_random_boundary_selection():
    random.choice(boundary_selection).play()


def play_type_your_boundary():
    type_your_boundary.play()


def play_type_your_answer():
    type_your_answer.play()


def play_random_idle_sound():
    s = pygame.mixer.Sound(random.choice(idle_sounds))
    s.play()




