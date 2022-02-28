class Serie:
    titulo = 'titulo serie'
    numero_temporadas = 3
    entregado = False
    genero = 'genero serie'
    creador = 'creador serie'

    def __init__(self, titulo, numero_temporadas, genero, creador):
        self.set_titulo(titulo)
        self.set_numero_temporadas(numero_temporadas)
        self.set_genero(genero)
        self.set_creador(creador)

    # Metodos Get
    def get_titulo(self):
        return self.titulo

    def get_numero_temporadas(self):
        return self.numero_temporadas

    def get_genero(self):
        return self.genero

    def get_creador(self):
        return self.creador

    # Metodos Set
    def set_titulo(self, titulo):
        self.titulo = titulo.title()

    def set_numero_temporadas(self, numero):
        self.numero_temporadas = numero

    def set_genero(self, genero):
        self.genero = genero

    def set_creador(self, creador):
        self.creador = creador.title()

    # Dunder str()
    def __str__(self):
        return f"\"{self.titulo}\" de {self.creador}"


# noinspection NonAsciiCharacters
class Videojuego:
    titulo = 'titulo videojuego'
    horas_estimadas = 10
    entregado = False
    genero = 'genero videojuego'
    compañia = 'compañia videojuego'

    def __init__(self, titulo, horas, genero, compañia):
        self.set_titulo(titulo)
        self.set_horas_estimadas(horas)
        self.set_genero(genero)
        self.set_creador(compañia)

    # Metodos Get
    def get_titulo(self):
        return self.titulo

    def get_horas_estimadas(self):
        return self.horas_estimadas

    def get_genero(self):
        return self.genero

    def get_compañia(self):
        return self.compañia

    # Metodos Set
    def set_titulo(self, titulo):
        self.titulo = titulo.title()

    def set_horas_estimadas(self, horas):
        self.horas_estimadas = horas

    def set_genero(self, genero):
        self.genero = genero

    def set_creador(self, compañia):
        self.compañia = compañia.title()

    # Dunder str()
    def __str__(self):
        return f"\"{self.titulo}\" de {self.compañia}"


class Entregable:

    def entregar(self, esto):
        esto.entregado = True

    def devolver(self, esto):
        esto.entregado = False

    def isEntregado(self, esto):
        return esto.entregado

    def compareTo(self, obj, a):
        if isinstance(obj, Serie):
            return obj.get_numero_temporadas() > a.get_numero_temporadas()
        elif isinstance(obj, Videojuego):
            return obj.get_horas_estimadas() > a.get_horas_estimadas()
