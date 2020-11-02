from enum import Enum


class TicTacToeModel:

    def __init__(self, board_size=3):
        self.board_size = board_size
        self.board = [[None for i in range(self.board_size)]
                      for j in range(self.board_size)]
        self.current_player = 0

    def check_winner(self, x, y):
        p = self.board[x][y]
        # TODO: Check if winner
        raise NotImplementedError

    def make_move(self, x, y, player):
        if x >= self.board_size or x < 0:
            raise ValueError(
                "x: %d out of range: %d".format(x, self.board_size - 1))
        if y >= self.board_size or y < 0:
            raise ValueError(
                "y: %d out of range: %d".format(y, self.board_size - 1))
        if player < 0 or player > 1:
            raise ValueError("invalid player")
        if self.current_player != player:
            raise ValueError("player is not current player")
        if self.board[x][y] is not None:
            raise ValueError("invalid move, spot already taken")
        self.board[x][y] = player
        self.current_player = (self.current_player + 1) % 2


def main():
    model = TicTacToeModel()
    model.make_move(0, 1, 4)


if __name__ == "__main__":
    main()
