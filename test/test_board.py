import unittest
from game.board import Board
from game.rook import Rook

class TestBoard(unittest.TestCase):
    
    def test_init(self):
        board = Board() # Creo objeto borad de la Clase Board
        self.assertEqual(
            len(board.matrix),8)
        for i in range(8):
            self.assertEqual(len(board.matrix[i]),8)

    def test_piece(self):
        board = Board() # Se crea objeto board de la Clase Board
        # assertIsInstance Verifica si un objeto pertenece a una clase 
        # específica o a una subclase de esa clase
        self.assertIsInstance(board.matrix[0][0],Rook)
        # assertEqual Verifica que a es igual a b.
        self.assertEqual(board.matrix[0][0].color,"WHITE")




if __name__ == '__main__':
    unittest.main()