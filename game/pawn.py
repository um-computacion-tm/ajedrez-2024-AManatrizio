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
    


    def is_valid_movement(self, initial_row, initial_col, final_row, final_col):
        # print(f"Debugging is_valid_movement:")
        # print(f"Color: {self.color}")
        # print(f"Initial position: ({initial_row}, {initial_col})")
        # print(f"Final position: ({final_row}, {final_col})")

        # Determinar la dirección del movimiento según el color
        direction = 1 if self.color.lower() == "black" else -1
        #print(f"Direction: {direction}")
        
        # Calcular la diferencia en filas y columnas
        row_diff = final_row - initial_row
        col_diff = abs(final_col - initial_col)
        #print(f"Row difference: {row_diff}")
        #print(f"Column difference: {col_diff}")

        # Movimiento hacia adelante
        if col_diff == 0:
            if self.first_move:
                # Primer movimiento: puede avanzar una o dos casillas
                valid = row_diff == direction or row_diff == 2 * direction
                #print(f"First move, forward movement valid: {valid}")
                return valid
            else:
                # Después del primer movimiento: solo puede avanzar una casilla
                valid = row_diff == direction
                #print(f"Not first move, forward movement valid: {valid}")
                return valid
        
        # Movimiento diagonal (potencial captura)
        elif col_diff == 1 and row_diff == direction:
            #print("Diagonal movement (capture) is valid")
            return True
        
        #print("Movement is not valid")
        return False
    
    # Cambia el estado de que ya no es el primer movimiento del peon
    def complete_move(self):
        if self.first_move:
            self.first_move = False