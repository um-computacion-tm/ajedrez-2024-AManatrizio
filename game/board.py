from king import  King
from knight import Knight
from queen import Queen
from bishop import Bishop
from rook import Rook
from pawn import Pawn
class Board:

    def __init__(self):
        # Crear un tablero vacío de 8x8
        self.positions = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.positions.append(col)

    def place_piece(self, piece, row, col):
        # Colocar una pieza en la posición indicada
        self.positions[row][col] = piece

    def setup_board(self):
        # Piezas blancas
        self.place_piece(Rook('white'), 0, 0)  # Torre blanca
        self.place_piece(Rook('white'), 0, 7)  # Torre blanca
        self.place_piece(Knight('white'), 0, 1)  # Caballo blanco
        self.place_piece(Knight('white'), 0, 6)  # Caballo blanco
        self.place_piece(Bishop('white'), 0, 2)  # Alfil blanco
        self.place_piece(Bishop('white'), 0, 5)  # Alfil blanco
        self.place_piece(Queen('white'), 0, 3)  # Reina blanca
        self.place_piece(King('white'), 0, 4)  # Rey blanco
        for i in range(8):
            self.place_piece(Pawn('white'), 1, i)  # Peones blancos

        # Piezas negras
        self.place_piece(Rook('black'), 7, 0)  # Torre negra
        self.place_piece(Rook('black'), 7, 7)  # Torre negra
        self.place_piece(Knight('black'), 7, 1)  # Caballo negro
        self.place_piece(Knight('black'), 7, 6)  # Caballo negro
        self.place_piece(Bishop('black'), 7, 2)  # Alfil negro
        self.place_piece(Bishop('black'), 7, 5)  # Alfil negro
        self.place_piece(Queen('black'), 7, 3)  # Reina negra
        self.place_piece(King('black'), 7, 4)  # Rey negro
        for i in range(8):
            self.place_piece(Pawn('black'), 6, i)  # Peones negros

    # def display_board(self):
    #     # Mostrar el tablero en la consola
    #     for row in self.positions:
    #         row_display = []
    #         for piece in row:
    #             if piece is None:
    #                 row_display.append(".")
    #             else:
    #                 row_display.append(str(piece))
    #         print(" ".join(row_display))
        