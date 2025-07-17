from strategies.winning_strategy import WinningStrategy
from enitites.board import Board

from enums.symbol import Symbol

from typing import Dict, List

class OptimizedWinningStrategy(WinningStrategy):
    def __init__(self, board_size: int):
        self.board_size = board_size
        self.rows: Dict[str, List[int]] = {}
        self.cols: Dict[str, List[int]] = {}
        self.diag: Dict[str, List[int]] = {}
        self.anti_diag: Dict[str, List[int]] = {}
        self.latest_move: Dict[str, tuple[int, int]] = {}

    
    def record_move(self, row: int, col: int, symbol: Symbol):

        key = symbol.value

        if key not in self.rows:
            self.rows[key] = [0] * self.board_size
            self.cols[key] = [0] * self.board_size
            self.diag[key] = 0
            self.anti_diag[key] = 0

        self.rows[key][row] += 1
        self.cols[key][col] += 1

        # Diagonal
        if row == col:
            self.diag[key] += 1

        # Anti Diagonal
        if row + col == self.board_size - 1:
            self.anti_diag[key] += 1

        self.latest_move[key] = (row, col)

        
    def check_winner(self, board: Board, symbol: Symbol):
        
        key = symbol.value
        if key not in self.latest_move:
            return False
        
        row, col = self.latest_move[key]

        return (
            self.rows[key][row] == self.board_size or
            self.cols[key][col] == self.board_size or 
            self.diag[key] == self.board_size or 
            self.anti_diag[key] == self.board_size
        )