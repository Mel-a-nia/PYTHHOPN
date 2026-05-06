from lab02.collection import PlayerList as PlayerListBase


class PlayerList(PlayerListBase):

    def sort_by(self, funcion_clave):
        self._items = sorted(self._items, key=funcion_clave)
        return self

    def filter_by(self, funcion_filtro):
        resultado = PlayerList()
        for jugador in self._items:
            if funcion_filtro(jugador):
                resultado._items.append(jugador)
        return resultado

    def apply(self, funcion):
        for jugador in self._items:
            funcion(jugador)
        return self

    def map_to(self, funcion_transformacion):
        resultado = []
        for jugador in self._items:
            resultado.append(funcion_transformacion(jugador))
        return resultado