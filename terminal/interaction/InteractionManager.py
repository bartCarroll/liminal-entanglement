import time

import keyboard

import DisplayEffects
import SoundEffects


class InteractionManager:
    def __init__(self, disp):
        self.display = disp

    def get_boundary_selection(self, categories):
        if not categories or len(categories) == 0:
            return ""
        DisplayEffects.scroll_text(self.display, categories)
        DisplayEffects.display_text(self.display, '???', font=DisplayEffects.BigFont)
        SoundEffects.play_type_your_boundary()
        cat_events = keyboard.record(until="enter")
        return next(keyboard.get_typed_strings(cat_events))

    def get_question_response(self, question):
        if not question:
            return ""
        DisplayEffects.scroll_text(self.display, question)
        DisplayEffects.display_text(self.display, '???', font=DisplayEffects.BigFont)
        SoundEffects.play_type_your_answer()
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




