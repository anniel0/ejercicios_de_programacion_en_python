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

# lectura de valor de escalado
def valor_escalado() -> int:
    try:
        with open("escalado.conf","r") as archivo:
            return int(archivo.readline().strip().split()[0])
    except FileExistsError:
        return

# modificacion del archivo
def modificar_imagen(num : int,imagenOriginal : imagen) -> imagen:
    imagenfinal = imagen()
    imagenfinal.tipo = imagenOriginal.tipo
    if num < 1 or num > 8192:
        num = 1

    imagenfinal.altura = imagenOriginal.altura * num
    imagenfinal.anchura = imagenOriginal.anchura * num
    imagenfinal.profundidad = imagenOriginal.profundidad
    for i in range(imagenOriginal .altura):
        for j in range(imagenOriginal .anchura):
            inicio_fil = i * num
            inicio_col = j * num
            for di in range(num):
                for dj in range(num):
                    if (inicio_fil + di < 8192 and inicio_col + dj < 8192):
                        imagenfinal.pixeles[inicio_fil + di][inicio_col + dj] = imagenOriginal .pixeles[i][j]

    return imagenfinal

# rotacion de imagen 90º
def rotar_imagen_90_grados(imagenOriginal: imagen) -> imagen:
    
    imagen_final = imagen()
    
    imagen_final.altura = imagenOriginal.anchura
    imagen_final.anchura = imagenOriginal.altura
    imagen_final.tipo = imagenOriginal.tipo
    imagen_final.profundidad = imagenOriginal.profundidad
    
    for i in range(imagenOriginal.altura):
        for j in range(imagenOriginal.anchura):
            # Fórmula correcta para rotación 90° horario
            nueva_fila = j
            nueva_columna = imagenOriginal.altura - i - 1
            imagen_final.pixeles[nueva_fila][nueva_columna] = imagenOriginal.pixeles[i][j]
    
    return imagen_final

# declaracion de la funcion base
def main() -> None:
    imagenOrigil = imagen()
    # lectura de la imagen
    lectura_archivo(imagenOrigil)
    # imagen de salida
    imagenfinal = rotar_imagen_90_grados(imagenOrigil)
    # imagen de salida
    salida_archivo(imagenfinal)

if __name__ == "__main__":
    main()


