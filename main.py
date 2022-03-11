# Reto Herencia

from interfaz import Interfaz
from serie import Serie
from videojuego import Videojuego
from random import randint


if __name__ == "__main__":

    lista_series = [
        Serie('Las Aventuras de Juanjo', 2, 'Aventura', 'Juan Zeta'),
        Serie('Cien', 3, 'Terror', 'Hans Fhurt'),
        Serie('Cremallera Solar', 5, 'Accion', 'Emilio Esteban'),
        Serie('Quiero llamarte Dorothy', 1, 'Comedia', 'Sebastian Yu'),
        Serie('Kilogramos', 6, 'Accion', 'Ramiro Peralta Martinez'),
    ]

    lista_videojuegos = [
        Videojuego('Killstreak', 10, 'FPS', 'Artes Electronicas'),
        Videojuego('Krashing Coco', 28, 'Karts', 'Yeti Inc'),
        Videojuego('Rush B', 12, 'FPS', 'Blyat Entertainment'),
        Videojuego('Juju Gems', 20, 'Mobile', 'Metagames'),
        Videojuego('Plush\'em all!', 18, 'Arcade', 'Loom Studios'),
    ]

    interfaz = Interfaz()

    for item in lista_series + lista_videojuegos:
        chance = randint(0,1)
        if chance:
            interfaz.entregar(item)

    count = 0
    for item in lista_series + lista_videojuegos:
        if interfaz.isEntregado(item):
            count += 1
            print(f"{item} está entregado.")

    print(f"Hay {count} productos entregados.")

    for index, serie in enumerate(lista_series):
        if index == 0:
            max_temporadas = serie
            continue
        if interfaz.compareTo(serie, max_temporadas):
            max_temporadas = serie

    print(f"\nLa serie con más temporadas es {max_temporadas} con {max_temporadas.get_numero_temporadas()} temporadas.")

    for index, juego in enumerate(lista_videojuegos):
        if index == 0:
            max_horas = juego
            continue
        if interfaz.compareTo(juego, max_horas):
            max_horas = juego

    print(f"El videojuego con el tiempo mayor completación es {max_horas} con {max_horas.get_horas_estimadas()} horas.")
