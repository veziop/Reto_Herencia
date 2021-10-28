# Reto Herencia



if __name__ == "__main__":
    serie1 = Serie('mr Robot', genero="Drama", creador="sam esmail")

    print(serie1)
    print(f"La serie {serie1.get_titulo()} tiene {serie1.get_numero_temporadas()} temporadas")

    juego1 = Videojuego('Red Dead Redemption', 'Accion', 'rockstar games')
    print(juego1)