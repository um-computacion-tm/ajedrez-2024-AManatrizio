# Knight (Caballo)
# Movimiento: El caballo se mueve en forma de “L”: dos casillas en 
# una dirección (horizontal o vertical) y luego una casilla 
# perpendicularmente, o una casilla en una dirección y luego 
# dos casillas perpendicularmente.

from .piece import Piece

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
    
    def __str__(self):
        return "♘" if self.color == "WHITE" else "♞"
    

    def is_valid_movement(self, initial_row, final_row, initial_col, final_col):
        # Calcula la diferencia entre las posiciones inicial y final
        row_difference = abs(final_row - initial_row)
        col_difference = abs(final_col - initial_col)
        
        # Verifica si el movimiento es válido para un caballo
        if (row_difference == 2 and col_difference == 1) or (row_difference == 1 and col_difference == 2):
            return True
        else:
            return False