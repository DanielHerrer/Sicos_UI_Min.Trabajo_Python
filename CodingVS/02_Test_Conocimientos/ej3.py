# 3. Escriba un programa que ingrese por consola numeros y te devuelva si es par, impar o 0. 
#     Si ingresa mas de 1 numero por consola,guardelo en una lista y luego devuelva el largo de la lista.

def numeroX(num):
    if num == 0:
        return "Es 0"
    elif num % 2 != 0:
        return "Es impar"
    elif num % 2 == 0:
        return "Es par"

def ingresarNumeros(lista):
    num = str(input("Ingrese un numero ('salir' para finalizar): "))
    while num != "salir":
        lista.append(int(num))
        print(numeroX(int(num)))
        num = str(input("Ingrese un numero ('salir' para finalizar): "))
    return len(lista)

lista = []
print("------------------------------------------------")
print("Cantidad de elementos de la lista = "+str(ingresarNumeros(lista)))
print(lista)