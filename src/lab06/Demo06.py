from lab06.Model06 import Player, Mago, Arquero
from lab06.Contenedor import TypedCollection, Displayable, Scorable

print("=" * 55)
print("  ESCENARIO 1 — TypedCollection basica")
print("=" * 55)

coleccion: TypedCollection[Player] = TypedCollection()

coleccion.add(Player("Totoro",  level=7, HP=100.0, XP=50))
coleccion.add(Player("Chihiro",  level=8, HP=85.0,  XP=30))
coleccion.add(Player("Sosuke",  level=3, HP=90.0,  XP=10))
coleccion.add(Mago("Howl",   level=9, HP=75.0,  XP=0, mana=100, elemento="rayo"))
coleccion.add(Arquero("Ponyo",   level=5, HP=95.0,  XP=0, flechas=20, velocidad=12))

print(coleccion)

todos = coleccion.get_all()
print(f"Total de elementos: {len(todos)}")

print("\n" + "=" * 55)
print("  ESCENARIO 2 — find(), filter() y map()")
print("=" * 55)

encontrado = coleccion.find(lambda j: j.level >= 8)
print(f"find(nivel >= 8): {encontrado.name if encontrado else None}")

no_encontrado = coleccion.find(lambda j: j.level >= 99)
print(f"find(nivel >= 99): {no_encontrado}")

nivel_alto = coleccion.filter(lambda j: j.level >= 5)
print(f"\nfilter(nivel >= 5) — {len(nivel_alto)} jugadores:")
for j in nivel_alto:
    print(f"  {j.name} | nivel {j.level}")

nombres = coleccion.map(lambda j: j.name)
print(f"\nmap a nombres (list[str]): {nombres}")

niveles = coleccion.map(lambda j: j.level)
print(f"map a niveles (list[int]): {niveles}")

resumenes = coleccion.map(lambda j: j.name + " nv." + str(j.level))
print(f"map a resumenes (list[str]): {resumenes}")

print("\n" + "=" * 55)
print("  ESCENARIO 3 — Protocol Displayable")
print("=" * 55)

jugador = Player("Jotaro",   level=9,  HP=100.0, XP=0)
mago    = Mago("Giorno",  level=8,  HP=90.0,  XP=0, mana=80, elemento="fuego")
arquero = Arquero("Noriaki", level=5,  HP=95.0,  XP=0, flechas=15, velocidad=10)

print("Llamando display() en cada tipo:")
print(jugador.display())
print(mago.display())
print(arquero.display())

coleccion_d: TypedCollection[Displayable] = TypedCollection()
coleccion_d.add(jugador)
coleccion_d.add(mago)
coleccion_d.add(arquero)

print("\nColeccion Displayable — display() para todos:")
for obj in coleccion_d:
    print(f"  {obj.display()}")

textos = coleccion_d.map(lambda obj: obj.display())
print("\nmap(display) devuelve list[str]:")
for t in textos:
    print(f"  {t}")

print("\n" + "=" * 55)
print("  ESCENARIO 4 — Protocol Scorable")
print("=" * 55)

coleccion_s: TypedCollection[Scorable] = TypedCollection()
coleccion_s.add(Player("Izuku", level=7, HP=100.0, XP=50))
coleccion_s.add(Mago("Bakugo",  level=9, HP=70.0,  XP=0, mana=200, elemento="fuego"))
coleccion_s.add(Arquero("All For One", level=5, HP=95.0,  XP=0, flechas=20, velocidad=12))

print("score() de cada jugador:")
for obj in coleccion_s:
    print(f"  score = {obj.score()}")

puntajes = coleccion_s.map(lambda obj: obj.score())
print(f"\nmap(score) devuelve list[float]: {puntajes}")

mayor = coleccion_s.find(lambda obj: obj.score() == max(puntajes))
print(f"\nJugador con mayor puntaje: {mayor.name} — score {mayor.score()}")

buenos = coleccion_s.filter(lambda obj: obj.score() >= 700)
print(f"\nfilter(score >= 700) — {len(buenos)} jugadores:")
for obj in buenos:
    print(f"  score = {obj.score()}")