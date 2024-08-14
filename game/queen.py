# Queen (Reina)
# Movimiento: La reina se mueve en línea recta tanto horizontal,
# vertical, como diagonalmente, tantas casillas como desee.


from .piece import Piece

class Queen(Piece):
    def move(self):
        # Lógica para mover la reina
        return