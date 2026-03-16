from lab01.Model import Player
 
 
def separator(title: str) -> None:
    print(f"\n{'=' * 55}")
    print(f"  {title}")
    print('=' * 55)

separator("Сценарий 1")
 
p1 = Player(name="Mario", level=5, salud=120.0, experience=50)
p2 = Player(name="Mario", level=5, salud=80.0, experience=200)
p3 = Player(name="Pepe", level=10, salud=100.0, experience=0)
 
print(p1)            #__str__
print(repr(p1))      #el otro
 
print(f"\np1 == p2 (одинаковое имя и уровень): {p1 == p2}")   
print(f"p1 == p3 (Другой игрок):  {p1 == p3}")   
 
print(f"\nPlayer.MAX_LEVEL = {Player.MAX_LEVEL}")
print(f"p1.MAX_LEVEL     = {p1.MAX_LEVEL}")

separator("Сценарий 2")
 
heroe = Player(name="Marce", level=1, salud=100.0, experience=0)
print(heroe)
 
print(heroe.ganar_experiencia(80))    
print(heroe.ganar_experiencia(30))    
 
print(heroe.получить_урон(25))
print(heroe.получить_урон(40))

heroe.salud = 200.0
print(f"\nПосле заживления:  {heroe}")
 
separator("Сценарий 3" )
 
Guerrero = Player(name="Garrosh", level=3, salud=30.0, experience=0)
print(Guerrero)
 
print(Guerrero.получить_урон(30))   
print(f"Состояние после получения смертельных повреждений: {Guerrero.status}")
 
try:
    Guerrero.ganar_experiencia(50)
except RuntimeError as e:
    print(f"[Blocked] {e}")

Guerrero.возродиться()
print(f"\nПосле возродиться:  {Guerrero}")
print(Guerrero.ganar_experiencia(100))   
 
separator("Сценарий 4")
 
Tramposo = Player(name="h4x0r", level=2, salud=100.0)
Tramposo.бан()
print(f"Status: {Tramposo.status}")
 
try:
    Tramposo.получить_урон(10)
except RuntimeError as e:
    print(f"[Blocked] {e}")
 
try:
    Tramposo.ganar_experiencia(999)
except RuntimeError as e:
    print(f"[Blocked] {e}")
 
try:
    Tramposo.возродиться()          
except RuntimeError as e:
    print(f"[Blocked] {e}")
 

separator("Сценарий 5")
 
bad_inputs = [
    dict(name="",     level=1,   salud=100.0, experience=0),   
    dict(name="Bob",  level=0,   salud=100.0, experience=0),  
    dict(name="Bob",  level=101, salud=100.0, experience=0),  
    dict(name="Bob",  level=1,   salud=-5.0,  experience=0),  
    dict(name="Bob",  level=1,   salud=100.0, experience=-1), 
    dict(name=42,     level=1,   salud=100.0, experience=0),  
]
 
for kwargs in bad_inputs:
    try:
        Player(**kwargs)
    except (TypeError, ValueError) as e:
        print(f"  X {e}")
 
valid_player = Player("Maria")
try:
    valid_player.health = -50
except ValueError as e:
    print(f" X Сеттер отклоне: {e}")