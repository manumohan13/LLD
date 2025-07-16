"""
    Relationships Between Core Entities
        1. Game → Player
            Type: Aggregation ("Has-a" but loosely coupled)
            Symbol: Hollow diamond
            Explanation:
                a. Game has multiple Player instances
                b. If game is deleted, players may exist elsewhere (e.g., in a tournament context)

            Representation:
                Game <>---- Player

            
        2. Game → Board
            Type: Composition (Strong ownership; part-whole)
            Symbol: Solid diamond

            Explanation:
                a. The Board is created and destroyed with the Game
                b. It's tightly coupled and lifecycle-bound

            
            Representation:
                Game ◼---- Board

        3. Board → Cell
            Type: Composition (Strong ownership; part-whole)
            Symbol: Solid diamond

            Explanation:
                a. A Board is made of Cells
                b. Without the Board, Cells don't make sense or exist

            Representation:
                Board ◼---- Cell

        4. Move → Player
            Type: Dependency (Temporarily uses another)
            Symbol: Dotted line

            Explanation:
                a. A Move includes a reference to the Player who made it
                b. But it doesn't own the player

            Reprensentation:
                Move ----> Player

        5. Player → Symbol
            Type: Association (One class uses another)
            Symbol: Solid line

            Explanation:
                a. Each player has a symbol (X or O)
                b. It's a fixed enum, shared among all players

        6. Game → GameStatus
            Type: Association (One class uses another)
            Symbol: Solid line

            Explanation:
                a. Game uses GameStatus to track current state

            Representation
                Game ----> GameStatus

                
        Game ◼---- Board ◼---- Cell
        |
        +<>---- Player ----> Symbol
        |
        +----> GameStatus
        |
        +----> Move ----> Player



        
    To define the attributes, methods for an entity:
        1. What is this class responsible for?
        2. What does it need to *know*? → Attributes
        3. What does it need to *do*? → Methods
        4. Who uses it? What methods will they need?
        5. What should be hidden? (encapsulation)
        6. What must always stay valid? (invariants)



"""