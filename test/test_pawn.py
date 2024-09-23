import unittest
from game.pawn import Pawn
from .test_utils import TestUtils

class TestPawn(unittest.TestCase):

    def setUp(self):
        self.white_pawn = Pawn("WHITE")
        self.black_pawn = Pawn("BLACK")

    def test_pawn_str(self):
        utils = TestUtils()
        utils.check_piece_str(self, Pawn, "♙", "♟")

    def test_init(self):
        self.assertIsInstance(self.white_pawn, Pawn)
        self.assertEqual(self.white_pawn.color, "WHITE")
        self.assertTrue(self.white_pawn.first_move)

        self.assertIsInstance(self.black_pawn, Pawn)
        self.assertEqual(self.black_pawn.color, "BLACK")
        self.assertTrue(self.black_pawn.first_move)

    def test_is_valid_movement_white(self):
        # Primer movimiento
        self.assertTrue(self.white_pawn.is_valid_movement(6, 0, 5, 0))  # Un paso adelante
        self.assertTrue(self.white_pawn.is_valid_movement(6, 0, 4, 0))  # Dos pasos adelante
        self.assertFalse(self.white_pawn.is_valid_movement(6, 0, 3, 0))  # Tres pasos adelante (inválido)

        # Movimiento diagonal (captura)
        self.assertTrue(self.white_pawn.is_valid_movement(6, 0, 5, 1))  # Captura a la derecha
        self.assertTrue(self.white_pawn.is_valid_movement(6, 1, 5, 0))  # Captura a la izquierda

        # Movimientos inválidos
        self.assertFalse(self.white_pawn.is_valid_movement(6, 0, 6, 1))  # Movimiento lateral
        self.assertFalse(self.white_pawn.is_valid_movement(6, 0, 7, 0))  # Movimiento hacia atrás

        # Después del primer movimiento
        self.white_pawn.complete_move()
        self.assertTrue(self.white_pawn.is_valid_movement(5, 0, 4, 0))  # Un paso adelante
        self.assertFalse(self.white_pawn.is_valid_movement(5, 0, 3, 0))  # Dos pasos adelante (ya no válido)

    def test_is_valid_movement_black(self):
        # Primer movimiento
        self.assertTrue(self.black_pawn.is_valid_movement(1, 0, 2, 0))  # Un paso adelante
        self.assertTrue(self.black_pawn.is_valid_movement(1, 0, 3, 0))  # Dos pasos adelante
        self.assertFalse(self.black_pawn.is_valid_movement(1, 0, 4, 0))  # Tres pasos adelante (inválido)

        # Movimiento diagonal (captura)
        self.assertTrue(self.black_pawn.is_valid_movement(1, 0, 2, 1))  # Captura a la derecha
        self.assertTrue(self.black_pawn.is_valid_movement(1, 1, 2, 0))  # Captura a la izquierda

        # Movimientos inválidos
        self.assertFalse(self.black_pawn.is_valid_movement(1, 0, 1, 1))  # Movimiento lateral
        self.assertFalse(self.black_pawn.is_valid_movement(1, 0, 0, 0))  # Movimiento hacia atrás

        # Después del primer movimiento
        self.black_pawn.complete_move()
        self.assertTrue(self.black_pawn.is_valid_movement(2, 0, 3, 0))  # Un paso adelante
        self.assertFalse(self.black_pawn.is_valid_movement(2, 0, 4, 0))  # Dos pasos adelante (ya no válido)

    def test_complete_move(self):
        self.assertTrue(self.white_pawn.first_move)
        self.white_pawn.complete_move()
        self.assertFalse(self.white_pawn.first_move)

        self.assertTrue(self.black_pawn.first_move)
        self.black_pawn.complete_move()
        self.assertFalse(self.black_pawn.first_move)

if __name__ == '__main__':
    unittest.main()