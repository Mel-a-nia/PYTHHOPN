def por_nombre(jugador):
    return jugador.name

def por_nivel(jugador):
    return jugador.level

def por_hp(jugador):

    return jugador.HP

def por_nivel_y_nombre(jugador):
    return (jugador.level, jugador.name)

def es_activo(jugador):
    return jugador.status == "активный"

def es_alto_nivel(jugador):
    return jugador.level >= 5

def hacer_filtro_nivel(nivel_minimo):
    def filtro(jugador):
        return jugador.level >= nivel_minimo
    return filtro

def hacer_filtro_hp(hp_minimo):
    def filtro(jugador):
        return jugador.HP >= hp_minimo
    return filtro

def a_resumen(jugador):
    return f"{jugador.name} (Nv.{jugador.level} | HP:{jugador.HP})"

def a_nombre(jugador):
    return jugador.name


class EstrategiaOrdenarPorNivel:
    def __call__(self, jugador):
        return jugador.level


class EstrategiaOrdenarPorHP:
    def __call__(self, jugador):
        return jugador.HP


class EstrategiaOrdenarPorNombre:
    def __call__(self, jugador):
        return jugador.name