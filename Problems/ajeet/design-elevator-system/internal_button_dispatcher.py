from typing import List
from elevator_creator import ElevatorCreator

class InternalButtonDispatcher:
    def dispatch(self, elevator_car , floor_level :int):
        elevator_controller = ElevatorCreator.elevator_controller_list[0]
        elevator_controller.submit_internal_button_request(elevator_car.diection , floor_level)