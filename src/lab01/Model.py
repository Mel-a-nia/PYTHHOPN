from lab01.Validate import (validate_name, validate_salud, validate_level, validate_experience,)
 
 
class Player:
    MAX_LEVEL: int = 100
    def __init__(self,name: str,level: int = 1,salud: float = 100.0,experience: int = 0,) -> None:
        validate_name(name)
        validate_level(level)
        validate_salud(salud)
        validate_experience(experience)

        self._name: str = name
        self._level: int = level
        self._salud: float = salud
        self._experience: int = experience
        self._status: str = "активный"

    @property
    def name(self) -> str:
        return self._name
 
    @property
    def level(self) -> int:
        return self._level
 
    @property
    def salud(self) -> float:
        return self._salud
 
    @property
    def experience(self) -> int:
        return self._experience
 
    @property
    def status(self) -> str:
        return self._status
 
    @salud.setter
    def salud(self, value: float) -> None:
        validate_salud(value)
        self._salud = value
        if self._salud == 0 and self._status == "активный":
            self._status = "мертвый"
 
    @experience.setter
    def experience(self, value: int) -> None:
        self._require_status("активный", action="приобрести опыт")
        validate_experience(value)
        self._experience = value
 
    def возродиться(self) -> None:
        if self._status != "мертвый":
            raise RuntimeError(f"Невозможно возродиться: игрок находится в статусе '{self._status}', а не 'мертвый'")
        self._salud = 100.0
        self._status = "активный"
 
    def бан(self) -> None:
        if self._status == "запрещенный":
            raise RuntimeError("Игрок уже забанен.")
        self._status = "запрещенный"
 
    def получить_урон(self, урон: float) -> str:
        self._require_status("активный", action="получить урон")
        if not isinstance(урон, (int, float)) or урон < 0:
            raise ValueError("Урон должен быть неотрицательным числом")
 
        self._salud = max(0.0, self._salud - урон)
        if self._salud == 0:
            self._status = "мертвый"
            return f"{self._name} получил {урон} урона и умер."   # ❌ era "получить" (infinitivo), corregido a "получил" (pasado)
        return f"{self._name} получил {урон} урона. HP: {self._salud:.1f}"
 
    def ganar_experiencia(self, points: int) -> str:
        self._require_status("активный", action="приобрести опыт")
        validate_experience(points)
 
        self._experience += points
        leveled_up = False
 
        while self._experience >= self._level * 100 and self._level < Player.MAX_LEVEL:
            self._experience -= self._level * 100
            self._level += 1
            leveled_up = True
 
        if leveled_up:
            return (f"{self._name} получил {points} XP и повысил уровень! "
                f"Теперь уровень {self._level} (XP: {self._experience}).")
        return f"{self._name} получил {points} XP. Всего XP: {self._experience}."

    def __str__(self) -> str:
        return (
            f"Player '{self._name}' | "
            f"Level: {self._level} | "
            f"HP: {self._salud:.1f} | "
            f"XP: {self._experience} | "
            f"Status: {self._status.upper()}"
        )
 
    def __repr__(self) -> str:
        return (
            f"Player(name={self._name!r}, level={self._level}, " 
            f"salud={self._salud}, experience={self._experience})" )
 
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Player):
            return NotImplemented
        return self._name == other._name and self._level == other._level
 
    def _require_status(self, required: str, action: str = "realizar acción") -> None:
        if self._status != required:
            raise RuntimeError(f"Невозможно {action}: игрок '{self._name}' "
                                f"находится в статусе '{self._status}', а не '{required}'.")