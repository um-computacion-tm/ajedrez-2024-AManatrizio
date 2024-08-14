# Knight (Caballo)
# Movimiento: El caballo se mueve en forma de “L”: dos casillas en 
# una dirección (horizontal o vertical) y luego una casilla 
# perpendicularmente, o una casilla en una dirección y luego 
# dos casillas perpendicularmente.

from .piece import Piece

class Knight(Piece):
    def move(self):
        # Lógica para mover el caballo
        return 