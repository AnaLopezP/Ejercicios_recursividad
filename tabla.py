
clientes = [["Pepa", "25012", "25"], ["Lucio", "28400", "48"], ["Maria", "45009", "16"], ["Cristopher", "33006","24"], ["Felix", "28010", "43"], ["Noemi", "45200", "18"], ["Miriam", "36066", "36"]]
persona = []

#funcion que mira que clientes son de Toledo por su codigo postal
def clientes_toledo(tabla, n ,cod_postal):
    if 0 <= n < len(tabla):
        if tabla[n][1].startwith(cod_postal):
            persona.append(tabla[n][0])
            clientes_toledo(tabla, n + 1, cod_postal)
        else:
            clientes_toledo(tabla, n + 1, cod_postal)
        return persona

