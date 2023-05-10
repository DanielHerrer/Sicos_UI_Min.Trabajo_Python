# Ejercicio: Mostrar al usuario un menú con tres opciones: 
# 1. Ingreso de números pares
# 2. Ingreso de números impares
# 3. Salir

# Los números pares se alojarán en una lista y los impares en otra. 
# Cuando el usurio elije la opción 3 (Salir), se le debe indicar si cometió algún error en
# el ingreso de datos. Se considera un error, que haya algún impar dentro de la lista de pares
# o un par dentro de la lista de impares. 


lista_con_pares = []
lista_con_impares = []
menu = 10
while(menu != 3): 
    print("1. Ingreso de números pares")
    print("2. Ingreso de números impares")
    print("3. Salir")
    menu = int(input("Ingrese una opción válida: "))
    if menu == 1: 
        numero = int(input("Ingrese un número par: "))
        lista_con_pares.append(numero)
    elif menu == 2: 
        numero = int(input("Ingrese un número impar: "))
        lista_con_impares.append(numero)


todos_pares = True
for valor in lista_con_pares: 
    if valor%2 != 0: 
        todos_pares = False


todos_impares = True
for valor in lista_con_impares: 
    if valor%2 == 0: 
        todos_impares = False


# Respuesta al usuario de la app: 

if todos_pares == False or todos_impares == False: 
    print("Los datos son incorrectos!")
else: 
    print("Los datos son correctos!")