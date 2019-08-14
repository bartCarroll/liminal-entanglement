import keyboard

import Effects


class InteractionManager:
    def __init__(self, disp):
        self.display = disp

    def get_user_input(self, text):
        Effects.scroll_text(self.display, text)
        Effects.display_text(self.display, '???', font=Effects.BigFont)
        cat_events = keyboard.record(until="enter")
        return next(keyboard.get_typed_strings(cat_events))

    def scroll_text(self, text):
        Effects.scroll_text(self.display, text)


