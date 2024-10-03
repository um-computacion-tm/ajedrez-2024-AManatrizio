from .king import King
from .knight import Knight
from .queen import Queen
from .bishop import Bishop
from .rook import Rook
from .pawn import Pawn
from .piece import Piece
from .exceptions import OutOfBoardError

class Board:

    def __init__(self):
        # Crear un tablero vacío de 8x8 y agrega las piezas en su posicion.
        self.__matrix__ = [[None for _ in range(8)] for _ in range(8)]
        self.__white_captures__ = 0  # Contador de piezas blancas capturadas
        self.__black_captures__ = 0  # Contador de piezas negras capturadas
        self.__king_captured__ = False  # Indicador si el rey ha sido capturado

        # negras
        self.__matrix__[0][0] = Rook(__color__= "BLACK") # Torre
        self.__matrix__[0][7] = Rook(__color__= "BLACK") # Torre
        self.__matrix__[0][1] = Knight(__color__= "BLACK") # Caballo
        self.__matrix__[0][6] = Knight(__color__= "BLACK") # Caballo
        self.__matrix__[0][2] = Bishop(__color__= "BLACK") # Alfil
        self.__matrix__[0][5] = Bishop(__color__= "BLACK") # Alfil
        self.__matrix__[0][3] = Queen(__color__= "BLACK") # Reina
        self.__matrix__[0][4] = King(__color__= "BLACK") # Rey
        for i in range(8):
            self.__matrix__[1][i] = Pawn(__color__= "BLACK") # Peon

        # blancas
        self.__matrix__[7][7] = Rook(__color__= "WHITE") # Torre
        self.__matrix__[7][0] = Rook(__color__= "WHITE") # Torre
        self.__matrix__[7][1] = Knight(__color__= "WHITE") # Caballo
        self.__matrix__[7][6] = Knight(__color__= "WHITE") # Caballo
        self.__matrix__[7][2] = Bishop(__color__= "WHITE") # Alfil
        self.__matrix__[7][5] = Bishop(__color__= "WHITE") # Alfil
        self.__matrix__[7][3] = Queen(__color__= "WHITE") # Reina
        self.__matrix__[7][4] = King(__color__= "WHITE") # Rey
        for i in range(8):
            self.__matrix__[6][i] = Pawn(__color__= "WHITE") # Peon
    
   # Revisa si la posicion ingresada no sale fuera de los limites del tablero
    def is_out_of_board(self, row, col):
        if 0 <= row < 8 and 0 <= col < 8:
            return False  # Está dentro de los límites del tablero
        else:
            raise OutOfBoardError(f"La posición ({row}, {col}) está fuera del tablero")

    # Revisa si hay una pieza en la posicion a la que se quiere ir
    def has_piece(self, row, col):
        if self.__matrix__[row][col] is not None:
            return True
        return False


    def get_color(self, row, col):
        piece = self.__matrix__[row][col]
        if piece is None:
            return None
        else:
            return piece.__color__
    

    # Verifica si un movimiento es válido en el tablero de ajedrez.
    # Combina todas las reglas de movimiento en una sola función.
    def is_valid_move(self, p_fila, p_columna, m_fila, m_columna):
        is_valid = False
        try:
            if self.are_positions_valid(p_fila, p_columna, m_fila, m_columna):
                pieza = self.__matrix__[p_fila][p_columna]
                if self.is_piece_movement_valid(pieza, p_fila, p_columna, m_fila, m_columna):
                    if isinstance(pieza, Knight) or self.is_path_clear_for_non_knight(pieza, p_fila, p_columna, m_fila, m_columna):
                        is_valid = self.is_destination_valid(pieza, m_fila, m_columna)
        except OutOfBoardError:
            is_valid = False
        
        return is_valid


    # Verifica si el camino está libre para piezas que no son caballos.
    # Los caballos pueden saltar sobre otras piezas, por eso se tratan diferente.
    def is_path_clear_for_non_knight(self, pieza, p_fila, p_columna, m_fila, m_columna):
        movement_type = self.get_movement_type(p_fila, p_columna, m_fila, m_columna)
        return self.is_path_clear(p_fila, p_columna, m_fila, m_columna, movement_type)


    # Comprueba si el destino del movimiento es válido.
    # Permite mover a un espacio vacío o capturar una pieza del oponente.
    def is_destination_valid(self, pieza, m_fila, m_columna):
        if not self.has_piece(m_fila, m_columna):
            return True
        return self.get___color__(m_fila, m_columna) != pieza.__color__ 

    def are_positions_valid(self, p_fila, p_columna, m_fila, m_columna):
        try:
            self.is_out_of_board(p_fila, p_columna)
            self.is_out_of_board(m_fila, m_columna)
        except OutOfBoardError:
            return False
        
        if not self.has_piece(p_fila, p_columna):
            #print(f"No hay una pieza en {p_fila} {p_columna}")
            return False
        return True

    def is_piece_movement_valid(self, pieza, p_fila, p_columna, m_fila, m_columna):
        if not pieza.is_valid_movement(p_fila, p_columna, m_fila, m_columna):
            #print("Movimiento no válido para esta pieza")
            return False
        return True

    def is_destination_valid(self, pieza, m_fila, m_columna):
        if self.has_piece(m_fila, m_columna):
            if self.get___color__(m_fila, m_columna) == pieza.__color__:
                return False
        return True

    def get_movement_type(self, p_fila, p_columna, m_fila, m_columna):
        if p_fila == m_fila:
            return "horizontal"
        elif p_columna == m_columna:
            return "vertical"
        elif abs(m_fila - p_fila) == abs(m_columna - p_columna):
            return "diagonal"
        else:
            return "invalid"
    

    def move_piece(self, p_fila, p_columna, m_fila, m_columna):
        pieza = self.__matrix__[p_fila][p_columna]
        
        # Verificar si hay una pieza en la casilla de destino
        if self.has_piece(m_fila, m_columna):
            # Obtener la pieza en la casilla de destino
            pieza_capturada = self.__matrix__[m_fila][m_columna]
            __color___destino = pieza_capturada.__color__
            
            # Verificar si es una pieza del __color__ opuesto
            if __color___destino != pieza.__color__:
                #print(f"Captura realizada en ({m_fila}, {m_columna})")

                if isinstance(pieza_capturada, King):
                    self.__king_captured__ = True
                    print(f"¡El rey {__color___destino} ha sido capturado! Fin del juego.")
                
                # Actualizar el contador de capturas
                self.update_capture_count(__color___destino)
                
                # Eliminar la pieza capturada
                self.__matrix__[m_fila][m_columna] = None
                
            else:
                print("No se puede capturar una pieza del mismo color.")
                return
    
        # Mover la pieza
        #print(f"Moviendo pieza: {pieza} de ({p_fila}, {p_columna}) a ({m_fila}, {m_columna})")
        self.__matrix__[p_fila][p_columna] = None
        self.__matrix__[m_fila][m_columna] = pieza

        if isinstance(pieza, Pawn):
            pieza.complete_move()

            # Verificar si el peón ha llegado al final del tablero
            if (pieza.__color__ == "WHITE" and m_fila == 0) or (pieza.__color__ == "BLACK" and m_fila == 7):
                return "PROMOTE"  # Indicar que se necesita una promoción
    
        return "NORMAL"  # Movimiento normal sin promoción
    

    def update_capture_count(self, __color___destino):
        """
        Actualiza el contador de capturas basado en el __color__ de la pieza capturada.
        """
        if __color___destino == "WHITE":
            self.__white_captures__ += 1
        else:
            self.__black_captures__ += 1
    


    def get_capture_counts(self):
        return {"__white_captures__": self.__white_captures__, "__black_captures__": self.__black_captures__}
    


    def is_path_clear(self, initial_row, initial_col, final_row, final_col, movement_type):
        #print(f"Checking path from ({initial_row}, {initial_col}) to ({final_row}, {final_col}) - {movement_type}")
        if movement_type == "horizontal":
            return self.is_horizontal_path_clear(initial_row, initial_col, final_col)
        elif movement_type == "vertical":
            return self.is_vertical_path_clear(initial_col, initial_row, final_row)
        elif movement_type == "diagonal":
            return self.is_diagonal_path_clear(initial_row, initial_col, final_row, final_col)
        return False

    def is_horizontal_path_clear(self, row, initial_col, final_col):
        #print(f"Checking horizontal path from ({row}, {initial_col}) to ({row}, {final_col})")
        step = 1 if final_col > initial_col else -1
        for col in range(initial_col + step, final_col, step):
            #print(f"Checking position ({row}, {col})")
            if self.__matrix__[row][col] is not None:
                #print(f"Found piece at ({row}, {col})")
                return False
        #print("Path is clear")
        return True

    def is_vertical_path_clear(self, col, initial_row, final_row):
        #print(f"Checking vertical path from ({initial_row}, {col}) to ({final_row}, {col})")
        step = 1 if final_row > initial_row else -1
        for row in range(initial_row + step, final_row, step):
            #print(f"Checking position ({row}, {col})")
            if self.__matrix__[row][col] is not None:
                #print(f"Found piece at ({row}, {col})")
                return False
        #print("Path is clear")
        return True

    def is_diagonal_path_clear(self, initial_row, initial_col, final_row, final_col):
        #print(f"Checking diagonal path from ({initial_row}, {initial_col}) to ({final_row}, {final_col})")
        row_step = 1 if final_row > initial_row else -1
        col_step = 1 if final_col > initial_col else -1
        row, col = initial_row + row_step, initial_col + col_step
        
        while (row != final_row) and (col != final_col):
            #print(f"Checking position ({row}, {col})")
            if self.__matrix__[row][col] is not None:
                #print(f"Found piece at ({row}, {col})")
                return False
            row += row_step
            col += col_step
        
        #print("Path is clear")
        return True


    def display_board(self):
        # Mostrar el tablero en la consola
        print("    0   1   2   3   4   5   6   7")
        print("  +" + "---+" * 8)

        # Mostrar el tablero con guías de filas (0-7)
        for i, row in enumerate(self.__matrix__, start=0):
            row_display = []
            for piece in row:
                if piece is None:
                    row_display.append(" ")
                else:
                    row_display.append(str(piece))

            # Imprimir la guía de filas al inicio y al final de cada fila
            print(f"{i} | " + " | ".join(row_display) + f" | {i}")
            print("  +" + "---+" * 8)

        # Mostrar los números de columna en la parte inferior del tablero
        print("    0   1   2   3   4   5   6   7")



if __name__ == "__main__":
    board = Board()  # Crear una instancia de la clase Board
    board.display_board()  # Llamar a la función display_board para imprimir el tablero
