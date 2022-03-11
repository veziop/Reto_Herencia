class Entregable:

    def __init__(self, titulo, numero, genero, autor):
        self.set_titulo(titulo)
        self.set_genero(genero)
        self.numero = numero
        self.autor = autor

    # Metodos Get
    def get_titulo(self):
        return self.titulo

    def get_genero(self):
        return self.genero

    # Metodos Set
    def set_titulo(self, titulo):
        self.titulo = titulo.title()

    def set_genero(self, genero):
        self.genero = genero

    # Dunder str()
    def __str__(self):
        return f"\"{self.titulo}\" de {self.autor}"
