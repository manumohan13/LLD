from door_status import DoorStatus

class Door:
    def __init__(self):
        self.status : DoorStatus = None
    
    def open(self):
        self.status = DoorStatus.OPEN
    
    def close(self):
        self.status  = DoorStatus.CLOSE


