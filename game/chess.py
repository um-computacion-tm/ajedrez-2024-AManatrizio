from .board import Board
class Chess:
    def __init__(self):
        self.board = Board() # Creo objeto board
        self.current_player = "WHITE" # Inicializo el primer jugador en blanco

    def is_over(self):
        # Implementar lógica para determinar si el juego ha terminado
        pass

    def display_board(self):
        self.board.display_board()


    def play_move(self, piece , move):
        print(f"Intentando mover pieza {piece} a {move}")
        p_fila, p_columna = self.parse_move(piece)
        m_fila, m_columna = self.parse_move(move)
        #initial_pos, final_pos = self.parse_move(move)
        if self.board.is_valid_move(p_fila, p_columna, m_fila, m_columna):
            self.board.move_piece(p_fila, p_columna, m_fila, m_columna)
            print(f"Posiciones convertidas: inicial ({p_fila}, {p_columna}), final ({m_fila}, {m_columna})")
            self.switch_turn()
            print(f"Turno de: {self.current_player}")
            return True
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
