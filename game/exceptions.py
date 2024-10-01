# exepciones

class ChessException(Exception):
    """Base exception class for the chess game."""
    pass

class InvalidMoveError(ChessException):
    """Raised when a move is not valid."""
    pass

class OutOfBoardError(ChessException):
    """Raised when a move is attempted outside the board."""
    pass

class PieceNotFoundError(ChessException):
    """Raised when trying to move a piece that doesn't exist."""
    pass

class SameColorCaptureError(ChessException):
    """Raised when trying to capture a piece of the same color."""
    pass