from Ball import Ball

class Container(list):
    def __init__(self, *args):
        super().__init__(*args)
        
    def get_top_ball(self) -> Ball:
        return self[-1]
        
    def can_pop(self):
        if len(self) == 0:
            return False
        return True

    def can_put(self, ball: Ball):
        if len(self) >= 4:
            return False
        if len(self) > 0 and self[-1] != ball:
            return False
        return True

    def put(self, ball: Ball):
        if len(self) >= 4:
            raise Exception("Container is full")
        if len(self) > 0 and self[-1] != ball:
            raise Exception(f"Cant put {ball} on {self[-1]}")
        super().append(ball)
        
    def __hash__(self) -> int:
        return hash(tuple(self))
