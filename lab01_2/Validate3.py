def validate_name(name: str) -> None:
    if isinstance(name, str):
        if name.strip():
            pass
        else:
            raise ValueError("El nombre no puede estar vacío")
    else:
        raise TypeError("El nombre debe ser texto (str)")

def validate_salud(HP: float) -> None:
    if isinstance(HP, (int, float)):
        if HP >= 0:
            pass
        else:
            raise ValueError("La salud (HP) no puede ser negativa")
    else:
        raise TypeError("La salud (HP) debe ser un número")

def validate_level(level: int) -> None:
    if isinstance(level, int):
        if 1 <= level <= 100:
            pass
        else:
            raise ValueError("El nivel debe estar entre 1 y 100")
    else:
        raise TypeError("El nivel debe ser un número entero")

def validate_XP(XP: int) -> None:
    if isinstance(XP, int):
        if XP >= 0:
            pass
        else:
            raise ValueError("El XP no puede ser negativo")
    else:
        raise TypeError("El XP debe ser un número entero")