from AiC4 import AiC4

class Idiot(AiC4):
    def __init__(self):
        pass

    """
       board is a 2d array of the connect 4 board
        board[0] is the first column
        board[0][0] is the bottom cell in the first column
        values will be one of:
         - True = your token
         - False = oponents token
         - None = empty
        
        return value should be the index column where you want to insert your next token
    """    
    def takeTurn(self, board):
        for x in range(7):
            if(board[x][5] is None):
                return x
        return -1