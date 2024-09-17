import unittest
from game.knight import Knight

class TestKnight(unittest.TestCase):

    def test_init(self):
        # Crea un objeto Knight de color blanco
        white_knight = Knight("WHITE")
        # Verifica que se ha inicializado correctamente como un objeto Knight
        self.assertEqual(white_knight.color, "WHITE")
        self.assertEqual(str(white_knight), "♘")  # Verifica la representación del caballo blanco
        
        # Crea un objeto Knight de color negro
        black_knight = Knight("BLACK")
        # Verifica que se ha inicializado correctamente como un objeto Knight
        self.assertEqual(black_knight.color, "BLACK")
        self.assertEqual(str(black_knight), "♞")  # Verifica la representación del caballo negro

    def test_valid_movement(self):
        knight = Knight("WHITE")  # Crea un objeto Knight blanco
        
        # Movimientos válidos en forma de L
        self.assertTrue(knight.is_valid_movement(0, 2, 0, 1))  # Dos casillas verticales y una horizontal
        self.assertTrue(knight.is_valid_movement(0, 1, 0, 2))  # Una casilla vertical y dos horizontales
        self.assertTrue(knight.is_valid_movement(3, 5, 4, 3))  # Otro movimiento en L válido
        
    def test_invalid_movement(self):
        knight = Knight("WHITE")  # Crea un objeto Knight blanco
        
        # Movimientos inválidos que no forman una "L"
        self.assertFalse(knight.is_valid_movement(0, 3, 0, 1))  # Movimiento inválido
        self.assertFalse(knight.is_valid_movement(1, 1, 0, 2))  # Movimiento inválido
        self.assertFalse(knight.is_valid_movement(4, 6, 2, 2))  # Movimiento inválido






if __name__ == "__main__":
    unittest.main()
