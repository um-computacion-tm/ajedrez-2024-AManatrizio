from board import Board
class Chess:
    def __init__(self):
        self.board = Board()
    
    def move_piece(self, start_position, end_position):
        piece = self.board.get_piece(start_position)
        if piece and self.is_move_valid(piece, start_position, end_position):
            self.board.place_piece(piece, end_position)
            self.board.place_piece(None, start_position)
    
    def is_move_valid(self, piece, start_position, end_position):
       
        return True 
    
    def get_valid_moves(self, position):
        piece = self.board.get_piece(position)
        if piece:
            return piece.valid_moves(position, self.board)
        return []