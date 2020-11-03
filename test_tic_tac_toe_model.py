import unittest
from tic_tac_toe_model import TicTacToeModel


class TicTacToeModelTestCases(unittest.TestCase):

    def setUp(self):
        self.empty_board = TicTacToeModel()

        self.mid_game_board = TicTacToeModel()
        self.mid_game_board.current_player = 1
        self.mid_game_board.num_moves = 5
        self.mid_game_board.board = [[0,    1, 0],
                                     [None, 0, None],
                                     [None, 1, None]]

    def test_default_size(self):
        self.assertEqual(self.empty_board.board_size, 3)

    def test_empty_board(self):
        self.assertEqual(self.empty_board.num_moves, 0)
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
            self.empty_board.make_move(1, 2, 1)
        with self.assertRaises(ValueError):
            self.mid_game_board.make_move(2, 2, 0)

    def test_make_move_empty_board(self):
        self.empty_board.make_move(1, 1, 0)
        self.assertEqual(self.empty_board.num_moves, 1)
        self.assertEqual(self.empty_board.board,
                         [[None, None, None],
                          [None, 0,    None],
                          [None, None, None]])
        self.empty_board.make_move(0, 0, 1)
        self.assertEqual(self.empty_board.num_moves, 2)
        self.assertEqual(self.empty_board.board,
                         [[1,    None, None],
                          [None, 0,    None],
                          [None, None, None]])

    def test_make_move_mid_game_board(self):
        self.mid_game_board.make_move(2, 2, 1)
        self.assertEqual(self.mid_game_board.num_moves, 6)
        self.assertEqual(self.mid_game_board.board,
                         [[0,    1, 0],
                          [None, 0, None],
                          [None, 1, 1]])
        self.mid_game_board.make_move(2, 0, 0)
        self.assertEqual(self.mid_game_board.num_moves, 7)
        self.assertEqual(self.mid_game_board.board,
                         [[0,    1, 0],
                          [None, 0, None],
                          [0,    1, 1]])

    def test_check_winner_empty_spot(self):
        with self.assertRaises(ValueError):
            self.mid_game_board.check_winner(1, 2)

    def test_check_winner_x_out_of_range(self):
        with self.assertRaises(ValueError):
            self.empty_board.check_winner(3, 0)
        with self.assertRaises(ValueError):
            self.empty_board.check_winner(-1, 0)

    def test_check_winner_y_out_of_range(self):
        with self.assertRaises(ValueError):
            self.empty_board.check_winner(0, 3)
        with self.assertRaises(ValueError):
            self.empty_board.check_winner(0, -1)

    def test_check_winner_empty_board(self):
        self.assertFalse(self.empty_board.check_winner(0, 0))

    def test_check_winner_no_winner(self):
        self.assertFalse(self.mid_game_board.check_winner(0, 0))
        self.assertFalse(self.mid_game_board.check_winner(0, 1))
        self.assertFalse(self.mid_game_board.check_winner(0, 2))
        self.assertFalse(self.mid_game_board.check_winner(1, 1))
        self.assertFalse(self.mid_game_board.check_winner(2, 1))

    def test_check_winner_column_0(self):
        self.winning_board = TicTacToeModel()
        self.winning_board.current_player = 1
        self.winning_board.num_moves = 8
        self.winning_board.board = [[1, None, 0],
                                    [1, 0,    0],
                                    [1, 0,    1]]
        self.assertTrue(self.winning_board.check_winner(0, 0))
        self.assertTrue(self.winning_board.check_winner(1, 0))
        self.assertTrue(self.winning_board.check_winner(2, 0))

    def test_check_winner_column_1(self):
        self.winning_board = TicTacToeModel()
        self.winning_board.current_player = 0
        self.winning_board.num_moves = 5
        self.winning_board.board = [[1,    0,    1],
                                    [None, 0,    None],
                                    [None, 0,    None]]
        self.assertTrue(self.winning_board.check_winner(0, 1))
        self.assertTrue(self.winning_board.check_winner(1, 1))
        self.assertTrue(self.winning_board.check_winner(2, 1))

    def test_check_winner_column_2(self):
        self.winning_board = TicTacToeModel()
        self.winning_board.current_player = 1
        self.winning_board.num_moves = 6
        self.winning_board.board = [[0,    0,    1],
                                    [None, 0,    1],
                                    [None, None, 1]]
        self.assertTrue(self.winning_board.check_winner(0, 2))
        self.assertTrue(self.winning_board.check_winner(1, 2))
        self.assertTrue(self.winning_board.check_winner(2, 2))

    def test_check_winner_row_0(self):
        self.winning_board = TicTacToeModel()
        self.winning_board.current_player = 0
        self.winning_board.num_moves = 7
        self.winning_board.board = [[0,    0,    0],
                                    [None, 1,    1],
                                    [1,    None, 0]]
        self.assertTrue(self.winning_board.check_winner(0, 0))
        self.assertTrue(self.winning_board.check_winner(0, 1))
        self.assertTrue(self.winning_board.check_winner(0, 2))

    def test_check_winner_row_1(self):
        self.winning_board = TicTacToeModel()
        self.winning_board.current_player = 1
        self.winning_board.num_moves = 7
        self.winning_board.board = [[0, None, 0],
                                    [1, 1,    1],
                                    [1, 0,    0]]
        self.assertTrue(self.winning_board.check_winner(1, 0))
        self.assertTrue(self.winning_board.check_winner(1, 1))
        self.assertTrue(self.winning_board.check_winner(1, 2))

    def test_check_winner_row_2(self):
        self.winning_board = TicTacToeModel()
        self.winning_board.current_player = 1
        self.winning_board.num_moves = 7
        self.winning_board.board = [[None, None, None],
                                    [1,    1,    None],
                                    [0,    0,    0]]
        self.assertTrue(self.winning_board.check_winner(2, 0))
        self.assertTrue(self.winning_board.check_winner(2, 1))
        self.assertTrue(self.winning_board.check_winner(2, 2))

    def test_check_winner_left_right_diag(self):
        self.winning_board = TicTacToeModel()
        self.winning_board.current_player = 1
        self.winning_board.num_moves = 6
        self.winning_board.board = [[1, None, None],
                                    [0,    1, None],
                                    [0,    0, 1]]
        self.assertTrue(self.winning_board.check_winner(0, 0))
        self.assertTrue(self.winning_board.check_winner(1, 1))
        self.assertTrue(self.winning_board.check_winner(2, 2))

    def test_check_winner_right_left_diag(self):
        self.winning_board = TicTacToeModel()
        self.winning_board.current_player = 1
        self.winning_board.num_moves = 6
        self.winning_board.board = [[0, None, 0],
                                    [1, 0,    1],
                                    [0, None, 1]]
        self.assertTrue(self.winning_board.check_winner(0, 2))
        self.assertTrue(self.winning_board.check_winner(1, 1))
        self.assertTrue(self.winning_board.check_winner(2, 0))


if __name__ == "__main__":
    unittest.main()
