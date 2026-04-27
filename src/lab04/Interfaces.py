
from abc import ABC, abstractmethod

class Mostrable(ABC): 
    @abstractmethod
    def mostrar(self):
        pass
    
class Comparable(ABC):
    @abstractmethod
    def comparar(self, otro):
        pass
 