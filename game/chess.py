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
        #print(f"Intentando mover pieza {piece} a {move}")
        p_fila, p_columna = self.parse_move(piece)
        m_fila, m_columna = self.parse_move(move)
        
        # Verificar si es el turno del jugador correcto
        piece_color = self.__board__.get_color(p_fila, p_columna)
        if piece_color != self.__current_player__:
            #print(f"No es el turno de las piezas {piece_color}")
            return False

        # Verificar si el destino tiene una pieza del oponente para capturar
        if self.__board__.has_piece(m_fila, m_columna):
            target_color = self.__board__.get_color(m_fila, m_columna)
            if target_color != self.__current_player__:
                #print(f"Capturando pieza de {target_color}")
                pass
            else:
                #print("No puedes capturar tu propia pieza")
                return False

        # Verificar si el movimiento es válido
        if self.__board__.is_valid_move(p_fila, p_columna, m_fila, m_columna):
            #print("Movimiento válido")
            self.__board__.move_piece(p_fila, p_columna, m_fila, m_columna)
            #print(f"Posiciones convertidas: inicial ({p_fila}, {p_columna}), final ({m_fila}, {m_columna})")
            self.switch_turn()
            #print(f"Turno de: {self.__current_player__}")
            return True
        else:
            #print("Movimiento no válido")
            return False



    def parse_move(self, move):
        # Checkeo de que las posiciones son validas
        # Convertir el movimiento en coordenadas
        fila = int(move[0])
        columna = int(move[1])
        return fila, columna


    # Cambio de turno
    def switch_turn(self):
        self.__current_player__ = "BLACK" if self.__current_player__ == "WHITE" else "WHITE"
