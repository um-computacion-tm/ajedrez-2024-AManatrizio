from .board import Board
class Chess:
    def __init__(self):
        self.__board__ = Board() # Creo objeto __board__
        self.__current_player__ = "WHITE" # Inicializo el primer jugador en blanco
        self.__mutual_agreement_to_end__ = False 

    
    def get_captures(self):
        return self.__board__.get_capture_counts()


    def is_over(self):
        # Un jugador se queda sin piezas (15 capturas, excluyendo el rey)
        if self.__board__.__white_captures__ == 15 or self.__board__.__black_captures__ == 15:
            return True
        
        # El rey ha sido capturado
        if self.__board__.__king_captured__:
            return True
        
        # Los jugadores deciden terminar la partida de mutuo acuerdo
        if self.__mutual_agreement_to_end__:
            return True
        
        return False

    # Cambia el estado de __mutual_agreement_to_end__
    def end_game_by_agreement(self):
        self.__mutual_agreement_to_end__ = True
    
    def display_board(self):
        self.__board__.display_board()
    
    def play_move(self, piece, move):
        p_row, p_col = self.parse_move(piece)
        m_row, m_col = self.parse_move(move)
        piece_color = self.__board__.get_color(p_row, p_col)
        
        if piece_color != self.__current_player__:
            return "INVALID_TURN"
        
        if not self.__board__.is_valid_move(p_row, p_col, m_row, m_col):
            return "INVALID"
        
        move_result = self.__board__.move_piece(p_row, p_col, m_row, m_col)
        
        if isinstance(move_result, tuple):
            result, info = move_result
        else:
            result, info = move_result, None
        
        if result == "NORMAL":
            result = "VALID"
            self.switch_turn()
        elif result in ["PROMOTION_NEEDED", "KING_CAPTURED"]:
            return result, info
        elif result not in ["INVALID", "INVALID_CAPTURE"]:
            self.switch_turn()
        
        return (result, info) if info is not None else result
    
    def promote_pawn(self, row, col, choice):
        promoted_piece = self.__board__.handle_pawn_promotion(row, col, choice)
        self.switch_turn()
        return promoted_piece
    
    def parse_move(self, move):
        if len(move) != 2:
            raise ValueError("Invalid input. Please enter two digits together (e.g., '62' for row 6, column 2).")
        
        try:
            row, col = map(int, move)
            if 0 <= row <= 7 and 0 <= col <= 7:
                return row, col
            raise ValueError("Coordinates must be between 0 and 7.")
        except ValueError:
            raise ValueError("Please enter only numbers for coordinates.")
    
    # cambio de turno
    def switch_turn(self):
        self.__current_player__ = "BLACK" if self.__current_player__ == "WHITE" else "WHITE"