from AiC4 import AiC4

class Doofus(AiC4):
    def __init__(self):
        self.pos = -1
    
    def takeTurn(self, board):
        self.pos += 1
        while board[self.pos%7][5] is not None:
            self.pos += 1
        return self.pos % 7