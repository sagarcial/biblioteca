# main.py
from biblioteca import Biblioteca
from sede import Sede
from libro import Libro

# Crear instancias de la biblioteca y sedes
biblioteca = Biblioteca()
sede1 = Sede("Sede A")
sede2 = Sede("Sede B")

# Agregar sedes a la biblioteca
biblioteca.agregar_sede(sede1)
biblioteca.agregar_sede(sede2)

# Cargar libros desde un archivo TXT
def cargar_libros_desde_txt(nombre_archivo, sede):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            datos = linea.strip().split(',')
            if len(datos) == 2:
                titulo, autor = datos
                sede.agregar_libro(Libro(titulo, autor))

# Cargar libros en las sedes desde un archivo TXT
cargar_libros_desde_txt('lista_libros.txt', sede1)
cargar_libros_desde_txt('lista_libros.txt', sede2)

# Solicitar datos del cliente
nombre_cliente = input("Ingrese su nombre: ")
carnet_cliente = input("Ingrese su número de carnet: ")

# Mostrar lista de libros disponibles
print("Lista de libros disponibles:")
for libro in sede1.libros + sede2.libros:
    print(libro)

# Permitir al cliente elegir un libro
titulo_elegido = input("Elija un libro por su título: ")

# Buscar el libro elegido en la biblioteca
libro_elegido = biblioteca.buscar_libro(titulo_elegido)

if libro_elegido:
    print(f"Libro elegido: {libro_elegido}")
    print(f"Alumno: {nombre_cliente}, Carnet: {carnet_cliente}")
    # Puedes agregar aquí la lógica para registrar el alquiler del libro y guardar los datos del alumno si lo deseas.
else:
    print(f"No se encontró el libro con el título: {titulo_elegido}")
