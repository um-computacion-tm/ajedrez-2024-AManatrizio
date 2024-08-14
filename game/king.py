# King (Rey):
# Movimiento: El rey se mueve una casilla en cualquier dirección: 
# horizontal, vertical o diagonal.

from .piece import Piece

class King(Piece):
    def move(self):
        # Lógica para mover el rey
        return