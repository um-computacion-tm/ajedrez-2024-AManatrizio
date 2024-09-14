# Rook (Torre)
# Movimiento: La torre se mueve en línea recta horizontal o 
# verticalmente, tantas casillas como quiera.

from .piece import Piece

class Rook(Piece):

    def __init__(self, color):
        super().__init__(color)
    
    def __str__(self):
        return "♖" if self.color == "WHITE" else "♜"

    

# initial_row -> fila inicial donde comienza la pieza 
# final_row -> fila a la que se quiere mover la pieza
# filas iguales -> horizontal
# columnas iguales -> vertical

    # Determina si el movimiento es horizontal o vertical
    def horizontal_or_vertical_movement(self, initial_row, final_row, initial_col, final_col):
        if initial_row == final_row and initial_col != final_col:
            return "horizontal"
        elif initial_row != final_row and initial_col == final_col:
            return "vertical"
        else:
            return "invalid"

    def is_valid_movement(self, initial_row, initial_col, final_row, final_col):
        # Determinar el tipo de movimiento
        movement_type = self.horizontal_or_vertical_movement(initial_row, final_row, initial_col, final_col)
        
        if movement_type == "invalid":
            return False

        # La verificación del camino despejado se hará en el Board
        return True