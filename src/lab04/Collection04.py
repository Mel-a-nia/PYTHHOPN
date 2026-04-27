from lab02.collection import PlayerList as PlayerListBase
from lab04.Interfaces import Mostrable, Comparable


class PlayerList(PlayerListBase):

    def get_mostrables(self):
        resultado = PlayerList()
        for jugador in self._items:
            if isinstance(jugador, Mostrable):
                resultado.add(jugador)
        return resultado

    def get_comparables(self):
        resultado = PlayerList()
        for jugador in self._items:
            if isinstance(jugador, Comparable):
                resultado.add(jugador)
        return resultado

    def mostrar_todos(self):
        for jugador in self._items:
            if isinstance(jugador, Mostrable):
                print(jugador.mostrar())

    def ordenar_por_comparar(self):
        total = len(self._items)
        for i in range(total):
            for j in range(0, total - i - 1):
                if self._items[j].comparar(self._items[j + 1]) > 0:
                    temporal = self._items[j]
                    self._items[j] = self._items[j + 1]
                    self._items[j + 1] = temporal