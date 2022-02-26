import string;

#la frase que vamos a analizar
frase = input()

#esta funcion quita todos los espacios, pasa todas las letras a minusculas y quita los acentos
def hazcadena (lista, cadena):
    if (len(lista)) != 0:
        car = lista.pop()
        cadena = hazcadena(lista,cadena)
        car = car.lower()
        if car != " ":
            cadena = cadena + sustituir_acentos(car)
    return cadena

#esta es la funcion que quita los acentos, que se usa en la funcion de arriba
def sustituir_acentos(car):
    if (car == "á"):
        return "a"
    elif (car == "é"):
        return "e"
    elif (car == "í"):
        return "i"
    elif (car == "ó"):
        return "o"
    elif (car == "ú"):
        return "u"
    else: 
        return car


#esta es la funcion principal que prepara la frase inicial para analizar
def preparar_frase(frase):
    frase_tabla = list(frase)
    cadena = ""
    cadena = hazcadena(frase_tabla, cadena)
    return cadena

#esta es una funcion que invierte la cadena
def invertir_cadena(frase):
    frase_lista = list(frase)
    cadena_invertida = ""
    while len(frase_lista) != 0:
        car = frase_lista.pop()
        cadena_invertida = cadena_invertida + car
    print(cadena_invertida)
    return cadena_invertida

#esta es la funcion que analiza que la frase sea polindroma
def es_polindromo(frase, frase_invertida):
    if frase == frase_invertida:
        return True
    else:
        return False

    
    
#codigo principal

frase = preparar_frase(frase)
frase_invertida = invertir_cadena(frase)
if es_polindromo(frase, frase_invertida) == True:
    print("Esta frase es polindroma")
else:
    print("esta frase no es polindroma")