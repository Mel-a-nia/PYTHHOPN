from lab01_2.Model3 import Player

print("=" * 50)
print("  ESCENARIO 1 — Crear jugadores y compararlos")
print("=" * 50)
 
p1 = Player("Mario", level=5, HP=120.0, XP=50)
p2 = Player("Mario", level=5, HP=80.0, XP=200)
p3 = Player("Dan Ramón", level=3, HP=100.0, XP=0)
 
print(p1)
print(repr(p1))
 
print(f"\np1 == p2: {p1 == p2}")   
print(f"p1 == p3: {p1 == p3}")    
 
print(f"\nPlayer.MAX_LEVEL = {Player.MAX_LEVEL}")   
print(f"p1.MAX_LEVEL     = {p1.MAX_LEVEL}")        
 
print("\n" + "=" * 50)
print("  ESCENARIO 2 — Daño y experiencia")
print("=" * 50)
 
heroe = Player("Link", level=1, HP=100.0, XP=0)
print(heroe)
 
print(heroe.ganar_XP(80))
print(heroe.ganar_XP(30))  
 
print(heroe.recibir_daño(25))
print(heroe.recibir_daño(40))
 
heroe.HP = 100.0           
print(f"\nDespués de curar: {heroe}")
 
print("\n" + "=" * 50)
print("  ESCENARIO 3 — Muerte y revivir")
print("=" * 50)
 
guerrero = Player("Kratos", level=3, HP=30.0, XP=0)
print(guerrero)
 
print(guerrero.recibir_daño(30))   
print(f"Estado: {guerrero.status}")
 
try:
    guerrero.ganar_XP(50)           
except RuntimeError as e:
    print(f"[Bloqueado] {e}")
 
guerrero.revivir()
print(f"\nDespués de revivir: {guerrero}")
 
print("\n" + "=" * 50)
print("  ESCENARIO 4 — Jugador baneado")
print("=" * 50)
 
trampa = Player("Hacker123", level=2, HP=100.0)
trampa.banear()
print(f"Estado: {trampa.status}")
 
try:
    trampa.recibir_danio(10)
except RuntimeError as e:
    print(f"[Bloqueado] {e}")
 
try:
    trampa.ganar_XP(999)
except RuntimeError as e:
    print(f"[Bloqueado] {e}")
 
print("\n" + "=" * 50)
print("  ESCENARIO 5 — Validaciones incorrectas")
print("=" * 50)

try:
    Player("")                          
except ValueError as e:
    print(f"  x {e}")
 
try:
    Player("Bob", level=0)              
except ValueError as e:
    print(f"  x {e}")
 
try:
    Player("Bob", level=101)            
except ValueError as e:
    print(f"  x {e}")
 
try:
    Player("Bob", HP=-10.0)             
except ValueError as e:
    print(f"  x {e}")
 
try:
    Player("Bob", XP=-5)               
except ValueError as e:
    print(f"  x {e}")
 
try:
    Player(123)                       
except TypeError as e:
    print(f"  x {e}")
 
try:
    Player("Samus").HP = -50          
except ValueError as e:
    print(f"  x Setter rechazó: {e}")
 