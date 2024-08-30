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

    def horizontal_or_vertical_movement(initial_row, final_row, initial_col, final_col):
        if initial_row == final_row and initial_col != final_col:
            return "horizontal"
        elif initial_col == final_col and initial_row != final_row:
            return "vertical"
        else:
            return "invalid"
    

#_______!!!!!! agregar una comprobacion de si hay alguna pieza en el path y en la posicion a la que quiere llegar.

# Verifica si el movimiento es válido (horizontal o vertical) en base a lo que devuelve
# la función que determina el tipo de movimiento.
def is_valid_movement(movement):
    if movement == "horizontal" or movement == "vertical":
        return True
    else:
        return False
    


