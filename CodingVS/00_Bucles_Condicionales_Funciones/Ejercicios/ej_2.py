# Ejercicio: Desarrollar una aplicacion que tenga una funcion que reciba una
# lista cualquiera con cuatro numeros y debe retornar otra lista con los numeros de
# la primera, multiplicados por 3

def multiplicar_x3(num):
    num *= 3
    return num

def lista_x3(lista):
    listax3 = []
    for num in lista:
        listax3.append(multiplicar_x3(num))
    return listax3

lista = [3,5,2]

print(lista_x3(lista))  # [9, 15, 6]