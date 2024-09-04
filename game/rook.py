# Rook (Torre)
# Movimiento: La torre se mueve en línea recta horizontal o 
# verticalmente, tantas casillas como quiera.

from .piece import Piece
from .board import Board

class Rook(Piece):

    def __init__(self, color):
        super().__init__(color)
    
    def __str__(self):
        return "♖" if self.color == "WHITE" else "♜"

    

# initial_row -> fila inicial donde comienza la pieza 
# final_row -> fila a la que se quiere mover la pieza
# Determina si el movimiento es horizontal, vertical o inválido según las
# posiciones inicial y final. Compara filas iguales para movimiento horizontal y
# columnas iguales para movimiento vertical. Si no es ninguna, el movimiento es inválido.

    # Determina si el movimiento es horizontal o vertical
    @staticmethod
    def horizontal_or_vertical_movement(initial_row, final_row, initial_col, final_col):
        if initial_row == final_row and initial_col != final_col:
            return "horizontal"
        elif initial_col == final_col and initial_row != final_row:
            return "vertical"
        else:
            return "invalid"
         

    # Verifica si el movimiento es válido (horizontal o vertical)
    @staticmethod
    def is_valid_movement(movement):
        return movement in {"horizontal", "vertical"}

    # Verifica si hay alguna pieza en el camino entre la posición inicial y la final
    def is_path_clear(self, initial_row, final_row, initial_col, final_col, board):
        movement_type = self.horizontal_or_vertical_movement(initial_row, final_row, initial_col, final_col)
        if movement_type == "horizontal":
            step = 1 if final_col > initial_col else -1
            for col in range(initial_col + step, final_col, step):
                if board.matrix[initial_row][col] is not None:
                    return False
        elif movement_type == "vertical":
            step = 1 if final_row > initial_row else -1
            for row in range(initial_row + step, final_row, step):
                if board.matrix[row][initial_col] is not None:
                    return False
        return True

    # Verifica si el movimiento es válido para la torre
    def valid_move(self, initial_row, final_row, initial_col, final_col, board):
        # Asegúrate de que el movimiento esté dentro de los límites del tablero
        if not board.is_out_of_board(final_row, final_col):
            return False

        movement_type = self.horizontal_or_vertical_movement(initial_row, final_row, initial_col, final_col)
        if self.is_valid_movement(movement_type) and self.is_path_clear(initial_row, final_row, initial_col, final_col, board):
            # Verifica si el destino está vacío o si hay una pieza enemiga
            destination_piece = board.matrix[final_row][final_col]
            if destination_piece is None or destination_piece.color != self.color:
                return True
        return False
