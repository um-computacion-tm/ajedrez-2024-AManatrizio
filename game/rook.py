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
# Determina si el movimiento es horizontal, vertical o inválido según las
# posiciones inicial y final. Compara filas iguales para movimiento horizontal y
# columnas iguales para movimiento vertical. Si no es ninguna, el movimiento es inválido.

    # Determina si el movimiento es horizontal o vertical
    @staticmethod
    def horizontal_or_vertical_movement(initial_row, final_row, initial_col, final_col):
        print(f"initial_row: {initial_row}, final_row: {final_row}, initial_col: {initial_col}, final_col: {final_col}")
        if initial_row == final_row and initial_col != final_col:
            return "horizontal"
        elif initial_row != final_row and initial_col == final_col:
            return "vertical"
        else:
            return "invalid"
        
    # Verifica si el movimiento es válido (horizontal o vertical)
    @staticmethod
    def is_valid_movement(movement):
        return movement in {"horizontal", "vertical"}

    