def por_nombre(jugador):
    return jugador.name

def por_nivel(jugador):
    return jugador.level

def por_hp(jugador):
    return jugador.HP

def por_nivel_y_nombre(jugador):
    return (jugador.level, jugador.name)

def es_activo(jugador):
    if jugador.status == "активный":
        return True
    else:
        return False

def es_nivel_alto(jugador):
    if jugador.level >= 5:
        return True
    else:
        return False

def a_resumen(jugador):
    return jugador.name + " (nv." + str(jugador.level) + " | HP:" + str(jugador.HP) + ")"

def a_nombre(jugador):
    return jugador.name

def hacer_filtro_nivel(nivel_minimo):
    def filtro(jugador):
        if jugador.level >= nivel_minimo:
            return True
        else:
            return False
    return filtro

def hacer_filtro_hp(hp_minimo):
    def filtro(jugador):
        if jugador.HP >= hp_minimo:
            return True
        else:
            return False
    return filtro

class EstrategiaOrdenarPorNivel:
    def __call__(self, jugador):
        return jugador.level

class EstrategiaOrdenarPorHP:
    def __call__(self, jugador):
        return jugador.HP

class EstrategiaOrdenarPorNombre:
    def __call__(self, jugador):
        return jugador.name