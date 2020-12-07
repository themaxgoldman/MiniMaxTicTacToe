from enum import Enum
import numpy as np
import copy


class TicTacToeModel:

    def __init__(self, board_size=3):
        self.board_size = board_size
        self.num_moves = 0
        self.current_player = 0
        self.board = [[None for x in range(self.board_size)]
                      for y in range(self.board_size)]
        self.remaining_moves = {
            (x, y) for x in range(self.board_size)
            for y in range(self.board_size)}

    def copy(self):
        copied = TicTacToeModel(board_size=self.board_size)
        copied.num_moves = self.num_moves
        copied.current_player = self.current_player
        copied.board = self.board.copy()
        copied.remaining_moves = self.remaining_moves.copy()
        return copied

    def check_winner(self, spot):
        if spot[0] >= self.board_size or spot[0] < 0:
            raise ValueError("x: {x} out of range: {board_size}".format(
                x=spot[0], board_size=(self.board_size - 1)))
        if spot[1] >= self.board_size or spot[1] < 0:
            raise ValueError(
                "y: {} out of range: {}".format(spot[1], self.board_size - 1))
        if self.num_moves < self.board_size * 2 - 1:
            return False
        player = self.board[spot[0]][spot[1]]
        if player is None:
            raise ValueError("empty spot given")

        column_win = True
        row_win = True

        rl_diag_win = True
        for i in range(self.board_size):
            column_win = column_win and self.board[i][spot[1]] == player
            row_win = row_win and self.board[spot[0]][i] == player

        lr_diag_win = False
        if spot[0] == spot[1]:
            lr_diag_win = True
            for i in range(self.board_size):
                lr_diag_win = lr_diag_win and (
                    self.board[i][i] == player)

        rl_diag_win = False
        if spot[0] + spot[1] == self.board_size - 1:
            rl_diag_win = True
            for i in range(self.board_size):
                rl_diag_win = rl_diag_win and (
                    self.board[i][self.board_size - 1 - i] == player)

        return column_win or row_win or lr_diag_win or rl_diag_win

    def make_move(self, move, player):
        if move[0] >= self.board_size or move[0] < 0:
            raise ValueError(
                "x: {x} out of range: {range}".format(
                    x=move[0],
                    range=(self.board_size - 1)))
        if move[1] >= self.board_size or move[1] < 0:
            raise ValueError(
                "y: {y} out of range: {range}".format(y=move[1],
                                                      range=(
                                                          self.board_size-1)))
        if player < 0 or player > 1:
            raise ValueError("invalid player")
        if self.current_player != player:
            raise ValueError("player is not current player")
        if self.board[move[0]][move[1]] is not None:
            raise ValueError("invalid move, spot already taken")
        self.board[move[0]][move[1]] = player
        self.current_player = (self.current_player + 1) % 2
        self.num_moves += 1
        self.remaining_moves.remove(move)

    def filled(self):
        return self.num_moves >= self.board_size ** 2
