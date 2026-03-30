def validate_name(name:str)-> None:
    if not isinstance (name , str):
        raise TypeError("имя должно быть на str")
    if not name.strip:
        raise ValueError("Пробелы не считаются именем")
    
def validate_salud(HP:float)-> None:
    if not isinstance(HP, (float, int)):
        raise TypeError ("Здоровье должно быть числовым")
    if  HP<0:
        raise ValueError ("невозможно иметь отрицательное здоровье")

def validate_level(level: int) -> None:
    if not isinstance(level, int):
        raise TypeError("Уровень должен быть целым числом.")
    if not (1 <= level <= 100):
        raise ValueError("Уровень должен быть числом от 1 до 100.")
    
def validate_experience(experience: int) -> None:
    if not isinstance(experience, int):
        raise TypeError("Опыт необходимо записывать целыми числами ")
    if experience < 0:
        raise ValueError("Опыт не может быть отрицательным")


def validate_status(status: str) -> None:
    permitido = {"активный", "мертвый", "запрещенный"}
    if status not in permitido:
        raise ValueError (f"status должен быть одним из {permitido}")