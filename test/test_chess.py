import unittest
from unittest.mock import MagicMock, patch
from game.chess import Chess
from game.board import Board

class TestChess(unittest.TestCase):

    def setUp(self):
        self.chess = Chess()

    def check_play_move(self, setup_color, setup_is_valid, setup_result, expected_result, expected_next_player=None):
        self.setup_move_scenario(setup_color, setup_is_valid, setup_result)
        result = self.chess.play_move("00", "01")
        if isinstance(expected_result, tuple):
            self.assertEqual(result, expected_result)
        elif expected_result is None:
            self.assertEqual(result, "INVALID")
        else:
            self.assertEqual(result, expected_result)
        if expected_next_player:
            self.assertEqual(self.chess.__current_player__, expected_next_player)

    def setup_move_scenario(self, color, is_valid_move, move_result):
        self.chess.__board__.get_color = MagicMock(return_value=color)
        self.chess.__board__.is_valid_move = MagicMock(return_value=is_valid_move)
        self.chess.__board__.move_piece = MagicMock(return_value=move_result)

    def test_init(self):
        self.assertIsInstance(self.chess.__board__, Board)
        self.assertEqual(self.chess.__current_player__, "WHITE")
        self.assertFalse(self.chess.__mutual_agreement_to_end__)

    def test_get_captures(self):
        self.chess.__board__.get_capture_counts = MagicMock(return_value={"WHITE": 5, "BLACK": 3})
        captures = self.chess.get_captures()
        self.assertEqual(captures, {"WHITE": 5, "BLACK": 3})

    def test_is_over(self):
        # Test when game is not over
        self.assertFalse(self.chess.is_over())

        # Test when white captures 15 pieces
        self.chess.__board__.__white_captures__ = 15
        self.assertTrue(self.chess.is_over())

        # Reset and test when black captures 15 pieces
        self.chess.__board__.__white_captures__ = 0
        self.chess.__board__.__black_captures__ = 15
        self.assertTrue(self.chess.is_over())

        # Test when king is captured
        self.chess.__board__.__black_captures__ = 0
        self.chess.__board__.__king_captured__ = True
        self.assertTrue(self.chess.is_over())

        # Test mutual agreement
        self.chess.__board__.__king_captured__ = False
        self.chess.__mutual_agreement_to_end__ = True
        self.assertTrue(self.chess.is_over())

    def test_end_game_by_agreement(self):
        self.chess.end_game_by_agreement()
        self.assertTrue(self.chess.__mutual_agreement_to_end__)

    def test_display_board(self):
        self.chess.__board__.display_board = MagicMock()
        self.chess.display_board()
        self.chess.__board__.display_board.assert_called_once()

    def test_play_move_invalid_turn(self):
        self.chess.__board__.get_color = MagicMock(return_value="BLACK")
        result = self.chess.play_move("00", "01")
        self.assertEqual(result, "INVALID_TURN")

    def test_play_move_valid(self):
        self.check_play_move("WHITE", True, "NORMAL", "VALID", "BLACK")

    def test_play_move_unexpected_result(self):
        self.check_play_move("WHITE", True, "UNEXPECTED", "UNEXPECTED", "BLACK")


    def check_play_move_scenario(self, expected_result, is_valid_move=True):
        self.setup_move_scenario("WHITE", is_valid_move, expected_result)
        result = self.chess.play_move("00", "01")
        if expected_result:
            self.assertEqual(result, expected_result)
        else:
            self.assertEqual(result, "INVALID")

    def test_play_move_king_captured(self):
        self.check_play_move_scenario(("KING_CAPTURED", "info"))

    def test_play_move_promotion_needed(self):
        self.check_play_move_scenario(("PROMOTION_NEEDED", "info"))

    def test_play_move_invalid_capture(self):
        self.check_play_move_scenario("INVALID_CAPTURE")

    def test_play_move_invalid(self):
        self.check_play_move_scenario(None, is_valid_move=False)
    
    def test_play_move_promotion(self):
        self.setup_move_scenario("WHITE", True, ("PROMOTION_NEEDED", "info"))
        result = self.chess.play_move("00", "01")
        self.assertEqual(result, ("PROMOTION_NEEDED", "info"))
        self.assertEqual(self.chess.__current_player__, "WHITE")

    def test_promote_pawn(self):
        self.chess.__board__.handle_pawn_promotion = MagicMock(return_value="QUEEN")
        result = self.chess.promote_pawn(0, 0, "QUEEN")
        self.assertEqual(result, "QUEEN")
        self.assertEqual(self.chess.__current_player__, "BLACK")

    def test_parse_move(self):
        fila, columna = self.chess.parse_move("12")
        self.assertEqual(fila, 1)
        self.assertEqual(columna, 2)
    
    def test_parse_move_invalid_input(self):
        with self.assertRaises(ValueError) as context:
            self.chess.parse_move("123")
        self.assertIn("Invalid input. Please enter two digits together", str(context.exception))

        with self.assertRaises(ValueError) as context:
            self.chess.parse_move("ab")
        self.assertIn("Please enter only numbers for coordinates.", str(context.exception))


if __name__ == "__main__":
    unittest.main()
