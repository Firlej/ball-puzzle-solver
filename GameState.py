from copy import deepcopy

from Ball import Ball
from Container import Container

class GameState:
    def __init__(self, containers: list[Container]):
        self.containers = containers
        
    def is_win(self):
        for c in self.containers:
            if len(c) < 4 and len(c) != 0:
                return False
            if len(c) == 4 and len(set(c)) > 1:
                return False
        return True
            
            
        
    def make_move(self, index_a, index_b):
        self.containers[index_b].put(self.containers[index_a].pop())

    def get_possible_moves(self):
        
        moves = []
        
        for i, a in enumerate(self.containers):
            
            if not a.can_pop():
                continue
            
            # Don't make moves that remove balls from containers with 3 or 4 balls with the same color
            if len(set(a)) == 1 and len(a) in [3, 4]:
                continue
            
            ball = a.get_top_ball()
            
            for j, b in enumerate(self.containers):
                
                # Don't make moves that keep balls in the same container
                if i == j:
                    continue
                
                # Don't make moves that move balls fron single colored containers into empty containers
                if len(set(a)) == 1 and len(a) in [1, 2] and len(b) == 0:
                    continue
                
                if b.can_put(ball):
                    moves.append((i, j))
        
        return moves
    
    def __str__(self) -> str:
        return str(self.containers)
    
    def __repr__(self) -> str:
        return str(self.containers)
        
    def __hash__(self) -> int:
        containers = deepcopy(self).containers
        containers.sort(key=lambda x: x)
        return hash(tuple(containers))
    
    def __eq__(self, other) -> bool:
        return hash(self) == hash(other)