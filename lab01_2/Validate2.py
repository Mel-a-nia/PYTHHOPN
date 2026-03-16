def validate_name2 (name: str)-> None:
    if isinstance (name, str):
        if name.strip:
            pass
        else:
           raise ValueError("имя должно быть на str")
    else:
        raise TypeError("Пробелы не считаются именем")

def validate_salud2(HP: float)-> None:
    if isinstance(HP,(int,float)):
        if HP>0:
            pass
        else:
            raise ValueError("Здоровье (HP)  должно быть числовым")
    else:
        raise TypeError("невозможно иметь отрицательное здоровье (HP)")
    ##HP es salud 

def validate_level2(level: int) -> None:
    if  isinstance(level, int): 
        if (1 <= level <= 100):
            pass
        else:
            raise ValueError("Уровень должен быть числом от 1 до 100.")
    else:
        raise TypeError("Уровень должен быть целым числом")  
    
def validate_XP2(XP: int) -> None:
    if isinstance(XP, int):
        if XP>0:
            pass
        else:
            raise ValueError("Опыт (XP) не может быть отрицательным")
        
        raise TypeError("Опыт (XP) необходимо записывать целыми числами ")
    
##XP es experiencia 

def validate_status2(status: str) -> None:
    permitido = {"активный", "мертвый", "запрещенный"}
    if status not in permitido:
        raise ValueError(f"status должен быть одним из {permitido}")