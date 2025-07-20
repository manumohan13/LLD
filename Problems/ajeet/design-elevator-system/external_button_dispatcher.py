from typing import List
from elevator_creator import ElevatorCreator

class ExternalButtonDispatcher:
    def dispatch(self, floor_level, dir):
        elevator_controller = ElevatorCreator.elevator_controller_list[0]
        elevator_controller.submit_external_buttom_request(floor_level, dir)