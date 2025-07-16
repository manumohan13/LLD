"""
    What is Tic Tac Toe?
        1. It's a two-player game played on a 3x3 grid.
        2. Players take turns marking cells with X or O.
        3. The first player to align three of their marks horizontally, vertically, or diagonally wins.
        4. If all 9 cells are filled and no one wins, it's a draw.

    Constraints and Edge Cases

        1. The grid can vary (3x3 is standard, but design should allow N x N).
        2. There may be variants with more than two players or different win conditions.
        3. Should support checking for invalid moves (e.g., playing on an already filled cell).
        4. Need to support game state management (in progress, draw, won).



    🧱 Phase Plan for Implementation

        We'll build the complete LLD in 3 Phases, starting from the foundation.

        ✅ Phase 1: Core Entities
            Focus: OOP, SRP/OCP, data encapsulation

            Entities to Design:

                Game

                Board

                Cell

                Player (base class)

                Move

                GameStatus (Enum)

                Symbol (Enum)

        🔶 Phase 2: Advanced Design Entities
            Focus: Strategy Pattern, extensibility, command stack, polymorphism

            Entities to Add:

                WinningStrategy (interface)

                DefaultWinningStrategy (implementation)

                GameManager (controller between UI & game engine)

                HumanPlayer, AIPlayer (inherit from Player)

                MoveHistory (stack for undo)

                MoveCommand (Command Pattern)

        🧩 Phase 3: Bonus Layer (Architectural Add-ons)
            Focus: Testability, maintainability, UI integration, real-time control

            Entities to Add:

            GameFactory (wiring all components, DI-friendly)

            GameObserver (Observer Pattern for UI/web/cli)

            TimerManager (for timed moves, advanced concurrency)

            Logger (for move audit, debugging)
"""