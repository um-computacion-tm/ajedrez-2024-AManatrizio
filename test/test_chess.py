import unittest
from game.chess import Chess
from game.board import Board

class TestChess(unittest.TestCase):

    def test_init(self):
        chess = Chess()  # Creo objeto Chess de la clase Chess
        # Verifica que se crea el objeto board dentro de Chess
        self.assertIsInstance(chess.board, Board)
        # Verifica que el jugador actual inicial sea "WHITE"
        self.assertEqual(chess.current_player, "WHITE")

    def test_switch_turn(self):
        chess = Chess()  # Creo objeto Chess de la clase Chess
        # Verifica que el turno se cambie correctamente
        chess.switch_turn()
        self.assertEqual(chess.current_player, "BLACK")
        chess.switch_turn()
        self.assertEqual(chess.current_player, "WHITE")

    def test_parse_move(self):
        chess = Chess()  # Creo objeto Chess de la clase Chess
        move = "12"  # Movimiento en formato cadena
        fila, columna = chess.parse_move(move)
        # Verifica que se convierte el movimiento a fila y columna correctamente
        self.assertEqual(fila, 1)
        self.assertEqual(columna, 2)

    def test_play_valid_move(self):
        chess = Chess()  # Creo objeto Chess de la clase Chess
        # Mock para que is_valid_move devuelva True
        chess.board.is_valid_move = lambda p_fila, p_columna, m_fila, m_columna: True
        # Mock para que move_piece no realice ninguna operación
        chess.board.move_piece = lambda p_fila, p_columna, m_fila, m_columna: None

        result = chess.play_move("12", "34")  # Intento un movimiento válido
        # Verifica que el movimiento fue exitoso
        self.assertTrue(result)
        # Verifica que el turno haya cambiado a "BLACK"
        self.assertEqual(chess.current_player, "BLACK")

    def test_play_invalid_move(self):
        chess = Chess()  # Creo objeto Chess de la clase Chess
        # Mock para que is_valid_move devuelva False
        chess.board.is_valid_move = lambda p_fila, p_columna, m_fila, m_columna: False

        result = chess.play_move("12", "34")  # Intento un movimiento inválido
        # Verifica que el movimiento fue fallido
        self.assertFalse(result)
        # Verifica que el turno no haya cambiado y siga siendo "WHITE"
        self.assertEqual(chess.current_player, "WHITE")


if __name__ == "__main__":
    unittest.main()
