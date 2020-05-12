class play:
    
    verbose = True
    
    def __init__(self):
        pass
        
    def initialiseBoard(self):
        board = []
        for x in range(7):
            column = []
            for cell in range(6):
                column.append(None)
            board.append(column)
        return board
        
    def playerBoard(self, board, player_num):
        player_board = []
        for column in board:
            player_column = []
            for cell in column:
                if cell is None:
                    player_column.append(None)
                else:
                    player_column.append(cell == player_num)
            player_board.append(player_column)
        return player_board
        
    def printBoard(self, board):
        none_code = " "
        player_codes = ["O","#"]
        header = "+-------+"
        print(header)
        for y in range(6)[::-1]:
            row = "|"
            for x in range(7):
                cell = board[x][y]
                if cell is None:
                    row += none_code
                else:
                    row += player_codes[cell]
            row += "|"
            print(row)
        print(header)
    
    def checkWin(self, board):
        # check columns
        for column in board:
            token = column[0]
            count = 1
            for x in range(1,6):
                cell = column[x]
                if cell is None:
                    break
                if cell == token:
                    count += 1
                    if count == 4:
                        return token
                else:
                    token = cell
                    count = 1

        # check rows
        for y in range(6):
            token = board[0][y]
            count = 1
            for x in range(1,7):
                cell = board[x][y]
                if cell is None:
                    token = None
                    count = 0
                else:
                    if cell == token:
                        count += 1
                        if count == 4:
                            return token
                    else:
                        token = cell
                        count = 1
        
        # check diagonals
        for x in range(6):
            token = None
            count = 0
            for y in range(6):
                column = x+y-2
                row = y
                if column >= 0 and column<7:
                    cell = board[column][row]
                    if cell is None:
                        token = None
                        count = 0
                    else:
                        if cell == token:
                            count += 1
                            if count == 4:
                                return token
                        else:
                            token = cell
                            count = 1
        for x in range(6):
            token = None
            count = 0
            for y in range(6):
                column = x-y+3
                row = y
                if column >= 0 and column<7:
                    cell = board[column][row]
                    if cell is None:
                        token = None
                        count = 0
                    else:
                        if cell == token:
                            count += 1
                            if count == 4:
                                return token
                        else:
                            token = cell
                            count = 1
                        
            
        
        return None
            
            

    def compete(self, player1, player2):
        board = self.initialiseBoard()
        players = [player1, player2]
        turn_num = 0
        while True:
            player_num = turn_num%2
            if self.verbose:
                print("Turn #"+str(turn_num)+" - Player #"+str(player_num))
            current_player = players[player_num]
            player_board = self.playerBoard(board, player_num)
            placement_position = current_player.takeTurn(player_board)
            if self.verbose:
                print("Insert token, pos "+str(placement_position))
            if board[placement_position][5] is None:
                for x in range(6):
                    if board[placement_position][x] is None:
                        board[placement_position][x] = player_num
                        break
            else:
                print("Error - invalid move - Player #"+str(player_num))
                return
            if self.verbose:
                self.printBoard(board)
                print("--------------------------------")
            turn_num += 1
            if turn_num == 42:
                print("GAME OVER - DRAW")
                return
            else:
                winner = self.checkWin(board)
                if winner is not None:
                    print("GAME OVER - Player #"+str(winner)+" wins")
                    return
            