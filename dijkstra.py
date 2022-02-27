import random
bandera = []

# funcion que crea aleatoriamente la bandera ,con R siendo rojo, A azul y V verde.
def crear_bandera():
    repe = random.randint(10, 20)
    for i in range(repe):
        num = random.randint(1, 3)
        if num == 1:
            bandera.append("R")
        elif num == 2:
            bandera.append("V")
        elif num == 3:
            bandera.append("A")
    return bandera

#funcion que ordena los colores de la bandera
def ordenar_colores(tamaño, indice, contador):
    if contador < tamaño:
        if bandera[indice] == "R":
            rojo = bandera.pop(indice)
            bandera.insert(0, rojo)
            ordenar_colores(tamaño, indice + 1, contador + 1)
        elif bandera[indice] == "A":
            azul = bandera.pop(indice)
            bandera.insert(len(bandera), azul)
            ordenar_colores(tamaño, indice, contador + 1)
        else:
            ordenar_colores(tamaño, indice + 1, contador + 1)
    else:
        return bandera
        
# aqui empieza el codigo principal
bandera = crear_bandera()
print(bandera)
ordenar_colores(len(bandera), 0, 0)
print(bandera)