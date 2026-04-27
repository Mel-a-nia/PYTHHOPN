from lab04.Model04 import Player, Mago, Arquero
from lab04.Collection04 import PlayerList
from lab04.Interfaces import Mostrable, Comparable

print("=" * 55)
print("  ESCENARIO 1 — Interfaz Mostrable")
print("=" * 55)

jugador = Player("Inuyasha", level=3, HP=100.0, XP=0)
mago    = Mago("Naraku",    level=5, HP=80.0,  XP=0, mana=100, elemento="fuego")
arquero = Arquero("Aome",   level=4, HP=90.0,  XP=0, flechas=30, velocidad=15)

print(jugador.mostrar())
print(mago.mostrar())
print(arquero.mostrar())

print(f"\n¿jugador es Mostrable?  {isinstance(jugador, Mostrable)}")
print(f"¿mago es Mostrable?     {isinstance(mago, Mostrable)}")
print(f"¿arquero es Mostrable?  {isinstance(arquero, Mostrable)}")

print("\n" + "=" * 55)
print("  ESCENARIO 2 — Interfaz Comparable")
print("=" * 55)

jugador2 = Player("Sesshomaru", level=8, HP=100.0, XP=0)
mago2    = Mago("Miroku",       level=2, HP=70.0,  XP=0, mana=40,  elemento="hielo")
arquero2 = Arquero("Kikyo",     level=1, HP=100.0, XP=0, flechas=10, velocidad=5)

resultado = jugador.comparar(jugador2)
if resultado > 0:
    print(f"{jugador._name} tiene mayor nivel que {jugador2._name}")
else:
    print(f"{jugador._name} tiene menor nivel que {jugador2._name}")

resultado = mago.comparar(mago2)
if resultado > 0:
    print(f"{mago._name} tiene mas mana que {mago2._name}")
else:
    print(f"{mago._name} tiene menos mana que {mago2._name}")

resultado = arquero.comparar(arquero2)
if resultado > 0:
    print(f"{arquero._name} tiene mas velocidad que {arquero2._name}")
else:
    print(f"{arquero._name} tiene menos velocidad que {arquero2._name}")

print(f"\n¿jugador es Comparable?  {isinstance(jugador, Comparable)}")
print(f"¿mago es Comparable?     {isinstance(mago, Comparable)}")

print("\n" + "=" * 55)
print("  ESCENARIO 3 — Función universal mostrar_info()")
print("=" * 55)

def mostrar_info(lista_objetos):
    for objeto in lista_objetos:
        if isinstance(objeto, Mostrable):
            print(f"  {objeto.mostrar()}")

objetos = [jugador, mago, arquero, jugador2, mago2, arquero2]
print("Mostrando todos a través de la interfaz:")
mostrar_info(objetos)

print("\n" + "=" * 55)
print("  ESCENARIO 4 — Filtros por interfaz en colección")
print("=" * 55)

lista = PlayerList()
lista.add(jugador)
lista.add(mago)
lista.add(arquero)
lista.add(jugador2)
lista.add(mago2)
lista.add(arquero2)

print("mostrar_todos() usando interfaz Mostrable:")
lista.mostrar_todos()

mostrables = lista.get_mostrables()
print(f"\nObjetos Mostrables en la lista: {len(mostrables)}")

comparables = lista.get_comparables()
print(f"Objetos Comparables en la lista: {len(comparables)}")

print("\n" + "=" * 55)
print("  ESCENARIO 5 — Ordenar usando Comparable")
print("=" * 55)

lista_jugadores = PlayerList()
lista_jugadores.add(Player("Goku",   level=9,  HP=100.0, XP=0))
lista_jugadores.add(Player("Vegeta", level=8,  HP=100.0, XP=0))
lista_jugadores.add(Player("Gohan",  level=3,  HP=100.0, XP=0))
lista_jugadores.add(Player("Krillin",level=2,  HP=100.0, XP=0))

print("Antes de ordenar:")
for j in lista_jugadores:
    print(f"  {j.mostrar()}")

lista_jugadores.ordenar_por_comparar()

print("\nDespués de ordenar por nivel (comparar()):")
for j in lista_jugadores:
    print(f"  {j.mostrar()}")