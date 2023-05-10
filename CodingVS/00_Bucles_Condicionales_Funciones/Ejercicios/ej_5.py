# Ejercicio: Desarrollar una aplicacion con una funcion que reciba una lista con numeros ingresados
# por el usuario y devuelva el menor y mayor numero de esa lista (en una misma funcion)

"""
def funcionComentada(){
    return nada
}
"""

def mayor_y_menor(coleccion):
    mayor = coleccion[0]
    menor = coleccion[0]
    for i in coleccion:
        if (mayor < i):
            mayor = i
        if (menor > i):
            menor = i
    return mayor, menor

lista = [7,9,2,6,3,4,5]

mayorMenor = mayor_y_menor(lista)
print("El mayor y menor es = "+ str(mayorMenor))

mayor, menor = mayor_y_menor(lista)
print("El numero mayor es = "+ str(mayor))
print("El numero menor es = "+ str(menor))