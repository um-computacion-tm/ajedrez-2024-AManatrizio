# King (Rey):
# Movimiento: El rey se mueve una casilla en cualquier dirección: 
# horizontal, vertical o diagonal.

from .piece import Piece

class King(Piece):

    def __init__(self, color):
        super().__init__(color)
    
    def __str__(self):
        return "♔" if self.color == "WHITE" else "♚"

    def is_valid_movement(self, initial_row, final_row, initial_col, final_col):
        # Calcular la diferencia absoluta en filas y columnas
        row_diff = abs(final_row - initial_row)
        col_diff = abs(final_col - initial_col)
        
        # El rey puede moverse una casilla en cualquier dirección
        # Por lo tanto, la diferencia máxima en filas y columnas debe ser 1
        if row_diff <= 1 and col_diff <= 1 and (row_diff != 0 or col_diff != 0):
            return True
        
            