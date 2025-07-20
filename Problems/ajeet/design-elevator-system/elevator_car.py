from internal_button import InternalButton
from door import Door
from display import Display
from direction import Direction

class ElevatorCar:
    def __init__(self):
        self.door = Door()
        self.internal_button = InternalButton()
        self.display = Display()
        self.direction  = Direction.UP
        self.curr_floor = 0

    def move(self, target_floor:int, direction:Direction):
        print(self.display)
        if direction == Direction.UP:
            for floor in range(self.curr_floor+1, target_floor+1):
                self.curr_floor = floor
                self.direction = direction
                self.display.set_display(floor, self.direction)
                print(self.display)
                
        else :
            for floor in range(self.curr_floor-1, target_floor-1, -1):
                self.curr_floor = floor
                self.direction = direction
                self.display.set_display(self.curr_floor, self.direction)
                print(self.display)
            
    def press_internal_button(self,target_floor:int):
        self.internal_button.press(self, self.direction, target_floor)

