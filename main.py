import string;

acentos = ["á", "é", "í", "ó", "ú"]
sinacentos = [ "a", "e", "i", "o", "u"]


#la frase que vamos a analizar
frase = input()

def hazcadena (lista, cadena):
    if (len(lista)) != 0:
        car = lista.pop()
        cadena = hazcadena(lista,cadena)
        car = car.lower()
        if car != " ":
            cadena = cadena + car
    return cadena;


#definicion de las funciones que necesitamos
def quitar_espacios(frase):
    frase_tabla = list(frase)
    cadena = ""
    cadena = hazcadena(frase_tabla, cadena)
    print(cadena)
    
    return cadena


#def sustituir_acentos(frase)

#def todo_mayus(frase)



quitar_espacios(frase)

#cadena = hazCadena(lista)



