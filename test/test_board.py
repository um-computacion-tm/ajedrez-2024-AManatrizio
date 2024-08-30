import unittest
from game.board import Board
from game.rook import Rook
from game.king import King
from game.knight import Knight
from game.bishop import Bishop
from game.queen import Queen
from game.pawn import Pawn

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
        self.assertEqual(board.matrix[0][0].color,"WHITE")
        self.assertEqual(board.matrix[7][3].color,"BLACK")

    def test_is_out_of_board(self):
        board = Board()
        # Posicion dentro del tablero
        self.assertTrue(board.is_out_of_board(0,0))
        # Posicion fuera del tablero
        self.assertFalse(board.is_out_of_board(9,9))


    def test_get_piece_color(self):
        board = Board()
        # Una negra
        color = board.get_color(7, 3)
        self.assertEqual(color, "BLACK")
        # Una blanca
        color = board.get_color(0, 0)
        self.assertEqual(color, "WHITE")
        

        

        






if __name__ == '__main__':
    unittest.main()