import unittest
from unittest.mock import MagicMock, patch
from game.chess import Chess
from game.board import Board

class TestChess(unittest.TestCase):

    def test_init(self):
        chess = Chess()
        self.assertIsInstance(chess.board, Board)
        self.assertEqual(chess.current_player, "WHITE")

    def test_switch_turn(self):
        chess = Chess()
        chess.switch_turn()
        self.assertEqual(chess.current_player, "BLACK")
        chess.switch_turn()
        self.assertEqual(chess.current_player, "WHITE")

    def test_parse_move(self):
        chess = Chess()
        move = "12"
        fila, columna = chess.parse_move(move)
        self.assertEqual(fila, 1)
        self.assertEqual(columna, 2)



    def test_play_invalid_move(self):
        chess = Chess()
        chess.board.is_valid_move = MagicMock(return_value=False)

        result = chess.play_move("12", "34")
        self.assertFalse(result)
        self.assertEqual(chess.current_player, "WHITE")

    def test_get_captures(self):
        chess = Chess()
        # Simulamos que get_capture_counts retorna un diccionario
        chess.board.get_capture_counts = MagicMock(return_value={"white_captures": 2, "black_captures": 3})
        
        captures = chess.get_captures()
        self.assertEqual(captures, {"white_captures": 2, "black_captures": 3})


    def test_play_move_wrong_turn(self):
        chess = Chess()
        # Intentar mover una pieza negra en el turno de las blancas
        result = chess.play_move("10", "30")
        self.assertFalse(result)
        self.assertEqual(chess.current_player, "WHITE")

    def test_play_move_empty_square(self):
        chess = Chess()
        # Intentar mover desde una casilla vacía
        result = chess.play_move("40", "50")
        self.assertFalse(result)

    def test_play_move_capture(self):
        chess = Chess()
        # Simular una captura
        chess.board.is_valid_move = MagicMock(return_value=True)
        chess.board.has_piece = MagicMock(return_value=True)
        chess.board.get_color = MagicMock(side_effect=["WHITE", "BLACK"])
        chess.board.move_piece = MagicMock()
        chess.board.update_capture_count = MagicMock()

        result = chess.play_move("60", "51")
        self.assertTrue(result)
        chess.board.update_capture_count.assert_called_once_with("BLACK")

    def test_display_board(self):
        chess = Chess()
        # Mock para verificar que se llame al método display_board del board
        chess.board.display_board = MagicMock()
        
        chess.display_board()
        chess.board.display_board.assert_called_once()

class TestChessAdditional(unittest.TestCase):

    def test_is_over_by_captures(self):
        chess = Chess()
        
        # Caso: No terminado
        chess.board.white_captures = 14
        chess.board.black_captures = 14
        self.assertFalse(chess.is_over())
        
        # Caso: Terminado por capturas blancas
        chess.board.white_captures = 15
        self.assertTrue(chess.is_over())
        
        # Caso: Terminado por capturas negras
        chess.board.white_captures = 14
        chess.board.black_captures = 15
        self.assertTrue(chess.is_over())

    def test_is_over_by_king_capture(self):
        chess = Chess()
        
        # Caso: Rey no capturado
        chess.board.king_captured = False
        self.assertFalse(chess.is_over())
        
        # Caso: Rey capturado
        chess.board.king_captured = True
        self.assertTrue(chess.is_over())

    @patch('builtins.print')
    def test_play_move_detailed(self, mock_print):
        chess = Chess()
        chess.board.is_valid_move = MagicMock(return_value=True)
        chess.board.has_piece = MagicMock(return_value=False)
        chess.board.get_color = MagicMock(return_value="WHITE")
        chess.board.move_piece = MagicMock()

        result = chess.play_move("60", "40")
        
        # self.assertTrue(result)
        # mock_print.assert_any_call("Intentando mover pieza 60 a 40")
        # mock_print.assert_any_call("Movimiento válido")
        # mock_print.assert_any_call("Posiciones convertidas: inicial (6, 0), final (4, 0)")
        # mock_print.assert_any_call("Turno de: BLACK")

    def test_play_move_capture_own_piece(self):
        chess = Chess()
        chess.board.has_piece = MagicMock(return_value=True)
        chess.board.get_color = MagicMock(return_value="WHITE")

        result = chess.play_move("60", "70")
        
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
