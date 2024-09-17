import unittest
from game.rook import Rook
from .test_utils import TestUtils

class TestRook(unittest.TestCase):

    def setUp(self):
        self.rook = Rook("WHITE")  # Crea un objeto Rook blanco para usar en las pruebas


    def check_movement(self, start_row, start_col, end_row, end_col, expected_result):
        self.assertEqual(self.rook.horizontal_or_vertical_movement(start_row, start_col, end_row, end_col), expected_result)

    def test_init(self):
        # Verifica que rook es una instancia de Rook
        self.assertIsInstance(self.rook, Rook)

    def check_piece_str(self, piece, expected_white, expected_black):
        self.assertEqual(str(piece("WHITE")), expected_white)
        self.assertEqual(str(piece("BLACK")), expected_black)

    def test_rook_str(self):
        utils = TestUtils()
        utils.check_piece_str(self, Rook, "♖", "♜")


    def test_horizontal(self):
        # Movimiento horizontal válido
        self.check_movement(0, 0, 0, 6, "horizontal")

    def test_vertical(self):
        # Movimiento vertical válido
        self.check_movement(0, 1, 0, 0, "vertical")

    def test_invalid(self):
        # Movimiento inválido (diagonal en este caso)
        self.check_movement(0, 1, 0, 1, "invalid")




if __name__ == "__main__":
    unittest.main()
