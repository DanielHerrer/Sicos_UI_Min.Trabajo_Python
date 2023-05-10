# Ejercicio: Ingresar numeros hasta ingresar "Salir". Mostrar la lista por pantalla.

lista_con_numeros = []
numero_entero = input("Ingrese un numero entero, 'Salir' para finalizar: ")
while (numero_entero != 'Salir'):
    lista_con_numeros.append(numero_entero)
    numero_entero = input("Ingrese un numero entero, 'Salir' para finalizar: ")

print(lista_con_numeros)