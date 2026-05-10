from lab04.Model04 import Player as PlayerBase
from lab04.Model04 import Mago as MagoBase
from lab04.Model04 import Arquero as ArqueroBase

class Player(PlayerBase):

    def __init__(self, name: str, level: int = 1, HP: float = 100.0, XP: int = 0) -> None:
        super().__init__(name, level, HP, XP)

    def display(self) -> str:
        return f"[Jugador] {self._name} | Nivel: {self._level} | HP: {self._HP} | Estado: {self._status}"

    def score(self) -> float:
        return float(self._level * 100 + self._XP)


class Mago(MagoBase):

    def __init__(self, name: str, level: int = 1, HP: float = 100.0, XP: int = 0, mana: int = 50, elemento: str = "fuego") -> None:
        super().__init__(name, level, HP, XP, mana, elemento)

    def display(self) -> str:
        return f"[Mago] {self._name} de {self._elemento} | Nivel: {self._level} | Mana: {self._mana} | Estado: {self._status}"

    def score(self) -> float:
        return float(self._level * 100 + self._mana)


class Arquero(ArqueroBase):

    def __init__(self, name: str, level: int = 1, HP: float = 100.0, XP: int = 0, flechas: int = 20, velocidad: int = 10) -> None:
        super().__init__(name, level, HP, XP, flechas, velocidad)

    def display(self) -> str:
        return f"[Arquero] {self._name} | Nivel: {self._level} | Flechas: {self._flechas} | Velocidad: {self._velocidad} | Estado: {self._status}"

    def score(self) -> float:
        return float(self._level * 100 + self._velocidad)