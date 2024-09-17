import unittest
from game.board import Board
from game.rook import Rook
from game.king import King
from game.knight import Knight
from game.bishop import Bishop
from game.queen import Queen
from game.pawn import Pawn
from game.piece import Piece
from unittest.mock import patch
from io import StringIO

class TestBoard(unittest.TestCase):
    
    def test_init(self):
        board = Board() # Creo objeto board de la Clase Board
        # Testea que se crea el tablero de 8x8
        self.assertEqual(
            len(board.matrix),8)
        for i in range(8):
            self.assertEqual(len(board.matrix[i]),8)

    def test_piece(self):
        board = Board() # Se crea objeto board de la Clase Board
        # assertIsInstance Verifica si un objeto pertenece a una clase 
        # específica o a una subclase de esa clase
        self.assertIsInstance(board.matrix[0][0],Rook)
        self.assertIsInstance(board.matrix[0][7],Rook)
        self.assertIsInstance(board.matrix[0][1],Knight)
        self.assertIsInstance(board.matrix[0][6],Knight)
        self.assertIsInstance(board.matrix[0][2],Bishop)
        self.assertIsInstance(board.matrix[0][5],Bishop)
        self.assertIsInstance(board.matrix[0][3],Queen)
        self.assertIsInstance(board.matrix[0][4],King)

        # assertEqual Verifica que a es igual a b.
        self.assertEqual(board.matrix[0][0].color,"BLACK")
        self.assertEqual(board.matrix[7][3].color,"WHITE")

    def test_is_out_of_board(self):
        board = Board()
        # Posicion dentro del tablero
        self.assertTrue(board.is_out_of_board(0,0))
        # Posicion fuera del tablero
        self.assertFalse(board.is_out_of_board(9,9))
        self.assertFalse(board.is_out_of_board(8,8))



    def test_get_color(self):
        board = Board()
        # Una negra
        color = board.get_color(7, 3)
        self.assertEqual(color, "WHITE")
        # Una blanca
        color = board.get_color(0, 0)
        self.assertEqual(color, "BLACK")
    
    def test_has_piece(self):
        board = Board()  # Crea una instancia de Board
        self.assertTrue(board.has_piece(0, 0))
        self.assertFalse(board.has_piece(4, 4))  # Asumiendo que esta posición está vacía

    def test_is_valid_move(self):
        board = Board()

        # Movimiento válido para una torre (0,0 a 1,0)
        self.assertTrue(board.is_valid_move(0, 0, 1, 0))

        # Movimiento inválido: fuera del tablero
        self.assertFalse(board.is_valid_move(0, 0, 8, 8))



    
    def test_is_path_clear(self):
        board = Board()
        self.assertTrue(board.is_path_clear(3, 0, 3, 7, 'horizontal'))
    
    def test_horizontal_path_blocked(self):
        board = Board()
        # Bloqueamos una posición en el camino horizontal
        self.assertFalse(board.is_path_clear(0, 0, 0, 7, 'horizontal'))

    def test_vertical_path_clear(self):
        board = Board()
        # Camino vertical despejado
        self.assertTrue(board.is_path_clear(1, 0, 1, 4, 'vertical'))

    def test_vertical_path_blocked(self):
        board = Board()
        board.matrix[3][0] = Pawn(color="BLACK")  # Coloca una pieza en el camino
        self.assertFalse(board.is_path_clear(1, 0, 4, 0, 'vertical'))
       
        
    def test_diagonal_path_clear(self):
        board = Board()
        # Camino diagonal despejado
        self.assertTrue(board.is_path_clear(2, 0, 3, 1, 'diagonal'))


    def test_display_board(self):
        board = Board()
        self.maxDiff = None  # Permite ver todo el diff cuando hay un error
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

        # Usar patch para capturar la salida de print
        with patch('sys.stdout', new=StringIO()) as fake_output:
            board.display_board()
            actual_output = fake_output.getvalue()

        print("Actual output:")
        print(actual_output)
        print("Expected output:")
        print(expected_output)

        self.assertEqual(actual_output, expected_output)




        

if __name__ == '__main__':
    unittest.main()