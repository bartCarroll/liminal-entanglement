import time

import keyboard

from effects import DisplayEffects
from effects import SoundEffects


class InteractionManager:
    def __init__(self, disp):
        self.display = disp

    def get_boundary_selection(self, categories):
        if not categories or len(categories) == 0:
            return ""
        for i, cat in categories.items():
            SoundEffects.categories[cat['name']].play()
            DisplayEffects.scroll_text(self.display, "{0}. {1} ".format(i, cat['display']))
        SoundEffects.play_type_your_boundary()
        DisplayEffects.display_text(self.display, '???', font=DisplayEffects.BigFont)
        cat_events = keyboard.record(until="enter")
        return next(keyboard.get_typed_strings(cat_events))

    def get_question_response(self, question):
        if not question:
            return ""
        DisplayEffects.scroll_text(self.display, question)
        SoundEffects.play_type_your_answer()
        DisplayEffects.display_text(self.display, '???', font=DisplayEffects.BigFont)
        answer_events = keyboard.record(until="enter")
        return next(keyboard.get_typed_strings(answer_events))

    def scroll_text(self, text):
        DisplayEffects.scroll_text(self.display, text)

    def try_again(self):
        SoundEffects.play_random_try_again()
        DisplayEffects.display_try_again(self.display)
        time.sleep(5)

    def select_boundary(self):
        SoundEffects.play_random_boundary_selection()
        self.scroll_text("Select Your Boundary...")
        DisplayEffects.random_transition(self.display)

    def play_random_idle_sound(self):
        SoundEffects.play_random_idle_sound()

    def random_display_transition(self):
        DisplayEffects.random_transition(self.display)

    def display_random_image(self):
        DisplayEffects.display_random_image(self.display)

    def fadeout_sound(self):
        SoundEffects.fadeout(2000)
        time.sleep(2)






