class Cell:
    
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.symbol = "-"

    def is_empty(self) -> bool:
        return self.symbol == '-'
    
    def mark(self, symbol: str):
        if not self.is_empty():
            raise ValueError(f"Cell is already marked")
        self.symbol = symbol

    def clear(self):
        self.symbol = '-'

    def __str__(self) -> str:
        return self.symbol