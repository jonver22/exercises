class Player:
    def __init__(self):
        self.name = input("Please enter your name: ")
        self.__score = 0
        self.__char = input("Choose your symbol: X or O")

    #getter
    @property
    def name(self):
        return self.__name

    #setter
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self, value):
        self.__score = value
        if value < 0:
            raise ValueError("geen geldige score")
        else:
            self.__score = value

    @property
    def char(self):
        return self.__char

    @char.setter
    def char(self, symb):
        if symb.lower() in "xo":
            self.__char = symb.upper()
        else:
            raise ValueError("Da kan ni")


class Board:
    def __init__(self):
        self.clear_board()

    def clear_board(self):
        self.__board = [["_"]*7]*6

    def insert_token(self, userinput, Player):
        self.__colidx = int(userinput) - 1
        for rowidx in range(len(self.__board)):
            if self.__board[rowidx][self.__colidx] == "_":
                continue
            else:
                self.__board[rowidx -1][self.__colidx] = Player.char
                self.__rowidx = rowidx - 1
                
    def print_board(self):
        print(" ".join(["1","2","3","4","5","6","7"]))
        for row in self.__board:
            print(" ".join(row))

    def check_win(self):
        #horizontaal
        #for loop
        startpoint = max((self.__colidx - 3), 0)
        endpoint = min((self.__colidx + 4), 7) #excl
        self.__board[self.__rowidx][startpoint:startpoint + 4]
        for i in range(startpoint, endpoint+4):
            if i + 4:
            self.__board[self.__rowidx][i:i+4]


testBoard = Board()
testBoard.print_board()