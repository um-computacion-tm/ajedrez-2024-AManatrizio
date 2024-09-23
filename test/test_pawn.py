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

    def test_is_valid_movement(self):
        self._test_pawn_movement(self.black_pawn, 1, 2, 3, 0)

    def _test_pawn_movement(self, pawn, start_row, one_step, two_step, back_step):
        # Primer movimiento
        self.assertTrue(pawn.is_valid_movement(start_row, 0, one_step, 0))  # Un paso adelante
        self.assertTrue(pawn.is_valid_movement(start_row, 0, two_step, 0))  # Dos pasos adelante
        self.assertFalse(pawn.is_valid_movement(start_row, 0, two_step + 1, 0))  # Tres pasos adelante (inválido)

        # Movimiento diagonal (captura)
        self.assertTrue(pawn.is_valid_movement(start_row, 0, one_step, 1))  # Captura a la derecha
        self.assertTrue(pawn.is_valid_movement(start_row, 1, one_step, 0))  # Captura a la izquierda

        # Movimientos inválidos
        self.assertFalse(pawn.is_valid_movement(start_row, 0, start_row, 1))  # Movimiento lateral
        self.assertFalse(pawn.is_valid_movement(start_row, 0, back_step, 0))  # Movimiento hacia atrás

        # Después del primer movimiento
        pawn.complete_move()
        self.assertTrue(pawn.is_valid_movement(one_step, 0, two_step, 0))  # Un paso adelante
        self.assertFalse(pawn.is_valid_movement(one_step, 0, two_step + 1, 0))  # Dos pasos adelante (ya no válido)

    def test_complete_move(self):
        self.assertTrue(self.white_pawn.first_move)
        self.white_pawn.complete_move()
        self.assertFalse(self.white_pawn.first_move)

        self.assertTrue(self.black_pawn.first_move)
        self.black_pawn.complete_move()
        self.assertFalse(self.black_pawn.first_move)

if __name__ == '__main__':
    unittest.main()