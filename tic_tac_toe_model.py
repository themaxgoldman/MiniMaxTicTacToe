from enum import Enum


class TicTacToeModel:

    def __init__(self, board_size=3):
        self.board_size = board_size
        self.num_moves = 0
        self.board = [[None for i in range(self.board_size)]
                      for j in range(self.board_size)]
        self.current_player = 0

    def check_winner(self, x, y):
        if x >= self.board_size or x < 0:
            raise ValueError(
                "x: %d out of range: %d".format(x, self.board_size - 1))
        if y >= self.board_size or y < 0:
            raise ValueError(
                "y: %d out of range: %d".format(y, self.board_size - 1))
        if self.num_moves < 5:
            return False
        player = self.board[x][y]
        if player is None:
            raise ValueError("empty spot given")

        column_win = True
        row_win = True

        rl_diag_win = True
        for i in range(self.board_size):
            column_win = column_win and self.board[i][y] == player
            row_win = row_win and self.board[x][i] == player

        lr_diag_win = False
        if x == y:
            lr_diag_win = True
            for i in range(self.board_size):
                lr_diag_win = lr_diag_win and (
                    self.board[i][i] == player)

        rl_diag_win = False
        if x + y == self.board_size - 1:
            rl_diag_win = True
            for i in range(self.board_size):
                rl_diag_win = rl_diag_win and (
                    self.board[i][self.board_size - 1 - i] == player)

        return column_win or row_win or lr_diag_win or rl_diag_win

    def make_move(self, x, y, player):
        if x >= self.board_size or x < 0:
            raise ValueError(
                "x: {x} out of range: {range}".format(x=x,
                                                      range=(
                                                          self.board_size-1)))
        if y >= self.board_size or y < 0:
            raise ValueError(
                "y: {y} out of range: {range}".format(y=y,
                                                      range=(
                                                          self.board_size-1)))
        if player < 0 or player > 1:
            raise ValueError("invalid player")
        if self.current_player != player:
            raise ValueError("player is not current player")
        if self.board[x][y] is not None:
            raise ValueError("invalid move, spot already taken")
        self.board[x][y] = player
        self.current_player = (self.current_player + 1) % 2
        self.num_moves += 1

    def filled(self):
        return self.num_moves == self.board_size ** 2


def main():
    model = TicTacToeModel()
    model.make_move(0, 1, 4)


if __name__ == "__main__":
    main()
