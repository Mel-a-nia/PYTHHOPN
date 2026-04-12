from lab03.Base import Player
 
 
class Mago(Player):

    def __init__(self, name, level=1, HP=100.0, XP=0, mana=50, elemento="fuego"):
        super().__init__(name, level, HP, XP) 
        self._mana = mana
        self._elemento = elemento

    @property
    def mana(self):
        return self._mana
    @property
    def elemento(self):
        return self._elemento

    def lanzar_hechizo(self):
        if self._status == "активный":
            if self._mana >= 10:
                self._mana = self._mana - 10
                return f"{self._name} lanzó un hechizo de {self._elemento}! Mana restante: {self._mana}"
            else:
                return f"{self._name} no tiene suficiente mana"
        else:
            raise RuntimeError(f"No se puede lanzar hechizo: el jugador está '{self._status}'")

    def ganar_XP(self, points):
        puntos_dobles = points * 2
        return super().ganar_XP(puntos_dobles)
 
    def atacar(self):
        return self.lanzar_hechizo()

    def descripcion(self):
        return f"Mago '{self._name}' de {self._elemento} | Mana: {self._mana}"
 
    def __str__(self):
        return f"Mago '{self._name}' | Nivel: {self._level} | HP: {self._HP} | Mana: {self._mana} | Elemento: {self._elemento} | Estado: {self._status}"
    
class Arquero(Player):

    def __init__(self, name, level=1, HP=100.0, XP=0, flechas=20, velocidad=10):
        super().__init__(name, level, HP, XP) 
        self._flechas = flechas
        self._velocidad = velocidad
 
    @property
    def flechas(self):
        return self._flechas
 
    @property
    def velocidad(self):
        return self._velocidad
 
    def disparar(self):
        if self._status == "активный":
            if self._flechas > 0:
                self._flechas = self._flechas - 1
                return f"{self._name} disparó una flecha! Flechas restantes: {self._flechas}"
            else:
                return f"{self._name} no tiene flechas"
        else:
            raise RuntimeError(f"No se puede disparar: el jugador está '{self._status}'")

    def recibir_daño(self, damage):
        daño_reducido = damage / 2
        return super().recibir_daño(daño_reducido)

    def atacar(self):
        return self.disparar()

    def descripcion(self):
        return f"Arquero '{self._name}' | Flechas: {self._flechas} | Velocidad: {self._velocidad}"
 
    def __str__(self):
        return f"Arquero '{self._name}' | Nivel: {self._level} | HP: {self._HP} | Flechas: {self._flechas} | Velocidad: {self._velocidad} | Estado: {self._status}"