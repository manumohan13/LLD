from typing import List
from direction import Direction
from external_button_dispatcher import ExternalButtonDispatcher

class ExternalButton:
    def __init__(self):
        self.dispatcher  =  ExternalButtonDispatcher()

    def press_button(self, floor_level:int, dir:Direction):
        self.dispatcher.dispatch(floor_level, dir)
            
