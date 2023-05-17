# 5. Escriba un programa que contenga un diccionario general y en el mismo contenga
#     diccionarios de personas con nombre y apellido (Puede estar precargado desde el codigo). 
#       Recorra ese diccionario,cree una funcion que verifique si es mayor de 18 años esa persona,
#         y se agregue a una lista solo los nombres. Luego imprima por consola la lista.

def mayorDeEdad(edad):
    if edad >= 18:
        return True
    else:
        return False
    
def añadirPersonasAdultas(diccionario):
    listaNombres = []
    for clave, valor in diccionario.items():
        if mayorDeEdad(valor):
            listaNombres.append(clave)
    return listaNombres
    
diccionarioPersonas = {"Daniel Herrera":25, "Martin Ciro":19, "Lucas Perez":17, "Fernando Almibar":36, "Apolo Manes":11}

print(diccionarioPersonas)
print("Personas adultas = "+str(añadirPersonasAdultas(diccionarioPersonas)))