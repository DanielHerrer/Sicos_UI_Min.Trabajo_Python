# Ejercicio: Desarrollar una funcion que reciba unalista formada por letras separadas
# y devuelva un objeto String con las letras unidas

def concatenarLetras(coleccion):
    palabra_unida = ""
    for var in coleccion:
        palabra_unida += var
    return palabra_unida

lista = ["D","a","n","i","e","l"]

print(concatenarLetras(lista))