import unittest
from game.board import Board
from game.rook import Rook
from game.king import King
from game.knight import Knight
from game.bishop import Bishop
from game.queen import Queen
from game.pawn import Pawn
from unittest.mock import patch
from io import StringIO

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()  # Crea una instancia de Board para usar en las pruebas

    def test_init(self):
        # Testea que se crea el tablero de 8x8
        self.assertEqual(len(self.board.matrix), 8)
        for row in self.board.matrix:
            self.assertEqual(len(row), 8)

    def test_piece(self):
        # Verifica la correcta colocación de piezas iniciales
        self.assertIsInstance(self.board.matrix[0][0], Rook)
        self.assertIsInstance(self.board.matrix[0][7], Rook)
        self.assertIsInstance(self.board.matrix[0][1], Knight)
        self.assertIsInstance(self.board.matrix[0][6], Knight)
        self.assertIsInstance(self.board.matrix[0][2], Bishop)
        self.assertIsInstance(self.board.matrix[0][5], Bishop)
        self.assertIsInstance(self.board.matrix[0][3], Queen)
        self.assertIsInstance(self.board.matrix[0][4], King)
        self.assertEqual(self.board.matrix[0][0].color, "BLACK")
        self.assertEqual(self.board.matrix[7][3].color, "WHITE")

    def test_is_out_of_board(self):
        # Verifica si una posición está dentro o fuera del tablero
        self.assertTrue(self.board.is_out_of_board(0, 0))
        self.assertFalse(self.board.is_out_of_board(9, 9))
        self.assertFalse(self.board.is_out_of_board(8, 8))

    def test_get_color(self):
        # Verifica el color de la pieza en una posición específica
        self.assertEqual(self.board.get_color(7, 3), "WHITE")
        self.assertEqual(self.board.get_color(0, 0), "BLACK")

    def test_has_piece(self):
        # Verifica si hay una pieza en una posición específica
        self.assertTrue(self.board.has_piece(0, 0))
        self.assertFalse(self.board.has_piece(4, 4))  # Asumiendo que esta posición está vacía

    def test_is_valid_move(self):
        # Verifica la validez de los movimientos
        self.assertTrue(self.board.is_valid_move(0, 0, 1, 0))  # Movimiento válido
        self.assertFalse(self.board.is_valid_move(0, 0, 8, 8))  # Movimiento inválido

    def test_is_path_clear(self):
        self.assertTrue(self.board.is_path_clear(3, 0, 3, 7, 'horizontal'))

    def test_horizontal_path_blocked(self):
        # Verifica si un camino horizontal está bloqueado
        self.assertFalse(self.board.is_path_clear(0, 0, 0, 7, 'horizontal'))

    def test_vertical_path_blocked(self):
        # Coloca una pieza en el camino vertical y verifica si está bloqueado
        self.board.matrix[3][0] = Pawn(color="BLACK")  # Coloca una pieza en el camino
        self.assertFalse(self.board.is_path_clear(1, 0, 4, 0, 'vertical'))

    def test_display_board(self):
        # Verifica la salida de la representación del tablero
        expected_output = (
            "    0   1   2   3   4   5   6   7\n"
            "  +---+---+---+---+---+---+---+---+\n"
            "0 | ♜ | ♞ | ♝ | ♛ | ♚ | ♝ | ♞ | ♜ | 0\n"
            "  +---+---+---+---+---+---+---+---+\n"
            "1 | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ | 1\n"
            "  +---+---+---+---+---+---+---+---+\n"
            "2 |   |   |   |   |   |   |   |   | 2\n"
            "  +---+---+---+---+---+---+---+---+\n"
            "3 |   |   |   |   |   |   |   |   | 3\n"
            "  +---+---+---+---+---+---+---+---+\n"
            "4 |   |   |   |   |   |   |   |   | 4\n"
            "  +---+---+---+---+---+---+---+---+\n"
            "5 |   |   |   |   |   |   |   |   | 5\n"
            "  +---+---+---+---+---+---+---+---+\n"
            "6 | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | 6\n"
            "  +---+---+---+---+---+---+---+---+\n"
            "7 | ♖ | ♘ | ♗ | ♕ | ♔ | ♗ | ♘ | ♖ | 7\n"
            "  +---+---+---+---+---+---+---+---+\n"
            "    0   1   2   3   4   5   6   7\n"
        )

        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.board.display_board()
            actual_output = fake_output.getvalue()

        self.assertEqual(actual_output, expected_output)



if __name__ == '__main__':
    unittest.main()
