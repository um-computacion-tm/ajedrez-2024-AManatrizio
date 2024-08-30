# King (Rey):
# Movimiento: El rey se mueve una casilla en cualquier dirección: 
# horizontal, vertical o diagonal.

from .piece import Piece

class King(Piece):

    def __init__(self, color):
        super().__init__(color)
    
    def __str__(self):
        return "♔" if self.color == "WHITE" else "♚"


    def move(self):
        # Lógica para mover el rey
        return