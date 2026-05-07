from lab01_2.Model3 import Player as PlayerBase

class PlayerList:
    def __init__(self):
        self._items = []

    def add(self, jugador):
        if isinstance(jugador, PlayerBase):
            if jugador in self._items:
                raise ValueError('El jugador ya esta en la lista')
            else:
                self._items.append(jugador)
        else:
            raise TypeError('Solo se pueden agregar objetos de tipo Player')

    def remove(self, jugador):
        if jugador in self._items:
            self._items.remove(jugador)
        else:
            raise ValueError('El jugador no esta en la lista')

    def get_all(self):
        return self._items

    def sort_by(self, funcion_clave):
        self._items = sorted(self._items, key=funcion_clave)
        return self

    def filter_by(self, funcion_filtro):
        resultado = PlayerList()
        for jugador in list(filter(funcion_filtro, self._items)):
            resultado.add(jugador)
        return resultado

    def apply(self, funcion):
        for jugador in self._items:
            funcion(jugador)
        return self

    def map_to(self, funcion):
        return list(map(funcion, self._items))

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, indice):
        return self._items[indice]

    def __str__(self):
        if len(self._items) == 0:
            return 'PlayerList: vacia'
        else:
            texto = 'PlayerList (' + str(len(self._items)) + ' jugadores):' + chr(10)
            for i in range(len(self._items)):
                texto = texto + '  [' + str(i) + '] ' + str(self._items[i]) + chr(10)
            return texto