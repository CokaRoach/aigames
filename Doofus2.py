from AiC4 import AiC4

class Doofus(AiC4):
    def __init__(self):
        self.pos = -1
        
    # Check for wins, only need to check ones which include that one position
    def checkWin(self, board, column_num, row_num):
        token = board[column_num][row_num]
        
        # check column
        if row_num >=3:
            for x in range(1,4):
                if board[column_num][row_num-x] == token:
                    if x == 3:
                        return True
                else:
                    break
                    
        # check row
        count = 1
        for x in range(column_num-1,-1,-1):  # previous columns
            if board[x][row_num] == token:
                count += 1
            else:
                break
        for x in range(column_num+1,7):  # next columns
            if board[x][row_num] == token:
                count += 1
            else:
                break
        if count >= 4:
            return True
        
        # check forward slash diagnonal    
        count = 1
        for x in range(1,4):
            if column_num-x >= 0 and row_num-x >= 0 and board[column_num-x][row_num-x] == token:
                count += 1
            else:
                break
        for x in range(1,4):
            if column_num+x < 7 and row_num+x < 6 and board[column_num+x][row_num+x] == token:
                count += 1
            else:
                break
        if count >= 4:
            return True
        
        # check back slash diagnonal    
        count = 1
        for x in range(1,4):
            if column_num-x >= 0 and row_num+x < 6 and board[column_num-x][row_num+x] == token:
                count += 1
            else:
                break
        for x in range(1,4):
            if column_num+x < 7 and row_num-x >=0 and board[column_num+x][row_num-x] == token:
                count += 1
            else:
                break
        if count >= 4:
            return True
        
        return False
        
        
        
    
    def nextRow(self, column):
        for x in range(0,6):
            if column[x] is None:
                return x
        return None
    
    def takeTurn(self, board):
        
        # Check for winning moves
        for column_num in range(0,7):
            row_num = self.nextRow(board[column_num])
            if row_num is not None:
                board[column_num][row_num] = True
                if self.checkWin(board,column_num,row_num):
                    return column_num
                board[column_num][row_num] = None
    
        # Check to stop winning moves
        for column_num in range(0,7):
            row_num = self.nextRow(board[column_num])
            if row_num is not None:
                board[column_num][row_num] = False
                if self.checkWin(board,column_num,row_num):
                    return column_num
                board[column_num][row_num] = None

        # proceed to play        
        self.pos += 1
        while board[self.pos%7][5] is not None:
            self.pos += 1
        return self.pos % 7
        
        
"""
python
from play import play
from Idiot1 import Idiot
from Doofus1 import Doofus
p = play()
p.compete(Idiot(), Doofus())
"""