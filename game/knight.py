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
    

    def is_valid_movement(self, initial_row, initial_col, final_row, final_col):
        row_difference = abs(final_row - initial_row)
        col_difference = abs(final_col - initial_col)
        
        # Check for valid Knight movement (L-shape)
        if (row_difference == 2 and col_difference == 1) or (row_difference == 1 and col_difference == 2):
            return True
        return False