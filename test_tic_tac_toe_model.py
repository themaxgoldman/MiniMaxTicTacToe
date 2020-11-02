import unittest
from tic_tac_toe_model import TicTacToeModel


class TicTacToeModelTestCases(unittest.TestCase):

    def setUp(self):
        self.empty_board = TicTacToeModel()

        self.mid_game_board = TicTacToeModel()
        self.mid_game_board.board = [[0,    1, 0],
                                     [None, 0, None],
                                     [None, 1, None]]

    def test_default_size(self):
        self.assertEqual(self.empty_board.board_size, 3)

    def test_empty_board(self):
        self.assertEqual(self.empty_board.board,
                         [[None, None, None],
                          [None, None, None],
                          [None, None, None]])

    def test_make_move_x_out_of_range(self):
        with self.assertRaises(ValueError):
            self.empty_board.make_move(3, 1, 0)
        with self.assertRaises(ValueError):
            self.empty_board.make_move(-1, 1, 0)

    def test_make_move_y_out_of_range(self):
        with self.assertRaises(ValueError):
            self.empty_board.make_move(1, 3, 0)
        with self.assertRaises(ValueError):
            self.empty_board.make_move(1, -1, 0)

    def test_make_move_invalid_player(self):
        with self.assertRaises(ValueError):
            self.empty_board.make_move(1, 2, -1)
        with self.assertRaises(ValueError):
            self.empty_board.make_move(1, 2, 2)

    def test_make_move_invalid_move(self):
        with self.assertRaises(ValueError):
            self.empty_board.make_move(0, 0, 1)

    def test_make_move_wrong_player(self):
        with self.assertRaises(ValueError):
            self.mid_game_board.make_move(1, 2, 1)

    def test_make_move_empty_board(self):


if __name__ == "__main__":
    unittest.main()
