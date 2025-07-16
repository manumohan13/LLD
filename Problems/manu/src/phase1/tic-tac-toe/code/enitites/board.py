from typing import List
from .cell import Cell

class Board:
    def __init__(self, size=3):

        if size < 3:
            raise ValueError("Board size must be atleast 3")
        
        self.size = size
        self.grid: List[List[Cell]] = []
        self.initalize_row()

    def initalize_row(self):
        self.grid = []
        for row in range(self.size):
            row_cells = []
            for col in range(self.size):
                row_cells.append(Cell(row, col))
            self.grid.append(row_cells)

    def reset_board(self):
        for row in self.grid:
            for cell in row:
                cell.clear()


    def print_board(self):
        for row in self.grid:
            print(" ".join(str(cell) for cell in row))
        print()