# Clase padre pieza 
# Abstracta

from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color):
        self.__color__ = color

    @abstractmethod
    def move(self):
        pass