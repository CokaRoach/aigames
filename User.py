from AiC4 import AiC4

class User(AiC4):
    def __init__(self):
        pass

    def takeTurn(self, board):
        header = "+-------+"
        print("Current board state: (you are $)")
        print("+0123456+")
        print("+-------+")
        for y in range(6)[::-1]:
            row = "|"
            for x in range(7):
                cell = board[x][y]
                if cell is None:
                    row += " "
                else:
                    if cell:
                        row += "$"
                    else:
                        row += "@"
            row += "|"
            print(row)
        print("+-------+")
        print("+0123456+")
        print("Which column would you like to try?")
        return int(input())