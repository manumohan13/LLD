from enitites.game import Game
from enums.game_status import GameStatus

class GameController:
    def __init__(self, game: Game):
        self.game = game

    def start(self):
        self.print_board()

        while self.game.status == GameStatus.IN_PROGRESS:
            player = self.game.get_current_player()
            print(f"{player.name}'s turn ({player.symbol.value}): ")

            try:
                row, col = self.get_move_input()
                self.game.make_move(row, col)
            except(ValueError, IndexError) as e:
                print(f"Invalid move: {e}")
                continue

            if self.game.check_winner():
                self.game.status = GameStatus.WON
                self.game.winner = player
                break

            if self.game.check_draw():
                self.game.status = GameStatus.DRAW
                break

            self.game.switch_turn()
            self.print_board()

        self.print_result()

    
    def print_board(self):
        self.game.board.print_board()

    def get_move_input(self):
        while True:
            try:
                row = int(input("Enter row: "))
                col = int(input ("Enter column: "))

                if not (0 <= row < self.game.board.size) or not (0 <= col < self.game.board.size):
                    raise ValueError("Row and column must be within board size")
                
                return row, col

            except ValueError as e:
                print(f"Invalid input: {e}, Please try again.")

    def print_result(self):
        if self.game.status == GameStatus.WON:
            print(f" {self.game.winner.name } wins!")
        elif self.game.status == GameStatus.DRAW:
            print("It is a draw! ")