from elevator_car import ElevatorCar
from typing import List
from direction import Direction
import heapq

class ElevatorController :
    def __init__(self, elevator_car:ElevatorCar):
        self.elevator_car = elevator_car
        self.min_heap=[]
        self.max_heap = []
        self.pending_request :List[int] = []


    def submit_internal_button_request(self, floor_level, direction):
        if direction == Direction.UP:
            heapq.heappush(self.min_heap, floor_level)
        else:
            heapq.heappush(self.max_heap, -floor_level)
        self.control()

    def submit_external_buttom_request(self, floor_level, direction:Direction):
        print(floor_level,direction)
        if direction == Direction.UP and self.elevator_car.direction == Direction.UP and  self.elevator_car.curr_floor < floor_level:
                heapq.heappush(self.min_heap,floor_level)
        elif direction == Direction.UP and self.elevator_car.direction == Direction.UP and self.elevator_car.curr_floor >= floor_level:
                self.pending_request.append(floor_level)
        elif direction == Direction.DOWN and self.elevator_car.direction == Direction.DOWN and self.elevator_car.curr_floor > floor_level:
                heapq.heappush(self.max_heap, -floor_level)
        elif direction == Direction.DOWN and self.elevator_car.direction == Direction.DOWN and self.elevator_car.curr_floor <= floor_level:
                self.pending_request.append(floor_level)
        
        self.control()


    def control(self):
          while True:
                if self.elevator_car.direction == Direction.UP:
                    while self.min_heap:
                          floor_level = heapq.heappop(self.min_heap)
                          self._move_to_floor(floor_level, Direction.UP)
                    for floor_level in self.pending_request:
                        heapq.heappush(self.min_heap, floor_level)
                    self.elevator_car.direction = Direction.DOWN
                else:
                    while self.max_heap:
                          floor_level = -heapq.heappop(self.max_heap)
                          self._move_to_floor(floor_level,Direction.DOWN )
                    for floor_level in self.pending_request:
                         heapq.heappush(self.max_heap, -floor_level)
                    self.elevator_car.direction = Direction.UP

    def _move_to_floor(self,floor_level, dir):
          self.elevator_car.move(floor_level, dir)



