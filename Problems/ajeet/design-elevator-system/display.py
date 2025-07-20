from direction import Direction


class Display:
    def __init__(self):
        self.level = 0
        self.direction : Direction  = None

    def set_display (self, level:int, dir: Direction):
        self.level = level
        self.direction = dir

    def __str__(self):
        return f"floor level : {self.level} , direction : {self.direction}"
