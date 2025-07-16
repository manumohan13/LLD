from enums.symbol import Symbol

class Player:
    def __init__(self, name: str, symbol: Symbol):
        if symbol not in (Symbol.X, Symbol.O):
            raise ValueError("Inavlid symbol for player")
        
        self._name = name
        self._symbol = symbol

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def symbol(self) -> Symbol:
        return self._symbol
    
    def __str__(self) -> str:
        return f"{self._name} ({self._symbol.value})"