from AiC4 import AiC4

class Idiot(AiC4):
    def __init__(self):
        pass
    
    def takeTurn(self, board):
        for x in range(7):
            if(board[x][5] is None):
                return x
        return -1