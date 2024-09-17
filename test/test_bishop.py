import unittest
from game.bishop import Bishop


class TestBishop(unittest.TestCase):

    def setUp(self):
        self.bishop = Bishop("WHITE")  # Crea un objeto Bishop blanco para usar en las pruebas

    def check_piece_str(self, piece, expected_white, expected_black):
        self.assertEqual(str(piece("WHITE")), expected_white)
        self.assertEqual(str(piece("BLACK")), expected_black)

    def test_str(self):
        # Verifica la representación en cadena para WHITE y BLACK
        self.check_piece_str(Bishop, "♗", "♝")

    # Test para verificar la inicialización del objeto Bishop
    def test_init(self):
        bishop = Bishop("WHITE")  # Creo objeto de la Clase Bishop
        self.assertIsInstance(bishop, Bishop)  # Verifica que es una instancia de Bishop
        self.assertEqual(bishop.color, "WHITE")  # Verifica que el color es "WHITE"
        
        bishop_black = Bishop("BLACK")  # Creo objeto de la Clase Bishop con color "BLACK"
        self.assertEqual(bishop_black.color, "BLACK")  # Verifica que el color es "BLACK"


    # Test para verificar el movimiento diagonal
    def test_diagonal_movement(self):
        bishop = Bishop("WHITE")
        self.assertEqual(bishop.diagonal_movement(2, 4, 2, 4), "diagonal")  # Movimiento diagonal válido
        self.assertEqual(bishop.diagonal_movement(3, 5, 3, 5), "diagonal")  # Otro movimiento diagonal válido
        self.assertEqual(bishop.diagonal_movement(1, 3, 1, 4), "invalid")   # Movimiento no diagonal (inválido)
        self.assertEqual(bishop.diagonal_movement(2, 3, 2, 5), "invalid")   # Otro movimiento no diagonal (inválido)

    # Test para verificar si el movimiento es válido
    def test_is_valid_movement(self):
        bishop = Bishop("WHITE")
        self.assertTrue(bishop.is_valid_movement("diagonal"))  # Verifica que un movimiento diagonal es válido
        self.assertFalse(bishop.is_valid_movement("invalid"))  # Verifica que un movimiento no diagonal es inválido




if __name__ == '__main__':
    unittest.main()