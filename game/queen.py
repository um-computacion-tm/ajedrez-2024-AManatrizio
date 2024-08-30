# Queen (Reina)
# Movimiento: La reina se mueve en línea recta tanto horizontal,
# vertical, como diagonalmente, tantas casillas como desee.


from .piece import Piece

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
    
    def __str__(self):
        return "♕" if self.color == "WHITE" else "♛"



    def move(self):
        # Lógica para mover la reina
        return