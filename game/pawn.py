# Pawn(Peón)
# Movimiento: Los peones se mueven una casilla hacia adelante,
# pero capturan en diagonal. En su primer movimiento, un peón 
# puede avanzar dos casillas.

from .piece import Piece

class Pawn(Piece):
    def move(self):
        # Lógica para mover el peón
        return