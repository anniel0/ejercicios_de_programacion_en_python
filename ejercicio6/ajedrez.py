
with open("tablero.txt","r") as archivo:
    tab = []
    for linea in archivo:
        linea = linea.strip()
        tab.append(linea)
    
def posicion_pieza(tablero):
    for i in range(0,len(tablero)):
        for j in range(0,len(tablero[0])):
            if tablero[i][j] == 'C' or tablero[i][j] == 'T':
                return (i,j,tablero[i][j])

posicion = posicion_pieza(tab)

def modificar_tablero(pos): 
    tablero = []
    for i in range(0,len(tab)):
        columna = ''
        for j in range(0,len(tab[0])):
            if i == pos[0]-1 and j == pos[1]-1:
                columna += pos[2]
            else:
                columna += '*'
        tablero.append(columna)
  
    return tablero      

def escribir_tablero(tablero):
    salida = open("tableroS.txt","w")    

    for i in range(0,len(tablero)):
        lineas = tablero[i] + '\n'
        salida.write(lineas)

    salida.close()       

def mostrar_posibles_movimientos(pos):
    if pos[2] == 'C':
        movX = [-2,-2,-1,1]
        movY = [1,-1,2,2,]
        for i in range(0,4):
            x = pos[0] + 1 + movX[i]
            y = pos[1] + 1 + movY[i]
            if x >= 1 and x <= 6 and y >= 1 and y <= 6:
                print(f'({x},{y})\n')
    elif pos[2] == 'T':
        for i in range(-4,5):
            if pos[0] + i + 1 >= 1 and pos[0] + i + 1 <= 6 and i != 0:
                print(f'({pos[0] + i + 1},{pos[1] + 1})')
            elif pos[1] + i + 1 >= 1 and pos[1] + i + 1 <= 6 and i != 0:
                print(f'({pos[0] + 1},{pos[1] + i + 1})')

mostrar_posibles_movimientos(posicion)
nuevoX = int(input("ingresa un numero(1,6):"))
nuevoY = int(input("ingresa un numero(1,6):"))

nuevos = (nuevoX,nuevoY,posicion[2])

tab = modificar_tablero(nuevos)

escribir_tablero(tab)


