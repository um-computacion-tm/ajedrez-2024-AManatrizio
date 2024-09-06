# test/test_rook.py
import unittest
from game.rook import Rook

class TestRook(unittest.TestCase):

    def test_init(self):
        rook = Rook("WHITE")  # Creo objeto rook de la Clase Rook
        self.assertIsInstance(rook, Rook)  # Verifica que rook es una instancia de Rook

    def test_str(self):
        white_rook = Rook("WHITE")
        black_rook = Rook("BLACK")
        self.assertEqual(str(white_rook), "♖")  # Verifica la representación en cadena para WHITE
        self.assertEqual(str(black_rook), "♜")  # Verifica la representación en cadena para BLACK

    def test_horizontal(self):
        rook = Rook("WHITE")  # Creo objeto rook de la Clase Rook
        # Movimieto horizontal
        self.assertEqual(rook.horizontal_or_vertical_movement(0, 0, 0, 6),"horizontal")

    def test_vertical(self):
        rook = Rook("WHITE")  # Creo objeto rook de la Clase Rook
        # Movimieto horizontal
        self.assertEqual(rook.horizontal_or_vertical_movement(0, 1, 0, 0), "vertical")

    def test_invalid(self):
        rook = Rook("WHITE")  # Creo objeto rook de la Clase Rook
        # Movimiento inválido (diagonal en este caso)
        self.assertEqual(rook.horizontal_or_vertical_movement(0, 1, 0, 1), "invalid")


if __name__ == "__main__":
    unittest.main()


