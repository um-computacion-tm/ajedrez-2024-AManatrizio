# Bishop (Alfil)
# Movimiento: El alfil se mueve diagonalmente, tantas casillas como desee.

from .piece import Piece

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
    
    def __str__(self):
        return "♗" if self.color == "WHITE" else "♝"
    

    def diagonal_movement(self, initial_row, final_row, initial_col, final_col):
        # Verifica si el movimiento es diagonal comparando las diferencias absolutas entre filas y columnas
        if abs(final_row - initial_row) == abs(final_col - initial_col):
            return "diagonal"
        else:
            return "invalid"

    def is_valid_movement(self, movement):
        # Solo los movimientos diagonales son válidos para el alfil
        if movement == "diagonal":
            return True
        else:
            return False