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

    @patch('builtins.input', side_effect=['1', '62', '64', '4'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_run_make_move_and_quit(self, mock_stdout, mock_input):
        self.cli.run()
        output = mock_stdout.getvalue()
        self.assertIn("Enter your piece to move:", output)
        self.assertIn("Enter where to move:", output)
        self.assertIn("Quitting the game.", output)

    @patch('builtins.input', side_effect=['2', '4'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_run_view_score_and_quit(self, mock_stdout, mock_input):
        self.cli.run()
        output = mock_stdout.getvalue()
        self.assertIn("White captures:", output)
        self.assertIn("Black captures:", output)
        self.assertIn("Quitting the game.", output)

    @patch('game.chess.Chess.is_over', side_effect=[False, True])
    @patch('game.chess.Chess.display_board')
    @patch('game.chess.Chess.get_captures', return_value={'__white_captures__': [], '__black_captures__': []})
    @patch('game.chess.Chess.end_game_by_agreement')
    @patch('builtins.input', side_effect=['3', 'y'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_run_end_game_by_agreement(self, mock_stdout, mock_input, mock_end_game, mock_get_captures, mock_display_board, mock_is_over):
        self.cli.run()
        output = mock_stdout.getvalue()
        print("Debug - Captured output:", output)  
        # Verificar que el juego ha terminado
        self.assertFalse(self.cli.running)

    @patch('game.chess.Chess.play_move')
    @patch('builtins.input', return_value='62')
    @patch('sys.stdout', new_callable=StringIO)
    def test_handle_move_valid(self, mock_stdout, mock_input, mock_play_move):
        mock_play_move.return_value = "VALID"
        self.cli.handle_move()
        mock_play_move.assert_called_once()
        self.assertEqual(mock_play_move.call_args[0], ('62', '62'))

    @patch('game.chess.Chess.play_move')
    @patch('builtins.input', side_effect=['62', '64'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_handle_move_promotion(self, mock_stdout, mock_input, mock_play_move):
        mock_play_move.return_value = ("PROMOTION_NEEDED", (7, 4))
        with patch.object(self.cli, 'handle_pawn_promotion') as mock_promotion:
            self.cli.handle_move()
            mock_promotion.assert_called_once_with((7, 4))

    @patch('game.chess.Chess.promote_pawn')
    @patch('builtins.input', return_value='1')
    @patch('sys.stdout', new_callable=StringIO)
    def test_handle_pawn_promotion(self, mock_stdout, mock_input, mock_promote_pawn):
        mock_promote_pawn.return_value = "Queen"
        self.cli.handle_pawn_promotion((7, 4))
        mock_promote_pawn.assert_called_once_with(7, 4, '1')

if __name__ == '__main__':
    unittest.main()