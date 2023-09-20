# Crear la lista de textos
textos = [
    "El sol brilla en un cielo despejado.",
    "La vida es un viaje que debemos disfrutar.",
    "Los libros son una puerta a otros mundos.",
    "La música tiene el poder de tocar el alma.",
    "La perseverancia es la clave del éxito.",
    "El conocimiento es el camino hacia la sabiduría.",
    "La naturaleza nos regala belleza en cada estación.",
    "La amistad es un tesoro que debemos cuidar.",
    "El tiempo es nuestro recurso más valioso.",
    "La creatividad fluye en momentos de inspiración."
]

# Escribir la lista de textos en el archivo lista_libros.txt
with open('lista_libros.txt', 'w') as archivo:
    for texto in textos:
        archivo.write(texto + '\n')

print("La lista de textos se ha guardado en el archivo lista_libros.txt.")
