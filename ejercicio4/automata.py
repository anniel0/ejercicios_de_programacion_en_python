"""
ejercicio de programacion:

Elabore un programa llamado 02-automata.c que simule un Autómata celular bidimensional de
dos estados: “vivo” o “muerto”. Para un número entero de iteraciones, se deben (por cada
una) evaluar todas las celdas y según sus ocho vecinos adyacentes y el valor que dicha celda
contenga, actualizarla según las siguientes reglas:

    a) Se reemplaza una celda en estado muerto por vivo si tiene exactamente 3 vecinos en
    estado vivo.
    b) Se reemplaza una celda en estado vivo por muerto si no tiene más de 1 vecino en
    estado vivo o si
    c) Tiene más de 3 vecinos vivos.
    d) Una celda en estado vivo permanecerá en ese estado si tiene 2 o 3 vecinos vivos.
    e) De no ocurrir ninguna de las anteriores, el contenido de la celda en cuestión permanece
    igual.

Entrada:

La información de entrada se almacena en un archivo llamado atc.txt con la siguiente
estructura
    n
    nv
    nit

Donde n es el número de celdas por dimensión del autómata; nv < = n, es el número de celdas
en estado vivo y nit, el número de iteraciones. La posiciones de celdas en estado vivo se
escogerán inicialmente de manera aleatoria

Salida:

El programa debe leer esa información y cargarla en una estructura conveniente e imprimir en
forma matricial en el mismo archivo el contenido del autómata correspondiente a las iteraciones
1, nit/2, nit/4, 3/4nit y nit.
"""

import numpy as np

def lectura_datos() -> list:
    try:
        with open("atc.txt","r") as archivo:
            n = int(archivo.readline().strip())
            nv = int(archivo.readline().strip())
            nit = int(archivo.readline().strip())
        return [n,nv,nit]
    except FileNotFoundError:
        print("Error de lectura de archivo")
        return None
    
def inicializar(n: int, vivos: int) -> np.ndarray:
    array = np.zeros((n,n), dtype=int)

    count = 0
    while count < vivos:  
        i = np.random.randint(0, n)
        j = np.random.randint(0, n)
        if array[i,j] == 0:
            array[i,j] = 1
            count += 1
    
    return array

def contar_vecinos(array: np.ndarray, i: int, j: int) -> int:
    """Cuenta los vecinos vivos de una celda, considerando bordes toroidales"""
    n = len(array)
    vecinos = 0
    
    # Definir las 8 direcciones posibles (incluyendo diagonales)
    direcciones = [(-1,-1), (-1,0), (-1,1),
                   (0,-1),          (0,1),
                   (1,-1),  (1,0),  (1,1)]
    
    for dx, dy in direcciones:
        x = (i + dx) % n  # Usar módulo para bordes toroidales
        y = (j + dy) % n
        
        if array[x, y] == 1:
            vecinos += 1
            
    return vecinos

def modificaciones(array: np.ndarray) -> np.ndarray:
    """Aplica las reglas del Juego de la Vida"""
    n = len(array)
    nuevo_array = array.copy()  # Crear una copia para no modificar el original durante el proceso
    
    for i in range(n):
        for j in range(n):
            vecinos = contar_vecinos(array, i, j)
            
            # Aplicar reglas del Juego de la Vida
            if array[i, j] == 1:  # Celda viva
                if vecinos < 2 or vecinos > 3:
                    nuevo_array[i, j] = 0  # Muere por soledad o sobrepoblacion
                else:
                    nuevo_array[i, j] = 1  # Sobrevive
            else:  # Celda muerta
                if vecinos == 3:
                    nuevo_array[i, j] = 1  # Nace por reproduccion
    
    return nuevo_array

def escribir_array(k: int, array: np.ndarray, data: list) -> None:
    modo = "w" if k == 1 else "a"
    
    with open("atc.txt", modo) as archivo:
        if k == 1:
            archivo.write(f'{data[0]}\n{data[1]}\n{data[2]}\n')
        
        archivo.write(f"\n############################## k = {k} ##############################\n")
        
        for i in range(len(array)):
            for j in range(len(array[i])):
                if array[i, j] == 1:
                    archivo.write("# ")
                else:
                    archivo.write(". ")
            archivo.write("\n")

def simulaciones(array: np.ndarray, data: list) -> None:
    """Ejecuta las simulaciones del Juego de la Vida"""
    puntos_guardado = [1, data[2]//4, data[2]//2, 3*data[2]//4, data[2]]
    
    for k in range(1, data[2] + 1):
        if k in puntos_guardado:
            escribir_array(k, array, data)
        array = modificaciones(array)

if __name__ == "__main__":
    data = lectura_datos()
    if data is not None:
        n, nv, nit = data
        array = inicializar(n, nv)
        simulaciones(array, data)
    