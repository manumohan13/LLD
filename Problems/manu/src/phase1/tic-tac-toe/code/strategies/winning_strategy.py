from abc import ABC, abstractmethod
from enitites.board import Board
from enums.symbol import Symbol

class WinningStrategy(ABC):
    @abstractmethod
    def check_winner(self, board: Board, symbol: Symbol) -> bool:
        pass

    @abstractmethod
    def record_move(self, row: int, col: int, symbol: Symbol):
        pass