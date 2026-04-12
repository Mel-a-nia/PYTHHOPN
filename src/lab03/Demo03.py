from lab03.Base import Player
from lab03.Model03 import Mago, Arquero
from lab02.collection import PlayerList

print("=" * 55)
print("  ESCENARIO 1 — Crear jugadores de distintos tipos")
print("=" * 55)

jugador_normal = Player("Inuyasha",   level=3, HP=100.0, XP=0)
mago1          = Mago("Naraku",    level=5, HP=80.0,  XP=0, mana=100, elemento="fuego")
mago2          = Mago("Miroku",     level=2, HP=70.0,  XP=0, mana=40,  elemento="hielo")
arquero1       = Arquero("Aome", level=4, HP=90.0,  XP=0, flechas=30, velocidad=15)
arquero2       = Arquero("Kikyo",   level=1, HP=100.0, XP=0, flechas=10, velocidad=8)

print(jugador_normal)
print(mago1)
print(arquero1)

print("\n-- descripcion() de cada uno --")
print(jugador_normal.descripcion())
print(mago1.descripcion())
print(arquero1.descripcion())

print("\n-- isinstance() --")
print(f"¿mago1 es Player?   {isinstance(mago1, Player)}")
print(f"¿mago1 es Mago?     {isinstance(mago1, Mago)}")
print(f"¿arquero1 es Mago?  {isinstance(arquero1, Mago)}")

print("\n" + "=" * 55)
print("  ESCENARIO 2 — Métodos propios de cada clase")
print("=" * 55)

print("-- Mago --")
print(mago2)
print(mago2.lanzar_hechizo())
print(mago2.lanzar_hechizo())
print(mago2.ganar_XP(50))   

print("\n-- Arquero --")
print(arquero2)
print(arquero2.disparar())
print(arquero2.disparar())
print(arquero2.recibir_daño(40))   

print("\n" + "=" * 55)
print("  ESCENARIO 3 — Colección con distintos tipos")
print("=" * 55)

lista = PlayerList()
lista.add(jugador_normal)
lista.add(mago1)
lista.add(mago2)
lista.add(arquero1)
lista.add(arquero2)

print(lista)

print("-- atacar() para todos sin usar if --")
for jugador in lista:
    print(f"  {jugador.atacar()}")


print("\n" + "=" * 55)
print("  ESCENARIO 4 — Estados y polimorfismo")
print("=" * 55)

mago_prueba = Mago("Dumbledore", level=3, HP=20.0, XP=0, mana=80, elemento="rayo")
print(mago_prueba)
print(mago_prueba.recibir_daño(20))
print(f"Estado: {mago_prueba.status}")

try:
    mago_prueba.lanzar_hechizo()
except RuntimeError as e:
    print(f"[Bloqueado] {e}")

mago_prueba.revivir()
print(f"\nDespués de revivir: {mago_prueba}")
print(mago_prueba.lanzar_hechizo())

arquero_prueba = Arquero("Ron Weasley", level=2, HP=100.0, XP=0, flechas=2, velocidad=12)
print(f"\n{arquero_prueba}")
print(arquero_prueba.disparar())
print(arquero_prueba.disparar())
print(arquero_prueba.disparar())  