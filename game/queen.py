# Queen (Reina)
# Movimiento: La reina se mueve en línea recta tanto horizontal,
# vertical, como diagonalmente, tantas casillas como desee.


from .piece import Piece

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
    
    def __str__(self):
        return "♕" if self.color == "WHITE" else "♛"



    def is_valid_movement(self, initial_row, initial_col, final_row, final_col):
        # Calcular la diferencia absoluta en filas y columnas
        row_diff = abs(final_row - initial_row)
        col_diff = abs(final_col - initial_col)
        
        #print(f"Debug: Queen movement from ({initial_row}, {initial_col}) to ({final_row}, {final_col})")
        #print(f"Debug: row_diff = {row_diff}, col_diff = {col_diff}")
        
        # La reina se puede mover cualquier número de casillas en línea recta o diagonal
        # Movimiento horizontal, vertical o diagonal
        if row_diff == col_diff or initial_row == final_row or initial_col == final_col:
            #print("Debug: Valid queen movement")
            return True
        else:
            #print("Debug: Invalid queen movement")
            return False