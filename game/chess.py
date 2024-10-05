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
        p_fila, p_columna = self.parse_move(piece)
        m_fila, m_columna = self.parse_move(move)
        
        piece_color = self.__board__.get_color(p_fila, p_columna)
        if piece_color != self.__current_player__:
            return "INVALID_TURN"

        if self.__board__.is_valid_move(p_fila, p_columna, m_fila, m_columna):
            result = self.__board__.move_piece(p_fila, p_columna, m_fila, m_columna)
            if isinstance(result, tuple):
                result, info = result
            else:
                info = None
            
            if result == "NORMAL":
                self.switch_turn()
                return "VALID"
            elif result == "KING_CAPTURED":
                return "KING_CAPTURED", info
            elif result == "PROMOTION_NEEDED":
                return "PROMOTION_NEEDED", info
            elif result == "INVALID_CAPTURE":
                return "INVALID_CAPTURE"
            else:
                return "INVALID"
        else:
            return "INVALID"

    def promote_pawn(self, fila, columna, choice):
        promoted_piece = self.__board__.handle_pawn_promotion(fila, columna, choice)
        self.switch_turn()
        return promoted_piece



    def parse_move(self, move):
        # Checkeo de que las posiciones son validas
        # Convertir el movimiento en coordenadas
        fila = int(move[0])
        columna = int(move[1])
        return fila, columna


    # Cambio de turno
    def switch_turn(self):
        self.__current_player__ = "BLACK" if self.__current_player__ == "WHITE" else "WHITE"
