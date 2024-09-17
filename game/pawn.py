# Pawn(Peón)
# Movimiento: Los peones se mueven una casilla hacia adelante,
# pero capturan en diagonal. En su primer movimiento, un peón 
# puede avanzar dos casillas.

from .piece import Piece

class Pawn(Piece):

    def __init__(self, color):
        super().__init__(color) # Hereda de la clase padre Piece
        self.first_move = True  # Indica si es el primer movimiento, lo inicializa asi

    def __str__(self):
       return "♙" if self.color == "WHITE" else "♟"
    
    def is_valid_movement(self, initial_row, final_row, initial_col, final_col):
        return True

    # # Significa que es un movimento en la misma columna
    # def is_same_column(self, initial_col, final_col):
    #     if initial_col == final_col:
    #         return True
        
    # # Determina si el movimiento es para arriba o para abajo dependiendo el color.
    # def is_moving_forward(self, initial_row, final_row, color):
    #     if color == "WHITE":
    #         return final_row < initial_row  # Blanco se mueve hacia arriba en el tablero
    #     else:
    #         return final_row > initial_row  # Negro se mueve hacia abajo en el tablero