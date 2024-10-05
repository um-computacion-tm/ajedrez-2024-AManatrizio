import unittest
from unittest.mock import MagicMock, patch
from game.chess import Chess
from game.board import Board

class TestChess(unittest.TestCase):

    def test_init(self):
        chess = Chess()
        self.assertIsInstance(chess.__board__, Board)
        self.assertEqual(chess.__current_player__, "WHITE")

    def test_switch_turn(self):
        chess = Chess()
        chess.switch_turn()
        self.assertEqual(chess.__current_player__, "BLACK")
        chess.switch_turn()
        self.assertEqual(chess.__current_player__, "WHITE")

    def test_parse_move(self):
        chess = Chess()
        move = "12"
        fila, columna = chess.parse_move(move)
        self.assertEqual(fila, 1)
        self.assertEqual(columna, 2)

    def test_play_invalid_move(self):
        chess = Chess()
        chess.__board__.is_valid_move = MagicMock(return_value=False)

        result = chess.play_move("12", "34")
        self.assertFalse(result)
        self.assertEqual(chess.__current_player__, "WHITE")

    def test_get_captures(self):
        chess = Chess()
        # Simulamos que get_capture_counts retorna un diccionario
        chess.__board__.get_capture_counts = MagicMock(return_value={"__white_captures__": 2, "__black_captures__": 3})
        
        captures = chess.get_captures()
        self.assertEqual(captures, {"__white_captures__": 2, "__black_captures__": 3})

    def test_play_move_wrong_turn(self):
        chess = Chess()
        # Intentar mover una pieza negra en el turno de las blancas
        result = chess.play_move("10", "30")
        self.assertFalse(result)
        self.assertEqual(chess.__current_player__, "WHITE")

    def test_play_move_empty_square(self):
        chess = Chess()
        # Intentar mover desde una casilla vacía
        result = chess.play_move("40", "50")
        self.assertFalse(result)

    def test_play_move_capture(self):
        chess = Chess()
        # Simular una captura
        chess.__board__.is_valid_move = MagicMock(return_value=True)
        chess.__board__.has_piece = MagicMock(return_value=True)
        chess.__board__.get_color = MagicMock(side_effect=["WHITE", "BLACK"])
        chess.__board__.move_piece = MagicMock()
        #chess.__board__.update_capture_count = MagicMock()

        # result = chess.play_move("60", "51")
        # self.assertTrue(result)
        # chess.__board__.update_capture_count.assert_called_once_with("BLACK")

    def test_display___board__(self):
        chess = Chess()
        # Mock para verificar que se llame al método display___board__ del __board__
        chess.__board__.display_board= MagicMock()
        
        chess.__board__.display_board()
        chess.__board__.display_board.assert_called_once()

class TestChessAdditional(unittest.TestCase):

    def test_is_over_by_captures(self):
        chess = Chess()
        
        # Caso: No terminado
        chess.__board__.__white_captures__ = 14
        chess.__board__.__black_captures__ = 14
        self.assertFalse(chess.is_over())
        
        # Caso: Terminado por capturas blancas
        chess.__board__.__white_captures__ = 15
        self.assertTrue(chess.is_over())
        
        # Caso: Terminado por capturas negras
        chess.__board__.__white_captures__ = 14
        chess.__board__.__black_captures__ = 15
        self.assertTrue(chess.is_over())

    def test_is_over_by_king_capture(self):
        chess = Chess()
        
        # Caso: Rey no capturado
        chess.__board__.__king_captured__ = False
        self.assertFalse(chess.is_over())
        
        # Caso: Rey capturado
        chess.__board__.__king_captured__ = True
        self.assertTrue(chess.is_over())

    @patch('builtins.print')
    def test_play_move_detailed(self, mock_print):
        chess = Chess()
        chess.__board__.is_valid_move = MagicMock(return_value=True)
        chess.__board__.has_piece = MagicMock(return_value=False)
        chess.__board__.get_color = MagicMock(return_value="WHITE")
        chess.__board__.move_piece = MagicMock()

        result = chess.play_move("60", "40")
        

    def test_play_move_capture_own_piece(self):
        chess = Chess()
        chess.__board__.has_piece = MagicMock(return_value=True)
        chess.__board__.get_color = MagicMock(return_value="WHITE")

        result = chess.play_move("60", "70")
        
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
