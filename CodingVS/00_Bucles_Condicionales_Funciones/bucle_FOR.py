# Dos formas de usarlo: 

# 1) Con la función range()

for i in range(10): # la variable i va de 0 a 9 (10 vueltas)
    print(i)

print("-------------------------------------------------------------------------------")

for i in range(1, 10): # la variable i va de 1 a 9 (9 vueltas)
    print(i)

print("-------------------------------------------------------------------------------")

for i in range(1, 10, 3): # la variable i tomará los valores: 1, 4, 7 (3 vueltas)
    print(i)

print("-------------------------------------------------------------------------------")

numero = 9
for i in range(10): 
    print(numero - i)

# Ejercicio 1: utilizando un bucle for con range(), crear una lista con los 
# números pares entre 2 y 100

print("-------------------------------------------------------------------------------")


lista_con_pares = []
for i in range(2, 101, 2): # i -> 2, 4, 6, ........, 100
    lista_con_pares.append(i)

print(lista_con_pares)


print("-------------------------------------------------------------------------------")

lista_con_pares_2 = []
for i in range(1, 51): 
    lista_con_pares_2.append(i*2)

print(lista_con_pares_2)

print("-------------------------------------------------------------------------------")

lista_con_pares_3 = []
for i in range(50): 
    lista_con_pares_3.append((i + 1)*2)

print(lista_con_pares_3)

print("-------------------------------------------------------------------------------")

# 2) Sin la función range, actuando directamente sobre una colección

for valor in lista_con_pares_3: # no utiliza la función range(), i se va cargando con cada uno
    # de los valores de la lista, del primero al último
    print(valor)


# Ejercicio 2: utilizando el bucle for sin range() sobre la lista "lista_con_valores_3", 
# cargar un diccionario que tenga el siguiente aspecto: 
# diccionario_1 = {2: "2", 4: "4", 6: "6", ............ 100: "100"}

diccionario_con_pares = {}
for i in range(50):       
      diccionario_con_pares[i*2] = str(i*2)
print(diccionario_con_pares)