import numpy as np # modulo utilizado numpy

# Estructura de la imagen
class imagen:
    def __init__(self):
        self.tipo = ""
        self.profundidad = 0
        self.altura = 0
        self.anchura = 0
        self.pixeles = np.zeros((8192, 8192, 3), dtype=int)

# lectura del archivo
def lectura_archivo(imagenOriginal : imagen):
    try:
        with open("personaje.ppm","r") as archivo:
            imagenOriginal.tipo = archivo.readline().strip()
            imagenOriginal.altura,imagenOriginal.anchura = map(int,archivo.readline().strip().split())
            imagenOriginal.profundidad = int(archivo.readline().strip())

            todos_los_valores = []
            for linea in archivo:
                valores = linea.split()
                todos_los_valores.extend(map(int, valores))
            
            index = 0
            for i in range(imagenOriginal.altura):
                for j in range(imagenOriginal.anchura):
                    if index + 2 < len(todos_los_valores):
                        r,g,b =  todos_los_valores[index],todos_los_valores[index + 1],todos_los_valores[index + 2]
                        imagenOriginal.pixeles[i,j] = [r, g, b]
                        index += 3

    except FileExistsError:
        print()
        return

# salida de archivo
def salida_archivo(imagenfinal : imagen) -> None:
    with open("personaje-modificado.ppm","w") as archivo:
        archivo.write(f'{imagenfinal.tipo}\n')
        archivo.write(f'{imagenfinal.altura} {imagenfinal.anchura}\n')
        archivo.write(f'{imagenfinal.profundidad}\n')

        for i in range(imagenfinal.altura):
            for j in range(imagenfinal.anchura):
                r,g,b = imagenfinal.pixeles[i,j]
                archivo.write(f'{r} {g} {b} ')
            archivo.write('\n')

# inversa de la imagen 
def espejo_imagen(imagenOriginal: imagen) -> imagen:
    
    imagen_final = imagen()
    
    imagen_final.altura = imagenOriginal.altura 
    imagen_final.anchura = imagenOriginal.anchura
    imagen_final.tipo = imagenOriginal.tipo
    imagen_final.profundidad = imagenOriginal.profundidad
    
    for i in range(imagenOriginal.altura):
        for j in range(imagenOriginal.anchura):
            imagen_final.pixeles[i][j] = imagenOriginal.pixeles[i][imagenOriginal.anchura-j-1]
    
    return imagen_final

# declaracion de la funcion base
def main() -> None:
    imagenOrigil = imagen()
    # lectura de la imagen
    lectura_archivo(imagenOrigil)
    # imagen de salida
    imagenfinal = espejo_imagen(imagenOrigil)
    # imagen de salida
    salida_archivo(imagenfinal)

if __name__ == "__main__":
    main()


