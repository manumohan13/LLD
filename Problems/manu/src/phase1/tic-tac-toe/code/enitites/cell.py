from enums.symbol import Symbol

class Cell:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.symbol = Symbol.EMPTY

    def is_empty(self) -> bool:
        return self.symbol == Symbol.EMPTY

    def mark(self, symbol: Symbol):
        if not self.is_empty():
            raise ValueError("Cell is already marked")
        self.symbol = symbol

    def clear(self):
        self.symbol = Symbol.EMPTY

    def __str__(self) -> str:
        return self.symbol.value
