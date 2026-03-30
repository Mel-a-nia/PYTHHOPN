from lab01_2.Model3 import Player


class PlayerList:

    def __init__(self):
        self._items = []


    def add(self, player):
        if isinstance(player, Player):
            if player in self._items:
                raise ValueError(f"El jugador '{player.name}' ya está en la lista")
            else:
                self._items.append(player)
        else:
            raise TypeError("Solo se pueden agregar objetos de tipo Player")

    def remove(self, player):
        if player in self._items:
            self._items.remove(player)
        else:
            raise ValueError(f"El jugador '{player.name}' no está en la lista")

    def remove_at(self, indice):
        if indice >= 0 and indice < len(self._items):
            eliminado = self._items[indice]
            self._items.pop(indice)
            return eliminado
        else:
            raise IndexError(f"Índice {indice} fuera de rango")


    def get_all(self):
        return self._items

    def find_by_name(self, nombre):
        for jugador in self._items:
            if jugador.name == nombre:
                return jugador
        return None

    def find_by_level(self, nivel):
        resultado = PlayerList()
        for jugador in self._items:
            if jugador.level == nivel:
                resultado.add(jugador)
        return resultado

    def get_active(self):
        resultado = PlayerList()
        for jugador in self._items:
            if jugador.status == "активный":
                resultado.add(jugador)
        return resultado

    def get_dead(self):
        resultado = PlayerList()
        for jugador in self._items:
            if jugador.status == "мертвый":
                resultado.add(jugador)
        return resultado

    def get_high_level(self, nivel_minimo):
        resultado = PlayerList()
        for jugador in self._items:
            if jugador.level >= nivel_minimo:
                resultado.add(jugador)
        return resultado
    def sort_by_name(self):
        total = len(self._items)
        for i in range(total):
            for j in range(0, total - i - 1):
                if self._items[j].name > self._items[j + 1].name:
                    temporal = self._items[j]
                    self._items[j] = self._items[j + 1]
                    self._items[j + 1] = temporal

    def sort_by_level(self):
        total = len(self._items)
        for i in range(total):
            for j in range(0, total - i - 1):
                if self._items[j].level > self._items[j + 1].level:
                    temporal = self._items[j]
                    self._items[j] = self._items[j + 1]
                    self._items[j + 1] = temporal

    def sort_by_hp(self):
        total = len(self._items)
        for i in range(total):
            for j in range(0, total - i - 1):
                if self._items[j].HP > self._items[j + 1].HP:
                    temporal = self._items[j]
                    self._items[j] = self._items[j + 1]
                    self._items[j + 1] = temporal
    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __str__(self):
        if len(self._items) == 0:
            return "PlayerList: vacía"
        else:
            texto = f"PlayerList ({len(self._items)} jugadores):\n"
            for i in range(len(self._items)):
                texto = texto + f"  [{i}] {self._items[i]}\n"
            return texto

    def __repr__(self):
        return f"PlayerList(count={len(self._items)})"