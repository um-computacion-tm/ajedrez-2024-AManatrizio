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
            self.matrix[6][i] = Pawn(color= "BLACK") # Peon
    
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
        

    # Verifica si el camino está libre entre dos posiciones dadas, según el tipo de movimiento.
    # 'movement_type' puede ser 'horizontal', 'vertical' o 'diagonal'.
    # Llama a funciones específicas para cada tipo de movimiento y devuelve True si no hay
    # piezas bloqueando el camino; False en caso contrario.
    def is_path_clear(self, initial_row, initial_col, final_row, final_col, movement_type):
        print(f"Checking path from ({initial_row}, {initial_col}) to ({final_row}, {final_col}) - {movement_type}")
        if movement_type == "horizontal":
            return self.is_horizontal_path_clear(initial_row, initial_col, final_col)
        elif movement_type == "vertical":
            return self.is_vertical_path_clear(initial_col, initial_row, final_row)  # Cambiado el orden de los argumentos
        elif movement_type == "diagonal":
            return self.is_diagonal_path_clear(initial_row, initial_col, final_row, final_col)
        return False

    def is_horizontal_path_clear(self, row, initial_col, final_col):
        # Verifica el camino horizontal
        step = 1 if final_col > initial_col else -1
        for col in range(initial_col + step, final_col, step):
            if self.matrix[row][col] is not None:
                return False
        return True

    def is_vertical_path_clear(self, col, initial_row, final_row):
        print(f"Checking vertical path from ({initial_row}, {col}) to ({final_row}, {col})")
        step = 1 if final_row > initial_row else -1
        for row in range(initial_row + step, final_row + step, step):  # Añadido +step al final_row para incluir la última posición
            print(f"Checking position ({row}, {col})")
            if self.matrix[row][col] is not None:
                print(f"Found piece at ({row}, {col})")
                return False
        print("Path is clear")
        return True

    def is_diagonal_path_clear(self, initial_row, initial_col, final_row, final_col):
        print(f"Checking diagonal path from ({initial_row}, {initial_col}) to ({final_row}, {final_col})")
        row_step = 1 if final_row > initial_row else -1
        col_step = 1 if final_col > initial_col else -1
        row, col = initial_row + row_step, initial_col + col_step
        
        while (row != final_row) and (col != final_col):
            print(f"Checking position ({row}, {col})")
            if self.matrix[row][col] is not None:
                print(f"Found piece at ({row}, {col})")
                return False
            row += row_step
            col += col_step
        
        print("Path is clear")
        return True



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
