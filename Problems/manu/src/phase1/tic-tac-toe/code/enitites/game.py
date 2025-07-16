from .board import Board
from enitites.player import Player

from enums.symbol import Symbol
from enums.game_status import GameStatus

from typing import List, Optional

class Game:
    def __init__(self, board_size: int, player1: Player, player2: Player):
        self.board = Board(board_size)
        self.players: List[Player] = [player1, player2]
        self.current_player_index = 0
        self.status = GameStatus.IN_PROGRESS
        self.winner: Optional[Player] = None

    
    def get_current_player(self) -> Player:
        return self.players[self.current_player_index]
    
    def switch_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def make_move(self, row: int, col: int):
        cell = self.board.grid[row][col]
        if not cell.is_empty():
            raise ValueError("Cell is already filled")
        
        current_symbol = self.get_current_player().symbol
        cell.mark(current_symbol)

    def check_draw(self) -> bool:
        for row in self.board.grid:
            for cell in row:
                if cell.is_empty():
                    return False

        return True
    
    def check_winner(self) -> bool:
        symbol = self.get_current_player().symbol
        size = self.board.size
        grid = self.board.grid

        for row in grid:

            # Check rows
            if all(cell.symbol == symbol for cell in row):
                return True

            # check columns
            for col in range(size):
                if all(grid[row][col].symbol == symbol for row in range(size)):
                    return True

            # Check diagonal    
            if all(grid[i][i].symbol == symbol for i in range(size)):
                return True
            
            # Check anti-diagonal
            if all(grid[i][size - 1 - i].symbol == symbol for i in range(size)):
                return True
            
            return False
            


