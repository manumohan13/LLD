from internal_button_dispatcher import InternalButtonDispatcher

class InternalButton :
        def __init__(self):
                self.dispatcher = InternalButtonDispatcher()
                self.floor_level_list = [1,2,3,4,5]

        def press(self,elevator_car,  target_floor:int):
                self.dispatcher.dispatch(elevator_car , target_floor)
                
