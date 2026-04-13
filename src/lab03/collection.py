from lab02.collection import PlayerList as PlayerListBase
from lab03.Model03 import Mago, Arquero
from lab01_2.Model3 import Player
 
 
class PlayerList(PlayerListBase):
 
    def get_solo_magos(self):
        resultado = PlayerList()
        for jugador in self._items:
            if isinstance(jugador, Mago):
                resultado.add(jugador)
        return resultado
 
    def get_solo_arqueros(self):
        resultado = PlayerList()
        for jugador in self._items:
            if isinstance(jugador, Arquero):
                resultado.add(jugador)
        return resultado
 
    def get_solo_jugadores_base(self):
        resultado = PlayerList()
        for jugador in self._items:
            if type(jugador) == Player:
                resultado.add(jugador)
        return resultado
 