# Bishop (Alfil)
# Movimiento: El alfil se mueve diagonalmente, tantas casillas como desee.

from .piece import Piece

class Bishop(Piece):
    def move(self):
        # Lógica para mover el alfil
        return