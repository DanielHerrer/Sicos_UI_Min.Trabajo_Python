i = 0
while (i < 5):
    print(i)
    i+=1






# Mostrar la lista por pantalla.

lista_con_numeros_enteros = []
numero_entero = int(input("Ingrese un numero entero, cero para finalizar: "))
while (numero_entero != 0):
    lista_con_numeros_enteros.append(numero_entero)
    numero_entero = int(input("Ingrese un numero entero, cero para finalizar: "))

print(lista_con_numeros_enteros)
