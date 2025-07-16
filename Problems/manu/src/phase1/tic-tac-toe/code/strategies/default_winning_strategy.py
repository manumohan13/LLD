from strategies.winning_strategy import WinningStrategy
from enitites.board import Board
from enums.symbol import Symbol

class DefaultWinningStrategy(WinningStrategy):
    def check_winner(self, board: Board, symbol: Symbol) -> bool:

        size = board.size
        grid = board.grid

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
    
    def record_move(self, row: int, col: int, symbol: Symbol):
        pass