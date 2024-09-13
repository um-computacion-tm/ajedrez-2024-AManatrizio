# Queen (Reina)
# Movimiento: La reina se mueve en línea recta tanto horizontal,
# vertical, como diagonalmente, tantas casillas como desee.


from .piece import Piece

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
    
    def __str__(self):
        return "♕" if self.color == "WHITE" else "♛"



    def is_valid_movement(self, initial_row, final_row, initial_col, final_col):
        # Calcular la diferencia absoluta en filas y columnas
        row_diff = abs(final_row - initial_row)
        col_diff = abs(final_col - initial_col)
        
        # La reina se puede mover cualquier número de casillas en línea recta o diagonal
        # Movimiento horizontal o vertical: uno de los dos (row_diff o col_diff) debe ser 0
        # Movimiento diagonal: row_diff debe ser igual a col_diff
        if (row_diff == col_diff or row_diff == 0 or col_diff == 0) and (row_diff != 0 or col_diff != 0):
            return True