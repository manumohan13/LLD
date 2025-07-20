from floor import Floor
from typing import List
from elevator_controller import ElevatorController
from elevator_car import ElevatorCar
class Building:
    
    def __init__(self):
        self.floor_list:List[Floor] = []
        self.floor_count = 0

    def add_floor(self, floor:Floor):
        self.floor_list.append(Floor)


