from lab01_2.Model3 import Player

def descripcion(self):
    return f"Jugador básico '{self._name}'"

Player.descripcion = descripcion

def atacar(self):
    return f"{self._name} ataca de forma básica"

Player.atacar = atacar