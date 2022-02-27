
clientes = [["Pepa", "25012", "25"], ["Lucio", "33006", "24"], ["Miriam", "45009", "16"], ["Cristopher", "28400","48"], ["Felix", "28010", "43"], ["Noemi", "45200", "18"], ["Maria", "36066", "36"]]
persona = []

#funcion que mira que clientes son de Toledo por su codigo postal
def clientes_cod(tabla, nombre ,cod_postal):
    if 0 <= nombre < len(tabla):
        if cod_postal in tabla[nombre][1]:
            persona.append(tabla[nombre][0])
            clientes_toledo(tabla, nombre + 1, cod_postal)
        else:
            clientes_toledo(tabla, nombre + 1, cod_postal)
        return persona

#funcion que mira que clientes entre los 40 y los 50 años son de Madrid
def clientes_cod_edad(tabla, nombre, cod_postal, edad_i, edad_f):
     if 0 <= nombre < len(tabla):
        if cod_postal in tabla[nombre][1]:
            if edad_i <= tabla[nombre][2] <= edad_f:
                persona.append(tabla[nombre][0])
                clientes_madrid(tabla, nombre + 1, cod_postal, edad_i, edad_f)
        else:
            clientes_madrid(tabla, nombre + 1, cod_postal, edad_i, edad_f)
        return persona

#codigo principal
clientes_toledo(clientes, 0, "45")
print(persona)
persona = []
clientes_madrid(clientes, 0, "28", "40", "50")
print(persona)