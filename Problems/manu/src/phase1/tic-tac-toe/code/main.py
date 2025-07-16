from enitites.game import Game
from enitites.player import Player

from enums.symbol import Symbol

from controllers.game_controller import GameController


def main():
    p1 = Player("Alice", Symbol.X)
    p2 = Player("Bob", Symbol.O)

    game = Game(board_size=3, player1=p1, player2=p2)
    controller = GameController(game)
    controller.start()


if __name__ == "__main__":
    main()