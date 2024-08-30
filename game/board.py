from .king import King
from .knight import Knight
from .queen import Queen
from .bishop import Bishop
from .rook import Rook
from .pawn import Pawn
from .piece import Piece
# from exceptions import InvalidMoveError, PieceNotFoundError, OutOfBoardError

class Board:

    def __init__(self):
        # Crear un tablero vacío de 8x8 y agrega las piezas en su posicion.
        self.matrix = [[None for _ in range(8)] for _ in range(8)]

        # Blancas
        self.matrix[0][0] = Rook(color= "WHITE") # Torre
        self.matrix[0][7] = Rook(color= "WHITE") # Torre
        self.matrix[0][1] = Knight(color= "WHITE") # Caballo
        self.matrix[0][6] = Knight(color= "WHITE") # Caballo
        self.matrix[0][2] = Bishop(color= "WHITE") # Alfil
        self.matrix[0][5] = Bishop(color= "WHITE") # Alfil
        self.matrix[0][3] = Queen(color= "WHITE") # Reina
        self.matrix[0][4] = King(color= "WHITE") # Rey
        for i in range(8):
            self.matrix[1][i] = Pawn(color= "WHITE") # Peon

        # Negras
        self.matrix[7][7] = Rook(color= "BLACK") # Torre
        self.matrix[7][0] = Rook(color= "BLACK") # Torre
        self.matrix[7][1] = Knight(color= "BLACK") # Caballo
        self.matrix[7][6] = Knight(color= "BLACK") # Caballo
        self.matrix[7][2] = Bishop(color= "BLACK") # Alfil
        self.matrix[7][5] = Bishop(color= "BLACK") # Alfil
        self.matrix[7][3] = Queen(color= "BLACK") # Reina
        self.matrix[7][4] = King(color= "BLACK") # Rey
        for i in range(8):
            self.matrix[6][i] = Pawn(color= "Black") # Peon
    
   # Revisa si la posicion ingresada no sale fuera de los limites del tablero
    def is_out_of_board(self, row, col):
        if 0 <= row < 7 and 0 <= col < 7:
            return True  # Está dentro de los límites del tablero
        else:
            return False  # Está fuera de los límites del tablero
    

    def has_piece(self, row, col):
        if self.matrix[row][col] is not None:
            return True


    def get_color(self, row, col):
        piece = self.matrix[row][col]
        if piece is None:
            return None
        else:
            return piece.color
        


    # def move_piece(self, start_position, end_position):
    #     # Verificar si las posiciones están dentro de los límites del tablero
    #     if not self.is_within_bounds(start_position) or not self.is_within_bounds(end_position):
    #         raise OutOfBoardError("El movimiento está fuera de los límites del tablero.")

    #     # Obtener la pieza en la posición de inicio
    #     piece = self.get_piece(start_position)
    #     if piece is None:
    #         raise PieceNotFoundError("No hay ninguna pieza en la posición especificada.")

    #     # Validar si el movimiento es válido según la lógica de la pieza
    #     if not piece.is_valid_move(start_position, end_position, self):
    #         raise InvalidMoveError("Movimiento no permitido para esta pieza.")

    #     # Verificar si hay alguna pieza en el camino, si aplica para la pieza)
    #     if not self.is_path_clear(start_position, end_position, piece):
    #         raise InvalidMoveError("El camino está bloqueado por otra pieza.")

    #     # Mover la pieza y actualizar las posiciones en el tablero
    #     self.place_piece(piece, end_position)
    #     self.place_piece(None, start_position)



    def display_board(self):
        # Mostrar el tablero en la consola
        print("    0   1   2   3   4   5   6   7")
        print("  +" + "---+" * 8)

        # Mostrar el tablero con guías de filas (1-8)
        for i, row in enumerate(self.matrix, start=0):
            row_display = []
            for piece in row:
                if piece is None:
                    row_display.append(" ")
                else:
                    row_display.append(str(piece))

            # Imprimir la guía de filas al inicio de cada fila
            print(f"{i} | " + " | ".join(row_display) + " |")
            print("  +" + "---+" * 8)




if __name__ == "__main__":
    board = Board()  # Crear una instancia de la clase Board
    board.display_board()  # Llamar a la función display_board para imprimir el tablero
