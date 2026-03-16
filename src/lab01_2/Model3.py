from lab01_2.Validate3 import validate_name, validate_salud, validate_level, validate_XP


class Player:
    MAX_LEVEL = 100  
    def __init__(self, name, level=1, HP=100.0, XP=0):
        validate_name(name)
        validate_level(level)
        validate_salud(HP)
        validate_XP(XP)

        self._name = name
        self._level = level
        self._HP = HP
        self._XP = XP
        self._status = "активный"

    @property
    def name(self):
        return self._name

    @property
    def level(self):
        return self._level

    @property
    def HP(self):
        return self._HP

    @property
    def XP(self):
        return self._XP

    @property
    def status(self):
        return self._status

    @HP.setter
    def HP(self, value):
        validate_salud(value)
        self._HP = value
        if self._HP == 0:
            self._status = "мертвый"

    def revivir(self):
        if self._status == "мертвый":
            self._HP = 100.0
            self._status = "активный"
        else:
            raise RuntimeError("Solo se puede revivir si el jugador está muerto")

    def banear(self):
        if self._status == "запрещенный":
            raise RuntimeError("El jugador ya está baneado")
        else:
            self._status = "запрещенный"

    def recibir_daño(self, damage):
        if self._status == "активный":
            if damage < 0:
                raise ValueError("El daño no puede ser negativo")
            else:
                self._HP = self._HP - damage
                if self._HP <= 0:
                    self._HP = 0
                    self._status = "мертвый"
                    return f"{self._name} recibió {damage} de daño y murió."
                else:
                    return f"{self._name} recibió {damage} de daño. HP: {self._HP}"
        else:
            raise RuntimeError(f"No se puede dañar: el jugador está '{self._status}'")

    def ganar_XP(self, points):
        if self._status == "активный":
            self._XP = self._XP + points
            if self._XP >= self._level * 100 and self._level < Player.MAX_LEVEL:
                self._XP = self._XP - self._level * 100
                self._level = self._level + 1
                return f"{self._name} subió al nivel {self._level}!"
            else:
                return f"{self._name} ganó {points} XP. Total: {self._XP}"
        else:
            raise RuntimeError(f"No se puede ganar XP: el jugador está '{self._status}'")

    
    def __str__(self):
        return f"Player '{self._name}' | Nivel: {self._level} | HP: {self._HP} | XP: {self._XP} | Estado: {self._status}"

    def __repr__(self):
        return f"Player(name='{self._name}', level={self._level}, HP={self._HP}, XP={self._XP})"

    def __eq__(self, other):
        if isinstance(other, Player):
            return self._name == other._name and self._level == other._level
        else:
            return NotImplemented