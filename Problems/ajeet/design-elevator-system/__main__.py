from building import Building
from floor import Floor
from direction import Direction
from elevator_creator import ElevatorCreator

if __name__ == "__main__":
    building = Building()

    floor_1 = Floor(1)
    floor_2 = Floor(2)
    floor_3 = Floor(3)
    floor_4 = Floor(4)
    floor_5 = Floor(5)

    building.add_floor(floor_1)
    building.add_floor(floor_2)
    building.add_floor(floor_3)
    building.add_floor(floor_4)
    building.add_floor(floor_5)

    ElevatorCreator.create()
    floor_5.press(Direction.UP)
