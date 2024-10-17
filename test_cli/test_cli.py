import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from contextlib import redirect_stdout
from game.chess import Chess
from cli import Cli

class TestCli(unittest.TestCase):
    def setUp(self):
        self.cli = Cli()
        self.cli.chess = MagicMock(spec=Chess)
        self.cli.chess.__mutual_agreement_to_end__ = False
        self.cli.chess.__board__ = MagicMock()
        self.cli.chess.__board__.__king_captured__ = False

    @patch('builtins.input')
    def test_run_quit(self, mock_input):
        mock_input.return_value = '4'
        with redirect_stdout(StringIO()):  # Captura la salida estándar
            self.cli.run()
        self.assertTrue(self.cli.running) 

    @patch('builtins.input')
    def test_handle_move(self, mock_input):
        mock_input.side_effect = ['62', '64']
        self.cli.chess.play_move.return_value = "VALID"
        with redirect_stdout(StringIO()):  # Captura la salida estándar
            self.cli.handle_move()
        self.cli.chess.play_move.assert_called_once_with('62', '64')

    @patch('builtins.input')
    def test_handle_pawn_promotion(self, mock_input):
        mock_input.return_value = '1'
        with redirect_stdout(StringIO()):  # Captura la salida estándar
            self.cli.handle_pawn_promotion((7, 0))
        self.cli.chess.promote_pawn.assert_called_once_with(7, 0, '1')

    def test_handle_view_score(self):
        self.cli.chess.get_captures.return_value = {
            '__white_captures__': ['Pawn', 'Knight'],
            '__black_captures__': ['Pawn']
        }
        with redirect_stdout(StringIO()):  # Captura la salida estándar
            self.cli.handle_view_score()

    @patch('builtins.input')
    def test_handle_end_game_agreement_yes(self, mock_input):
        mock_input.return_value = 'y'
        with redirect_stdout(StringIO()):  # Captura la salida estándar
            result = self.cli.handle_end_game_agreement()
        self.assertTrue(result)
        self.cli.chess.end_game_by_agreement.assert_called_once()

    @patch('builtins.input')
    def test_handle_end_game_agreement_no(self, mock_input):
        mock_input.return_value = 'n'
        with redirect_stdout(StringIO()):  # Captura la salida estándar
            result = self.cli.handle_end_game_agreement()
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()