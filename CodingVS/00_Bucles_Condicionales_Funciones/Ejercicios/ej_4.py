# Ejercicio: Solicitar al usuario de la aplicacion el ingreso de numeros enteros 
# hasta que ingrese el numero 0. Agregar todos esos numeros a una lista (menos el 0)
# Crear una funcion que retorne la suma de todos los numeros de la lista

lista = []
num = int(input("Ingrese un numero => "))
while (num!=0):
    lista.append(num)
    num = int(input("Ingrese un numero => "))
    if (num==0):
        print("Finalizando..")

def sumaTotal(coleccion):
    numTotal = 0
    for var in lista:
        numTotal += var
    return numTotal

print(lista)
print(sumaTotal(lista))