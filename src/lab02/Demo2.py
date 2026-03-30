from lab02.Model import Player
from lab02.collection import PlayerList
 

print("=" * 50)
print("  ESCENARIO 1 — Agregar y eliminar jugadores")
print("=" * 50)
 
lista = PlayerList()
 
p1 = Player("Mario",   level=5,  HP=120.0, XP=50)
p2 = Player("Link",    level=3,  HP=100.0, XP=200)
p3 = Player("Kratos",  level=8,  HP=80.0,  XP=0)
p4 = Player("Samus",   level=2,  HP=100.0, XP=10)
 
lista.add(p1)
lista.add(p2)
lista.add(p3)
lista.add(p4)
 
print(lista)
 
lista.remove(p2)
print(f"\nDespués de eliminar a Link:")
print(lista)
 
try:
    lista.add("no soy un Player")
except TypeError as e:
    print(f"\n  x {e}")

try:
    lista.add(p1)
except ValueError as e:
    print(f"  x {e}")

print("\n" + "=" * 50)
print("  ESCENARIO 2 — len, for y búsqueda")
print("=" * 50)
 
print(f"Total de jugadores: {len(lista)}")
 
print("\nIterando con for:")
for player in lista:
    print(f"  - {player.name} | Nivel {player.level} | HP {player.HP}")
 
print(f"\nBuscar 'Mario':   {lista.find_by_name('Mario')}")
print(f"Buscar 'Luigi':   {lista.find_by_name('Luigi')}")   # no existe → None
 
por_nivel = lista.find_by_level(5)
print(f"\nJugadores nivel 5:")
print(por_nivel)
 
print("\n" + "=" * 50)
print("  ESCENARIO 3 — Índices y remove_at")
print("=" * 50)
 
print(f"lista[0] → {lista[0]}")
print(f"lista[1] → {lista[1]}")
 
eliminado = lista.remove_at(1)
print(f"\nEliminado en índice 1: {eliminado.name}")
print(lista)

try:
    lista.remove_at(99)
except IndexError as e:
    print(f"\n  x {e}")
 
print("  ESCENARIO 4 — Ordenar la colección")
print("=" * 50)
 
lista2 = PlayerList()
lista2.add(Player("Zelda",  level=7,  HP=90.0,  XP=300))
lista2.add(Player("Arthur", level=2,  HP=100.0, XP=50))
lista2.add(Player("Mega",   level=10, HP=60.0,  XP=900))
lista2.add(Player("Cloud",  level=5,  HP=120.0, XP=150))
 
lista2.sort_by_name()
print("Ordenado por nombre:")
for p in lista2:
    print(f"  {p.name}")
 
lista2.sort_by_level()
print("\nOrdenado por nivel:")
for p in lista2:
    print(f"  {p.name} — nivel {p.level}")
 
lista2.sort_by_hp()
print("\nOrdenado por HP:")
for p in lista2:
    print(f"  {p.name} — HP {p.HP}")

print("\n" + "=" * 50)
print("  ESCENARIO 5 — Filtros")
print("=" * 50)
 
lista3 = PlayerList()
vivo1  = Player("Vivo1",  level=3, HP=100.0, XP=0)
vivo2  = Player("Vivo2",  level=6, HP=80.0,  XP=0)
muerto = Player("Muerto", level=2, HP=20.0,  XP=0)
muerto.recibir_daño(20)   # lo matamos
 
lista3.add(vivo1)
lista3.add(vivo2)
lista3.add(muerto)
 
activos = lista3.get_active()
print(f"Jugadores activos ({len(activos)}):")
print(activos)
 
muertos = lista3.get_dead()
print(f"\nJugadores muertos ({len(muertos)}):")
print(muertos)
 
elite = lista3.get_high_level(5)
print(f"\nJugadores nivel 5 o más ({len(elite)}):")
print(elite)
 