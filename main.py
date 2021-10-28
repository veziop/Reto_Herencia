# Reto Herencia

class Serie:
    titulo = ''
    numero_temporadas = 3
    entregado = False
    genero = ''
    creador = ''

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
        self.titulo = titulo

    def set_numero_temporadas(self, numero):
        self.numero_temporadas = numero

    def set_genero(self, genero):
        self.genero = genero

    def set_creador(self, creador):
        self.creador = creador

    # Dunder str()
    def __str__(self):
        return f"{self.titulo.title()} es una serie de {self.creador.title()}"


if __name__ == "__main__":
    serie1 = Serie('mr Robot', 4,genero="Drama", creador="sam esmail")

    print(serie1)