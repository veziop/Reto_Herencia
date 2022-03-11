from entregable import Entregable


class Serie(Entregable):
    titulo = ''
    numero_temporadas = 3
    entregado = False
    genero = ''
    creador = ''

    def __init__(self, titulo, numero, genero, autor):
        super().__init__(titulo, numero, genero, autor)
        self.set_creador()
        self.set_numero_temporadas()

    def get_numero_temporadas(self):
        return self.numero_temporadas

    def get_creador(self):
        return self.creador

    def set_numero_temporadas(self):
        self.numero_temporadas = self.numero

    def set_creador(self):
        self.creador = self.autor
