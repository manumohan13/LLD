


class ElevatorCreator:
    elevator_controller_list = []

    def create():
        from elevator_car import ElevatorCar
        from elevator_controller import ElevatorController
        elevator_car = ElevatorCar()
        elevator_car_contoller = ElevatorController(elevator_car)
        ElevatorCreator.elevator_controller_list.append(elevator_car_contoller)