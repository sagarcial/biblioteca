# sede.py

class Sede:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None

    def alquilar_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            self.libros.remove(libro)
            return libro
        return None
