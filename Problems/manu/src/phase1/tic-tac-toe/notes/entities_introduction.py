"""
    Phase 1: Core Entities + Responsibilities

        1. Game: The central coordinator. Manages flow, turns, and outcome.

            Responsibilities:
                a. Initialize game: players, board, etc.
                b. Manage player turns
                c. Accept and apply moves
                d. Update game status (IN_PROGRESS, WON, DRAW)
                e. Identify winner or draw
                f. Terminate game when needed

            Design Notes:
                a. Should not handle board internals or win logic directly
                b. Should use WinningStrategy later via delegation

        2. Board: Holds the grid, validates and applies moves.

            Responsibilities:
                a. Initialize size x size grid of cells
                b. Validate whether a move is within bounds and on an empty cell
                c. Update the cell with a player's symbol
                d. Provide access to rows/columns/diagonals for win check
                e. Expose current board state (for logging, UI, or debugging)

            
            Design Notes:
                a. Should be independent of game loop or player logic.
                b. May later delegate win-check logic to WinningStrategy.

        3. Cell: Represents a single position on the board.

            Responsibilities:
                a. Maintain its coordinates (row, col)
                b. Maintain who occupies it (None or a Player)
                c. Should be able to report if it's empty


            Design Notes:
                a. Immutable once set (or enforce single-assignment logic)
                b. Could hold symbol directly or reference to player
        
        4. Player (abstract class): Base class for human or AI players

            Responsibilities:
                a. Hold player name and symbol (e.g., X or O)
                b. Expose make_move(board) interface — to be overridden
                c. Could store additional metadata (e.g., id, score)

            Design Notes:
                Polymorphic design; we will later extend with HumanPlayer and AIPlayer.

        5. Move: One atomic action in the game.

            Responsibilities:
                a. Represent a move (row, col, player)
                b. Encapsulate the intent of a player's action

            Design Notes:
                a. Useful for tracking history, auditing, or debugging
                b. May be used with MoveHistory in Phase 2

        6. GameStatus(Enum): State of the game.

            Possible Values:
                IN_PROGRESS
                DRAW
                WON

            Responsibilities:
                a. Represent finite game states
                b. Used in Game to check when to stop or announce outcome


            Design Notes:
                In future, a State pattern could replace this, but an Enum is usually enough here.

        7. Symbol (Enum): Either X or O

            Responsibilities:
                Represent valid symbols used by players

            Design Notes:
                Better than raw strings (type-safe, readable, maintainable)
                
                                
"""