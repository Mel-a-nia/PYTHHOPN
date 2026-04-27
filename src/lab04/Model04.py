from lab01_2.Model3 import Player as PlayerBase
from lab03.Model03 import Mago as MagoBase
from lab03.Model03 import Arquero as ArqueroBase
from lab04.Interfaces import Mostrable, Comparable

class Player(PlayerBase, Mostrable, Comparable):

    def mostrar(self):
        return f"[Jugador] {self._name} | Nivel: {self._level} | HP: {self._HP} | Estado: {self._status}"

    def comparar(self, otro):
        return self._level - otro.level

class Mago(MagoBase, Mostrable, Comparable):

    def mostrar(self):
        return f"[Mago] {self._name} de {self._elemento} | Nivel: {self._level} | Mana: {self._mana} | Estado: {self._status}"

    def comparar(self, otro):
        return self._mana - otro.mana

class Arquero(ArqueroBase, Mostrable, Comparable):

    def mostrar(self):
        return f"[Arquero] {self._name} | Nivel: {self._level} | Flechas: {self._flechas} | Velocidad: {self._velocidad} | Estado: {self._status}"

    def comparar(self, otro):
        return self._velocidad - otro.velocidad