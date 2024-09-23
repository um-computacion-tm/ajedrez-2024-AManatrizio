import unittest
from game.board import Board
from game.rook import Rook
from game.king import King
from game.knight import Knight
from game.bishop import Bishop
from game.queen import Queen
from game.pawn import Pawn
from unittest.mock import patch
from io import StringIO

class TestBoardSetup(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_init(self):
        self.assertEqual(len(self.board.matrix), 8)
        for row in self.board.matrix:
            self.assertEqual(len(row), 8)

    def test_piece(self):
        self.assertIsInstance(self.board.matrix[0][0], Rook)
        self.assertIsInstance(self.board.matrix[0][7], Rook)
        self.assertIsInstance(self.board.matrix[0][1], Knight)
        self.assertIsInstance(self.board.matrix[0][6], Knight)
        self.assertIsInstance(self.board.matrix[0][2], Bishop)
        self.assertIsInstance(self.board.matrix[0][5], Bishop)
        self.assertIsInstance(self.board.matrix[0][3], Queen)
        self.assertIsInstance(self.board.matrix[0][4], King)
        self.assertEqual(self.board.matrix[0][0].color, "BLACK")
        self.assertEqual(self.board.matrix[7][3].color, "WHITE")

class TestBoardHelperMethods(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_is_out_of_board(self):
        self.assertTrue(self.board.is_out_of_board(0, 0))
        self.assertFalse(self.board.is_out_of_board(9, 9))
        self.assertFalse(self.board.is_out_of_board(8, 8))

    def test_get_color(self):
        self.assertEqual(self.board.get_color(7, 3), "WHITE")
        self.assertEqual(self.board.get_color(0, 0), "BLACK")

    def test_has_piece(self):
        self.assertTrue(self.board.has_piece(0, 0))
        self.assertFalse(self.board.has_piece(4, 4))

    def test_is_valid_move(self):
        self.assertTrue(self.board.is_valid_move(0, 0, 1, 0))
        self.assertFalse(self.board.is_valid_move(0, 0, 8, 8))

class TestBoardPathClear(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_is_path_clear(self):
        self.assertTrue(self.board.is_path_clear(3, 0, 3, 7, 'horizontal'))

    def test_is_path_clear_blocked(self):
            test_cases = [
                # start_row, start_col, end_row, end_col, block_row, block_col, direction
                (0, 0, 0, 3, 0, 2, "horizontal"),
                (0, 0, 3, 0, 2, 0, "vertical"),
                (0, 0, 3, 3, 2, 2, "diagonal"),
            ]

            for start_row, start_col, end_row, end_col, block_row, block_col, direction in test_cases:
                with self.subTest(f"{direction} from ({start_row},{start_col}) to ({end_row},{end_col})"):
                    self.board.matrix[block_row][block_col] = Pawn("BLACK")
                    self.assertFalse(self.board.is_path_clear(start_row, start_col, end_row, end_col, direction))
    
    def test_is_path_clear_invalid_movement(self):
        self.assertFalse(self.board.is_path_clear(0, 0, 2, 1, "invalid"))

class TestBoardDisplay(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_display_board(self):
        expected_output = (
            "    0   1   2   3   4   5   6   7\n"
            "  +---+---+---+---+---+---+---+---+\n"
            "0 | ♜ | ♞ | ♝ | ♛ | ♚ | ♝ | ♞ | ♜ | 0\n"
            "  +---+---+---+---+---+---+---+---+\n"
            "1 | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ | 1\n"
            "  +---+---+---+---+---+---+---+---+\n"
            "2 |   |   |   |   |   |   |   |   | 2\n"
            "  +---+---+---+---+---+---+---+---+\n"
            "3 |   |   |   |   |   |   |   |   | 3\n"
            "  +---+---+---+---+---+---+---+---+\n"
            "4 |   |   |   |   |   |   |   |   | 4\n"
            "  +---+---+---+---+---+---+---+---+\n"
            "5 |   |   |   |   |   |   |   |   | 5\n"
            "  +---+---+---+---+---+---+---+---+\n"
            "6 | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | 6\n"
            "  +---+---+---+---+---+---+---+---+\n"
            "7 | ♖ | ♘ | ♗ | ♕ | ♔ | ♗ | ♘ | ♖ | 7\n"
            "  +---+---+---+---+---+---+---+---+\n"
            "    0   1   2   3   4   5   6   7\n"
        )

        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.board.display_board()
            actual_output = fake_output.getvalue()

        self.assertEqual(actual_output, expected_output)

class TestBoardMovement(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_move_piece_capture(self):
        self.board.matrix[3][3] = Pawn("BLACK")
        self.board.move_piece(6, 3, 3, 3)
        self.assertIsInstance(self.board.matrix[3][3], Pawn)
        self.assertEqual(self.board.matrix[3][3].color, "WHITE")

    def test_move_piece_same_color(self):
        with patch('builtins.print') as mock_print:
            self.board.move_piece(7, 0, 7, 1)
        mock_print.assert_called_with("No se puede capturar una pieza del mismo color.")

    def test_move_piece_pawn_first_move(self):
        pawn = self.board.matrix[6][0]
        self.board.move_piece(6, 0, 4, 0)
        self.assertFalse(pawn.first_move)

class TestBoardCaptures(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_update_capture_count(self):
        for color in ["WHITE", "BLACK"]:
            with self.subTest(f"Updating {color} capture count"):
                initial_captures = getattr(self.board, f"{color.lower()}_captures")
                self.board.update_capture_count(color)
                self.assertEqual(getattr(self.board, f"{color.lower()}_captures"), initial_captures + 1)


    def test_get_capture_counts(self):
        self.board.white_captures = 2
        self.board.black_captures = 3
        capture_counts = self.board.get_capture_counts()
        self.assertEqual(capture_counts["white_captures"], 2)
        self.assertEqual(capture_counts["black_captures"], 3)

    def test_print_capture_counts(self):
        self.board.white_captures = 2
        self.board.black_captures = 3
        with patch('builtins.print') as mock_print:
            self.board.print_capture_counts()
            mock_print.assert_any_call("Piezas blancas capturadas: 2")
            mock_print.assert_any_call("Piezas negras capturadas: 3")





if __name__ == '__main__':
    unittest.main()