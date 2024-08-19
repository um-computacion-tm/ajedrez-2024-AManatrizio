# Pawn(Peón)
# Movimiento: Los peones se mueven una casilla hacia adelante,
# pero capturan en diagonal. En su primer movimiento, un peón 
# puede avanzar dos casillas.

from .piece import Piece

class Pawn(Piece):

    def __init__(self, color, position):
        super().__init__(color, position) # Hereda de la clase padre Piece
        self.first_move = True  # Indica si es el primer movimiento, lo inicializa asi 

     #ovimientos
    def is_valid_movement(self, initial_row, final_row, initial_col, final_col):
        # Movimientos verticales
        # Si estas son iguales significa que se mantiene en la misma columna es decir el movimiento es correcto.
        if initial_col == final_col:
            # Primer movimiento del peón (dos casillas hacia adelante)
            # TRUE                   Ejemplo: 3 - 1 = 2
            if self.first_move and abs(final_row - initial_row) == 2:
                self.first_move = False  # Después del primer movimiento, se desactiva
                return True
            # Movimientos normales del peón (una casilla hacia adelante)
            elif abs(final_row - initial_row) == 1:
                return True
        

        # Capturas
        # Movimiento de captura en diagonal
        elif abs(initial_col - final_col) == 1 and abs(final_row - initial_row) == 1:
            return True
        
        return False
    


