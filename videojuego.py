from entregable import Entregable

# noinspection NonAsciiCharacters
class Videojuego(Entregable):
    titulo = ''
    horas_estimadas = 10
    entregado = False
    genero = ''
    compañia = ''

    def __init__(self, titulo, numero, genero, autor):
        super().__init__(titulo, numero, genero, autor)
        self.set_compañia()
        self.set_horas_estimadas()

    def get_horas_estimadas(self):
        return self.horas_estimadas

    def get_compañia(self):
        return self.compañia

    def set_horas_estimadas(self):
        self.horas_estimadas = self.numero

    def set_compañia(self):
        self.compañia = self.autor
