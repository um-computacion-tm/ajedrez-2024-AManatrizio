import unittest
from game.pawn import Pawn

class TestPawn(unittest.TestCase):
    def test_init(self):
        pawn = Pawn("WHITE")  # Creo objeto pawn de la Clase Pawn
        self.assertIsInstance(pawn, Pawn)  # Verifica que pawn es una instancia de Pawn

    def test_str(self):
        white_pawn = Pawn("WHITE")
        black_pawn= Pawn("BLACK")
        self.assertEqual(str(white_pawn), "♙")  # Verifica la representación en cadena para WHITE
        self.assertEqual(str(black_pawn), "♟")  # Verifica la representación en cadena para BLACK

    def test_first_move(self):
        pawn = Pawn("WHITE")  # Creo objeto pawn de la Clase Pawn
        # El primer movimiento puede ser dos casillas hacia adelante
        self.assertTrue(pawn.is_valid_movement(1, 3, 0, 0))

    def test_second_move_one_square(self):
        pawn = Pawn("WHITE")
        # Simulamos que el primer movimiento ya se hizo
        pawn.first_move = False
        # Movimiento de una casilla hacia adelante después del primer movimiento
        self.assertTrue(pawn.is_valid_movement(3, 4, 0, 0))
    
    def test_invalid_first_move_three_squares(self):
        pawn = Pawn("WHITE")
        # Un peón no puede moverse tres casillas hacia adelante
        self.assertFalse(pawn.is_valid_movement(1, 4, 0, 0))
    
    def test_move_in_same_column(self):
        pawn = Pawn("BLACK")
        # Movimiento en la misma columna, que es válido para peones
        self.assertTrue(pawn.is_valid_movement(1, 2, 0, 0))  # Movimiento normal de una casilla

    def test_invalid_diagonal_move(self):
        pawn = Pawn("BLACK")
        # Movimiento diagonal inválido sin capturar otra pieza
        self.assertFalse(pawn.is_valid_movement(1, 2, 0, 1))



if __name__ == '__main__':
    unittest.main()