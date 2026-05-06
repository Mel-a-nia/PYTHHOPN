from lab01_2.Model3 import Player
from lab03.Model03 import Mago, Arquero
from lab05.collection05 import PlayerList
from lab05.Estrategias import (
    por_nombre, por_nivel, por_hp, por_nivel_y_nombre,
    es_activo, es_alto_nivel,
    hacer_filtro_nivel, hacer_filtro_hp,
    a_resumen, a_nombre,
    EstrategiaOrdenarPorNivel, EstrategiaOrdenarPorHP, EstrategiaOrdenarPorNombre,
)


def crear_lista():
    lista = PlayerList()
    lista.add(Player("Sasha",  level=7, HP=100.0, XP=0))
    lista.add(Player("Connie",  level=8, HP=85.0,  XP=0))
    lista.add(Player("El amigo de Sasha y Connie",  level=3, HP=90.0,  XP=0))
    lista.add(Mago("Eren",   level=29, HP=75.0,  XP=0, mana=100, elemento="rayo"))
    lista.add(Mago("Armin",    level=15, HP=60.0,  XP=0, mana=80,  elemento="fuego"))
    lista.add(Arquero("Levi",   level=20, HP=95.0,  XP=0, flechas=20, velocidad=12))
    lista.add(Arquero("Mikasa", level=19, HP=100.0, XP=0, flechas=15, velocidad=8))
    return lista


print("=" * 55)
print("  ESCENARIO 1 — Ordenar y filtrar con estrategias")
print("=" * 55)

lista = crear_lista()

print("Ordenado por nombre:")
for j in sorted(lista, key=por_nombre):
    print(f"  {j.name}")

print("\nOrdenado por nivel:")
for j in sorted(lista, key=por_nivel):
    print(f"  {j.name} - nivel {j.level}")

print("\nOrdenado por HP:")
for j in sorted(lista, key=por_hp):
    print(f"  {j.name} - HP {j.HP}")

print("\nOrdenado por nivel y nombre:")
for j in sorted(lista, key=por_nivel_y_nombre):
    print(f"  {j.name} - nivel {j.level}")

print("\nSolo activos (con filter):")
for j in list(filter(es_activo, lista)):
    print(f"  {j.name}")

print("\nSolo nivel alto con filter (nivel >= 5):")
for j in list(filter(es_alto_nivel, lista)):
    print(f"  {j.name} - nivel {j.level}")


print("\n" + "=" * 55)
print("  ESCENARIO 2 — map, fábrica de funciones y sort_by")
print("=" * 55)

lista = crear_lista()

print("map a_resumen:")
for r in list(map(a_resumen, lista)):
    print(f"  {r}")

print("\nmap a_nombre (solo nombres):")
print(f"  {list(map(a_nombre, lista))}")

filtro_nivel_4 = hacer_filtro_nivel(4)
filtro_nivel_7 = hacer_filtro_nivel(7)
filtro_hp_90   = hacer_filtro_hp(90)

print("\nFabrica - nivel >= 4:")
for j in list(filter(filtro_nivel_4, lista)):
    print(f"  {j.name} - nivel {j.level}")

print("\nFabrica - nivel >= 7:")
for j in list(filter(filtro_nivel_7, lista)):
    print(f"  {j.name} - nivel {j.level}")

print("\nFabrica - HP >= 90:")
for j in list(filter(filtro_hp_90, lista)):
    print(f"  {j.name} - HP {j.HP}")

print("\nsort_by(por_nivel):")
lista.sort_by(por_nivel)
for j in lista:
    print(f"  {j.name} - nivel {j.level}")

print("\nfilter_by(es_alto_nivel):")
for j in lista.filter_by(es_alto_nivel):
    print(f"  {j.name} - nivel {j.level}")

print("\nfilter_by con lambda (nivel >= 5):")
for j in lista.filter_by(lambda j: j.level >= 5):
    print(f"  {j.name} - nivel {j.level}")

print("\nmap_to a_resumen:")
for r in lista.map_to(a_resumen):
    print(f"  {r}")


print("\n" + "=" * 55)
print("  ESCENARIO 3 — Callable objects (patrón Estrategia)")
print("=" * 55)

lista = crear_lista()

estrategia_nivel  = EstrategiaOrdenarPorNivel()
estrategia_hp     = EstrategiaOrdenarPorHP()
estrategia_nombre = EstrategiaOrdenarPorNombre()

print("Estrategia: ordenar por nivel")
lista.sort_by(estrategia_nivel)
for j in lista:
    print(f"  {j.name} - nivel {j.level}")

print("\nEstrategia: ordenar por HP")
lista.sort_by(estrategia_hp)
for j in lista:
    print(f"  {j.name} - HP {j.HP}")

print("\nEstrategia: ordenar por nombre")
lista.sort_by(estrategia_nombre)
for j in lista:
    print(f"  {j.name}")

print("\napply - curar a todos (HP = 100):")
def curar(jugador):
    jugador.HP = 100.0

lista.apply(curar)
for j in lista:
    print(f"  {j.name} - HP {j.HP}")

print("\nCadena: filter_by(nivel>=5) luego sort_by(por_hp):")
for j in lista.filter_by(es_alto_nivel).sort_by(por_hp):
    print(f"  {j.name} - nivel {j.level} | HP {j.HP}")