import unittest
from game.board import Board
from game.rook import Rook
from game.king import King
from game.knight import Knight
from game.bishop import Bishop
from game.queen import Queen
from game.pawn import Pawn
from game.exceptions import OutOfBoardError
from unittest.mock import patch
from io import StringIO

class TestBoardSetup(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_init(self):
        self.assertEqual(len(self.board.__matrix__), 8)
        for row in self.board.__matrix__:
            self.assertEqual(len(row), 8)

    def test_piece(self):
        self.assertIsInstance(self.board.__matrix__[0][0], Rook)
        self.assertIsInstance(self.board.__matrix__[0][7], Rook)
        self.assertIsInstance(self.board.__matrix__[0][1], Knight)
        self.assertIsInstance(self.board.__matrix__[0][6], Knight)
        self.assertIsInstance(self.board.__matrix__[0][2], Bishop)
        self.assertIsInstance(self.board.__matrix__[0][5], Bishop)
        self.assertIsInstance(self.board.__matrix__[0][3], Queen)
        self.assertIsInstance(self.board.__matrix__[0][4], King)
        self.assertEqual(self.board.__matrix__[0][0].__color__, "BLACK")
        self.assertEqual(self.board.__matrix__[7][3].__color__, "WHITE")

class TestBoardHelperMethods(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_is_out_of_board(self):
        self.assertFalse(self.board.is_out_of_board(0, 0))
        self.assertFalse(self.board.is_out_of_board(7, 7))
        
        with self.assertRaises(OutOfBoardError):
            self.board.is_out_of_board(-1, 0)
        
        with self.assertRaises(OutOfBoardError):
            self.board.is_out_of_board(0, 8)

    def test_get_color(self):
        self.assertEqual(self.board.get_color(7, 3), "WHITE")
        self.assertEqual(self.board.get_color(0, 0), "BLACK")

    def test_has_piece(self):
        self.assertTrue(self.board.has_piece(0, 0))
        self.assertFalse(self.board.has_piece(4, 4))

    # def test_is_valid_move(self):
    #     self.assertTrue(self.board.is_valid_move(0, 0, 1, 0))  # Movimiento válido hacia adelante

class TestBoardPathClear(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_is_path_clear(self):
        self.assertTrue(self.board.is_path_clear(3, 0, 3, 7, 'horizontal'))

    def test_is_path_clear_blocked(self):
            test_cases = [
                # start_row, start_col, end_row, end_col, block_row, block_col, direction
                (0, 0, 0, 3, 0, 2, "horizontal"),
                (0, 0, 3, 0, 2, 0, "vertical"),
                (0, 0, 3, 3, 2, 2, "diagonal"),
            ]

            for start_row, start_col, end_row, end_col, block_row, block_col, direction in test_cases:
                with self.subTest(f"{direction} from ({start_row},{start_col}) to ({end_row},{end_col})"):
                    self.board.__matrix__[block_row][block_col] = Pawn("BLACK")
                    self.assertFalse(self.board.is_path_clear(start_row, start_col, end_row, end_col, direction))
    
    def test_is_path_clear_invalid_movement(self):
        self.assertFalse(self.board.is_path_clear(0, 0, 2, 1, "invalid"))

class TestBoardDisplay(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_display_board(self):
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

class TestBoardMovement(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_move_piece_capture(self):
        self.board.__matrix__[3][3] = Pawn("BLACK")
        self.board.move_piece(6, 3, 3, 3)
        self.assertIsInstance(self.board.__matrix__[3][3], Pawn)
        self.assertEqual(self.board.__matrix__[3][3].__color__, "WHITE")

    def test_move_piece_same_color(self):
        with patch('builtins.print') as mock_print:
            self.board.move_piece(7, 0, 7, 1)
        mock_print.assert_called_with("No se puede capturar una pieza del mismo color.")

    def test_move_piece_pawn___first_move__(self):
        pawn = self.board.__matrix__[6][0]
        self.board.move_piece(6, 0, 4, 0)
        self.assertFalse(pawn.__first_move__)

class TestBoardCaptures(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_get_capture_counts(self):
        self.board.__white_captures__ = 2
        self.board.__black_captures__ = 3
        capture_counts = self.board.get_capture_counts()
        self.assertEqual(capture_counts["__white_captures__"], 2)
        self.assertEqual(capture_counts["__black_captures__"], 3)

    def test_get_capture_counts(self):
        self.board.__white_captures__ = 2
        self.board.__black_captures__ = 3
        capture_counts = self.board.get_capture_counts()
        self.assertEqual(capture_counts["__white_captures__"], 2)
        self.assertEqual(capture_counts["__black_captures__"], 3)

    def test_print_capture_counts(self):
        self.board.__white_captures__ = 2
        self.board.__black_captures__ = 3

    
class TestBoardAdditional(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_is_valid_move(self):
        # Prueba para movimiento fuera del tablero
        self.assertFalse(self.board.is_valid_move(8, 0, 9, 0))
        
        # Prueba para mover una pieza que no existe
        self.assertFalse(self.board.is_valid_move(3, 3, 4, 4))
        
        # Prueba para un movimiento válido de un peón
        self.assertTrue(self.board.is_valid_move(6, 0, 5, 0))
        
        # Prueba para un movimiento válido de un caballo
        self.assertTrue(self.board.is_valid_move(7, 1, 5, 2))
        
        # Prueba para un movimiento inválido (camino bloqueado)
        self.assertFalse(self.board.is_valid_move(7, 0, 5, 0))

    def test_move_piece(self):
        # Mover un peón
        self.board.move_piece(6, 0, 4, 0)
        self.assertIsInstance(self.board.__matrix__[4][0], Pawn)
        self.assertIsNone(self.board.__matrix__[6][0])

        # Intentar mover a una posición ocupada por una pieza del mismo color
        with patch('builtins.print') as mock_print:
            self.board.move_piece(7, 0, 7, 1)
            mock_print.assert_called_with("No se puede capturar una pieza del mismo color.")

        # Capturar una pieza
        self.board.__matrix__[3][0] = Pawn("BLACK")
        self.board.move_piece(4, 0, 3, 0)
        self.assertIsInstance(self.board.__matrix__[3][0], Pawn)
        self.assertEqual(self.board.__matrix__[3][0].__color__, "WHITE")
        

    def test_is_path_clear(self):
        # Camino horizontal bloqueado
        self.board.__matrix__[0][2] = None  # Eliminar el alfil negro
        self.assertFalse(self.board.is_path_clear(0, 0, 0, 3, "horizontal"))

        
        # Camino diagonal bloqueado
        self.board.__matrix__[5][1] = Pawn("WHITE")
        self.assertFalse(self.board.is_path_clear(6, 0, 4, 2, "diagonal"))
        
        # Camino diagonal libre
        self.board.__matrix__[5][1] = None
        self.assertTrue(self.board.is_path_clear(6, 0, 4, 2, "diagonal"))

    def test_get_movement_type(self):
        self.assertEqual(self.board.get_movement_type(0, 0, 0, 3), "horizontal")
        self.assertEqual(self.board.get_movement_type(0, 0, 3, 0), "vertical")
        self.assertEqual(self.board.get_movement_type(0, 0, 3, 3), "diagonal")
        self.assertEqual(self.board.get_movement_type(0, 0, 1, 2), "invalid")
    
class TestBoardAdditionalCoverage(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_king_capture(self):
        # Colocar un rey negro en una posición vulnerable
        self.board.__matrix__[4][4] = King("BLACK")
        
        # Mover una pieza blanca para capturar al rey
        self.board.__matrix__[5][5] = Pawn("WHITE")
        self.board.move_piece(5, 5, 4, 4)
        
        self.assertTrue(self.board.__king_captured__)


    def test_get_capture_counts(self):
        self.board.__white_captures__ = 2
        self.board.__black_captures__ = 3
        
        capture_counts = self.board.get_capture_counts()
        
        self.assertEqual(capture_counts['__white_captures__'], 2)
        self.assertEqual(capture_counts['__black_captures__'], 3)

    def test_update_capture_count(self):
        initial_white_captures = self.board.__white_captures__
        initial_black_captures = self.board.__black_captures__
        
        self.board.update_capture_count("WHITE")
        self.assertEqual(self.board.__black_captures__, initial_black_captures + 1)
        
        self.board.update_capture_count("BLACK")
        self.assertEqual(self.board.__white_captures__, initial_white_captures + 1)

    def test_get_capture_counts(self):
        self.board.__white_captures__ = 2
        self.board.__black_captures__ = 3
        
        capture_counts = self.board.get_capture_counts()
        
        self.assertEqual(capture_counts['__white_captures__'], 2)
        self.assertEqual(capture_counts['__black_captures__'], 3)

    def test_is_path_clear_for_non_knight(self):
        # Limpiar el camino para la prueba
        self.board.__matrix__[6][3] = None
        self.board.__matrix__[5][4] = None
        
        # Probar con un movimiento diagonal
        bishop = Bishop("WHITE")
        self.assertTrue(self.board.is_path_clear_for_non_knight(bishop, 7, 2, 5, 4))
        
        # Bloquear el camino y probar de nuevo
        self.board.__matrix__[6][3] = Pawn("WHITE")
        self.assertFalse(self.board.is_path_clear_for_non_knight(bishop, 7, 2, 5, 4))

    def test_are_positions_valid(self):
        # Posiciones válidas
        self.assertTrue(self.board.are_positions_valid(0, 0, 1, 0))
        
        # Posición fuera del tablero
        self.assertFalse(self.board.are_positions_valid(0, 0, 8, 0))
        
        # Posición inicial sin pieza
        self.board.__matrix__[4][4] = None
        self.assertFalse(self.board.are_positions_valid(4, 4, 5, 5))

    def test_is_piece_movement_valid(self):
        # Movimiento válido de un peón
        pawn = self.board.__matrix__[6][0]
        self.assertTrue(self.board.is_piece_movement_valid(pawn, 6, 0, 5, 0))
        
        # Movimiento inválido de un peón
        self.assertFalse(self.board.is_piece_movement_valid(pawn, 6, 0, 4, 1))

    def test_get_movement_type(self):
        self.assertEqual(self.board.get_movement_type(0, 0, 0, 3), "horizontal")
        self.assertEqual(self.board.get_movement_type(0, 0, 3, 0), "vertical")
        self.assertEqual(self.board.get_movement_type(0, 0, 3, 3), "diagonal")
        self.assertEqual(self.board.get_movement_type(0, 0, 1, 2), "invalid")
    
    def test_is_valid_move_out_of_board(self):
        # Prueba para movimiento fuera del tablero (líneas 75-76)
        self.assertFalse(self.board.is_valid_move(8, 0, 9, 0))

    def test_is_valid_move_knight(self):
        # Prueba para movimiento válido de un caballo (línea 91)
        self.assertTrue(self.board.is_valid_move(7, 1, 5, 2))

    def test_is_valid_move_blocked_path(self):
        # Prueba para movimiento bloqueado (líneas 92-93)
        self.assertFalse(self.board.is_valid_move(7, 0, 5, 0))

    def test_move_piece_invalid(self):
        # Prueba para movimiento inválido (líneas 115-116)
        result = self.board.move_piece(7, 0, 7, 1)
        self.assertEqual(result, "INVALID")

    # def test_handle_pawn_promotion_invalid_choice(self):
    #     # Colocar un peón blanco en la última fila
    #     self.board.__matrix__[0][0] = Pawn("WHITE")
        
    #     # Simular una elección inválida y luego una válida
    #     with patch('builtins.input', side_effect=['5', '1']):
    #         with patch('sys.stdout', new=StringIO()) as fake_output:
    #             self.board.handle_pawn_promotion(0, 0)
    #             output = fake_output.getvalue()

    #     self.assertIn("Elección no válida", output)
    #     self.assertIsInstance(self.board.__matrix__[0][0], Queen)

    def test_king_capture(self):
        # Colocar un rey negro en una posición vulnerable
        self.board.__matrix__[4][4] = King("BLACK")
        
        # Mover una pieza blanca para capturar al rey
        self.board.__matrix__[5][5] = Pawn("WHITE")
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.board.move_piece(5, 5, 4, 4)
            output = fake_output.getvalue()
        
        self.assertIn("¡El rey BLACK ha sido capturado! Fin del juego.", output)
        self.assertTrue(self.board.__king_captured__)

    def test_is_valid_move_knight(self):
        # Prueba para movimiento válido de un caballo (línea 91)
        self.assertTrue(self.board.is_valid_move(7, 1, 5, 2))

    def test_is_valid_move_blocked_path(self):
        # Prueba para movimiento bloqueado (líneas 92-93)
        self.assertFalse(self.board.is_valid_move(7, 0, 5, 0))

    def test_move_piece_invalid(self):
        # Prueba para movimiento inválido (líneas 115-116)
        result = self.board.move_piece(7, 0, 7, 1)
        self.assertEqual(result, "INVALID")

    def test_king_capture(self):
        # Colocar un rey negro en una posición vulnerable (líneas 159-160)
        self.board.__matrix__[4][4] = King("BLACK")
        self.board.__matrix__[5][5] = Pawn("WHITE")
        
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.board.move_piece(5, 5, 4, 4)
            output = fake_output.getvalue()
        
        self.assertIn("¡El rey BLACK ha sido capturado! Fin del juego.", output)
        self.assertTrue(self.board.__king_captured__)

    def test_handle_pawn_promotion_all_choices(self):
        # Prueba para todas las opciones de promoción de peón (líneas 180, 182, 184)
        test_cases = [
            ("1", Queen), ("2", Rook), ("3", Bishop), ("4", Knight), ("5", Queen)
        ]
        
        for choice, expected_piece in test_cases:
            with self.subTest(choice=choice):
                self.board.__matrix__[0][0] = Pawn("WHITE")
                with patch('builtins.input', return_value=choice):
                    self.board.handle_pawn_promotion(0, 0)
                self.assertIsInstance(self.board.__matrix__[0][0], expected_piece)


if __name__ == '__main__':
    unittest.main()