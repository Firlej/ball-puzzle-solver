class Ball:
    def __init__(self, color):
        self.color = color
    
    def __str__(self) -> str:
        return str(self.color)
    
    def __repr__(self) -> str:
        return str(self.color)
    
    def __hash__(self):
        return hash(self.color)

    def __gt__(self, other):
        if not isinstance(other, Ball):
            return NotImplemented
        return self.color > other.color

    def __lt__(self, other):
        if not isinstance(other, Ball):
            return NotImplemented
        return self.color < other.color
    
    def __eq__(self, other):
        if isinstance(other, Ball):
            return self.color == other.color
        raise Exception(f"invalid comparison of {other} with {self}")
