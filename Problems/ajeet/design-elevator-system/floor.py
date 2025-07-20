from external_button import ExternalButton
from direction import Direction

class Floor:
    def __init__(self, level):
        self.level = level
        self.external_button = ExternalButton()
    
    def press(self, dir:Direction):
        print(self.level,dir)
        self.external_button.press_button(self.level,dir)