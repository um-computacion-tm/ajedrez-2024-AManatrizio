from board import Board
class Chess:
    def __init__(self):
        self.board = Board() # Creo objeto board
        self.current_player = "WHITE" # Inicializo el primer jugador en blanco

    def is_over(self):
        # Implementar lógica para determinar si el juego ha terminado
        pass

    def display_board(self):
        self.board.display_board()

    def play_move(self, move):
        initial_pos, final_pos = self.parse_move(move)
        if self.board.is_valid_move(initial_pos, final_pos, self.current_player):
            self.board.move_piece(initial_pos, final_pos)
            self.switch_turn()
            return True
        return False

    def parse_move(self, move):
        # Convertir el movimiento (e.g., e2 e4) en coordenadas
        pass


    # Cambio de turno
    def switch_turn(self):
        self.current_player = "BLACK" if self.current_player == "WHITE" else "WHITE"
