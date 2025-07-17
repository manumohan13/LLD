from enitites.game import Game
from enitites.player import Player

from enums.symbol import Symbol

from strategies.default_winning_strategy import DefaultWinningStrategy
from strategies.optimized_winning_strategy import OptimizedWinningStrategy

from controllers.game_controller import GameController


def main():
    p1 = Player("Alice", Symbol.X)
    p2 = Player("Bob", Symbol.O)
    # strategy = DefaultWinningStrategy()
    strategy = OptimizedWinningStrategy(board_size=3)

    game = Game(board_size=3, player1=p1, player2=p2, winning_strategy=strategy)
    controller = GameController(game)
    controller.start()


if __name__ == "__main__":
    main()