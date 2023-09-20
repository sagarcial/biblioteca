# biblioteca.py

class Biblioteca:
    def __init__(self):
        self.sedes = []

    def agregar_sede(self, sede):
        self.sedes.append(sede)

    def buscar_libro(self, titulo):
        for sede in self.sedes:
            libro = sede.buscar_libro(titulo)
            if libro:
                return libro
        return None
