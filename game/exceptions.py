# Exepciones

class ChessError(Exception):
    """Clase base para todas las excepciones relacionadas con el ajedrez."""
    pass

class InvalidMoveError(ChessError):
    """Excepción para movimientos inválidos."""
    def __init__(self, message="Movimiento no permitido para esta pieza."):
        self.message = message
        super().__init__(self.message)

class PieceNotFoundError(ChessError):
    """Excepción cuando no se encuentra una pieza en la posición indicada."""
    def __init__(self, message="No hay ninguna pieza en la posición especificada."):
        self.message = message
        super().__init__(self.message)

class OutOfBoardError(ChessError):
    """Excepción para movimientos que salen fuera del tablero."""
    def __init__(self, message="El movimiento está fuera de los límites del tablero."):
        self.message = message
        super().__init__(self.message)
