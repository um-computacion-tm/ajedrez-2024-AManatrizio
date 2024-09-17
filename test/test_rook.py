import unittest
from game.rook import Rook

class TestRook(unittest.TestCase):

    def setUp(self):
        self.rook = Rook("WHITE")  # Crea un objeto Rook blanco para usar en las pruebas

    def check_movement(self, start_row, start_col, end_row, end_col, expected_result):
        self.assertEqual(self.rook.horizontal_or_vertical_movement(start_row, start_col, end_row, end_col), expected_result)

    def test_init(self):
        # Verifica que rook es una instancia de Rook
        self.assertIsInstance(self.rook, Rook)

    def test_str(self):
        # Verifica la representación en cadena para WHITE
        white_rook = Rook("WHITE")
        self.assertEqual(str(white_rook), "♖")
        
        # Verifica la representación en cadena para BLACK
        black_rook = Rook("BLACK")
        self.assertEqual(str(black_rook), "♜")

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
