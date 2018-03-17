import numpy as np

class TTTcore:
    PLAYER_1 = 1
    PLAYER_2 = -1
    def __init__(self):
        self.counter = 0
        self.history = []
        self.chess_board = np.zeros((3,3), dtype=np.int8)

    def put_chess(self, i, j):
        if self.chess_board[i, j] == 0:
            self.chess_board[i, j] = self.PLAYER_1 if self.counter%2 == 0 else self.PLAYER_2
            self.history.append((i, j))
            self.counter += 1
            return False
        else:
            return True

    def check(self):
        terminal_condition = [3*self.PLAYER_1, 3*self.PLAYER_2]
        if (sum([self.chess_board[i, 0] for i in range(3)]) in terminal_condition or
            sum([self.chess_board[i, 1] for i in range(3)]) in terminal_condition or
            sum([self.chess_board[i, 2] for i in range(3)]) in terminal_condition or
            sum([self.chess_board[0, i] for i in range(3)]) in terminal_condition or
            sum([self.chess_board[1, i] for i in range(3)]) in terminal_condition or
            sum([self.chess_board[2, i] for i in range(3)]) in terminal_condition or
            sum([self.chess_board[i, i] for i in range(3)]) in terminal_condition or
            sum([self.chess_board[i, 2-i] for i in range(3)]) in terminal_condition):
            return True
        else:
            return False