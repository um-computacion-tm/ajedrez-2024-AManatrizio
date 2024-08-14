# Rook (Torre)
# Movimiento: La torre se mueve en línea recta horizontal o 
# verticalmente, tantas casillas como quiera.

from .piece import Piece

class Rook(Piece):
    def move(self):
        # Lógica para mover la torre
        return