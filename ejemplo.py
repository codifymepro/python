def genMatriz(valor, valor2):
        print("Aqui inicia la matriz, indique datos: ")
        global datos
        datos = []
        for i in range(1, valor2 + 1, 1):
            fila = []
            for x in range(0, valor, 1):
                dato = int(input("[" + str(x + 1) + "]"+ "[" + str(i) + "]" + " = " ))
                fila.append(dato)
            datos.append(fila)
        print(" ")   
        for z in range(valor2):
            for w in range(valor):

                print("[" + str(datos [z][w]) + "]" , end = " ")
            print()
def ubicar(x,y):
     print("Los datos que seleccionaste son: ")
     print([x][y])
while True:
    texto = input("Que desea hacer? ")
    
    if texto == "matriz":
        valor = int(input("Ingrese cuantas columnas: "))
        valor2 = int(input("Ingrese cuantas filas: "))
        genMatriz(valor, valor2)
        #break
    elif texto == "ubicar":
        x = int(input("Ingrese fila "))
        y = int(input("Ingrese columna "))
        print("El valor seleccionado es: " + str(datos[y-1][x-1]), end="\n")
    else: break

    