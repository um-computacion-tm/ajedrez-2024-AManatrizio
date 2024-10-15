from .piece import Piece

class Pawn(Piece):
    def __init__(self, __color__):
        super().__init__(__color__)
        self.__first_move__ = True

    def __str__(self):
        return "♙" if self.__color__ == "WHITE" else "♟"

    def is_valid_movement(self, initial_row, initial_col, final_row, final_col, is_capture=False):
        direction = 1 if self.__color__.lower() == "black" else -1
        row_diff = final_row - initial_row
        col_diff = abs(final_col - initial_col)

        valid_move = False

        if not is_capture:
            # Movimiento hacia adelante (sin captura)
            if col_diff == 0:
                if self.__first_move__:
                    valid_move = row_diff == direction or row_diff == 2 * direction
                else:
                    valid_move = row_diff == direction
        else:
            # Captura en diagonal
            valid_move = col_diff == 1 and row_diff == direction

        return valid_move

    def complete_move(self):
        if self.__first_move__:
            self.__first_move__ = False