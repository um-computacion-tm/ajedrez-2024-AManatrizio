from .board import Board
class Chess:
    def __init__(self):
        self.board = Board() # Creo objeto board
        self.current_player = "WHITE" # Inicializo el primer jugador en blanco
        self.mutual_agreement_to_end = False 

    
    def get_captures(self):
        return self.board.get_capture_counts()


    def is_over(self):
        # Un jugador se queda sin piezas (15 capturas, excluyendo el rey)
        if self.board.white_captures == 15 or self.board.black_captures == 15:
            return True
        
        # El rey ha sido capturado
        if self.board.king_captured:
            return True
        
        # Los jugadores deciden terminar la partida de mutuo acuerdo
        if self.mutual_agreement_to_end:
            return True
        
        return False

    # Cambia el estado de mutual_agreement_to_end
    def end_game_by_agreement(self):
        self.mutual_agreement_to_end = True


    def display_board(self):
        self.board.display_board()



    def play_move(self, piece, move):
        #print(f"Intentando mover pieza {piece} a {move}")
        p_fila, p_columna = self.parse_move(piece)
        m_fila, m_columna = self.parse_move(move)
        
        # Verificar si es el turno del jugador correcto
        piece_color = self.board.get_color(p_fila, p_columna)
        if piece_color != self.current_player:
            #print(f"No es el turno de las piezas {piece_color}")
            return False

        # Verificar si el destino tiene una pieza del oponente para capturar
        if self.board.has_piece(m_fila, m_columna):
            target_color = self.board.get_color(m_fila, m_columna)
            if target_color != self.current_player:
                #print(f"Capturando pieza de {target_color}")
                self.board.update_capture_count(target_color)  # Aumentar el conteo de capturas
            else:
                #print("No puedes capturar tu propia pieza")
                return False

        # Verificar si el movimiento es válido
        if self.board.is_valid_move(p_fila, p_columna, m_fila, m_columna):
            #print("Movimiento válido")
            self.board.move_piece(p_fila, p_columna, m_fila, m_columna)
            #print(f"Posiciones convertidas: inicial ({p_fila}, {p_columna}), final ({m_fila}, {m_columna})")
            self.switch_turn()
            #print(f"Turno de: {self.current_player}")
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
        self.current_player = "BLACK" if self.current_player == "WHITE" else "WHITE"
