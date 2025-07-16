from .board import Board

class Game:
    def run_game(self):
        board = Board(3)

        print("Initial empty board:")
        board.print_board()

        print("Marking some cells")
        board.grid[0][0].mark("X")
        board.grid[1][1].mark("O")
        board.grid[2][2].mark("X")
        board.print_board()

        print("Trying to mark an already filled cell:")
        try:
            board.grid[0][0].mark("O")
        except ValueError as e:
            print(f"Expected error: {e}")

        print("Clearing the board:")
        board.reset_board()
        board.print_board()