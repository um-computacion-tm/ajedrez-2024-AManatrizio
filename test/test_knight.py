import unittest
from game.knight import Knight

class TestKnight(unittest.TestCase):

    def setUp(self):
        self.knight = Knight("WHITE")  # Crea un objeto Knight blanco para usar en las pruebas

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
        # Movimientos válidos en forma de L
        self.assertTrue(self.knight.is_valid_movement(0, 2, 0, 1))  # Dos casillas verticales y una horizontal

    def test_invalid_movement(self):
        # Movimientos inválidos que no forman una "L"
        self.assertFalse(self.knight.is_valid_movement(0, 3, 0, 1))  # Movimiento inválido





if __name__ == "__main__":
    unittest.main()
