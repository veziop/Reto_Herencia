from serie import Serie
from videojuego import Videojuego

class Interfaz:

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
