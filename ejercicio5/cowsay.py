# lee y almacena la informacion en un lista
entrada = open("mensaje.txt","r")

guardadoText = []
for linea in entrada:
    valor = linea.strip('\n')
    guardadoText.append(valor)

entrada.close()

# longitud de tamaño maximo para el espaciado
def longitud_espaciado( lineas ) -> int:
    maximo = 0
    for linea in lineas:
        if len(linea) > maximo:
            maximo = len(linea)
    
    return maximo
# crea el archivo
def crear_archivo() -> None:
    salida = open("salida.txt","w")

    for i in range(1,3):
        for j in range(1,longitud_espaciado(guardadoText)+4):
            if i == 1:
                salida.write("*")
            elif i > 1 and (j == 1 or j == longitud_espaciado(guardadoText) + 3 ):
                salida.write("*")
            else:
                salida.write(" ")
            
            if j == longitud_espaciado(guardadoText)+3:
                salida.write("\n")

    salida.close()  
# añade el mensaje
def añadir_mensaje() -> None:
    salida = open("salida.txt","a")

    for linea in guardadoText:
        n = len(linea) 
        linea = "*"  + linea
        for i in range(1,longitud_espaciado(guardadoText)-n + 2):
            linea += ' '
        linea += '*\n'
        salida.write(linea)

    salida.close()
# cierra el archivo
def cerrar_archivo() -> None:
    salida = open("salida.txt","a")

    for i in range(1,3):
        for j in range(1,longitud_espaciado(guardadoText)+4):
            if i == 2:
                salida.write("*")
            elif i < 2 and (j == 1 or j == longitud_espaciado(guardadoText) + 3 ):
                salida.write("*")
            else:
                salida.write(" ")
            
            if j == longitud_espaciado(guardadoText)+3:
                salida.write("\n")

    salida.write("*\n:\n^__^\n(oo)\\_______\n(__)\\\t\t)\\/\\\n\t||----w  |\n\t||\t\t||")
    salida.close()  

if __name__ == "__main__":
    # crea el archivo de salida
    crear_archivo()
    # añade el mensaje con el espaciado
    añadir_mensaje()
    # cierra el archivo con la parte final
    cerrar_archivo()

