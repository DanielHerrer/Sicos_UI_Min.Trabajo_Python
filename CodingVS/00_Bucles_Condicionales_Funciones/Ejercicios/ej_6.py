# Ejercicio: Crear una función que permita el ingreso de números enteros por parte del 
# usuario. Los valores múltiplos de 3 deben quedar dentro de una lista. Los valores múltiplos
# de 5 en otra lista. Se termina el ingreso de números con un cero. Al final la función debe 
# retornar la lista con múltiplos de 3 y la lista con múltiplos de 5. 


# Versión 1 de la app
def multiplos(numero): 
    if numero%3 == 0: # divisible por 3
        lista_multiplos_3.append(numero)
    if numero%5 == 0: # divisible por 5
        lista_multiplos_5.append(numero)
    

lista_multiplos_3 = []
lista_multiplos_5 = []
numero = int(input("Ingrese un número entero, cero para finalizar: "))
while(numero != 0): 
    multiplos(numero)
    numero = int(input("Ingrese un número entero, cero para finalizar: "))

print(lista_multiplos_3)
print(lista_multiplos_5)
# Fin versión 1



# Versión 2 de la app (Tomás)
lista = []
num_entero = int(input("Ingrese números enteros, ingrese 0 para finalizar: "))
while (num_entero!=0):
    lista.append(num_entero)
    num_entero = int(input("Ingrese números enteros, ingrese 0 para finalizar: "))
 
print(lista)

def multiplo (coleccion):
    list_mult_tres = []
    list_mult_cinco = []
    for num in coleccion:
        if num%3 == 0:
            list_mult_tres.append(num)
        if num%5 == 0: # aquí se debe usar dos if independientes (ya que el hecho de que un numero sea divisible
            # por 3 no implica necesariamente que no sea divisible también por 5)
            list_mult_cinco.append(num)
    return list_mult_tres, list_mult_cinco


print(multiplo(lista))
# Fin versión 2