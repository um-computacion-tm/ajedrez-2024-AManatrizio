# Clase padre pieza 
# Abstracta

from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        self.__color__ = color
        self.__position__ = position

    @abstractmethod
    def move(self):
        pass