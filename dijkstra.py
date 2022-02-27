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


# aqui empieza el codigo principal
bandera = crear_bandera()
print(bandera)