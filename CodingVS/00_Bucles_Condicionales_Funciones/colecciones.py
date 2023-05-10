# Colecciones (Listas, Tuplas y Diccionarios)

# LISTAS: -------------------------------------------------------
# Las listas son una colección ordenada y mutable de elementos. 
# Se pueden agregar, eliminar o modificar elementos de la lista. Se definen con corchetes [ ].

lista_1 = [10, 20, 30, True, False, True, "Hoy es miércoles", 2.71]

print(lista_1[3])

print(lista_1[2:5])

print(lista_1[2:])

lista_1[2] = 300    # Modificar un elemento de la lista

print(lista_1)

lista_1.remove(2.71)    # Eliminar un elemento de la lista

print(lista_1)

lista_1.remove(True)

print(lista_1)

lista_1.append(3.14)    # Agregar un elemento al final de la lista

print(lista_1)

lista_1.insert(2, "Mañana es jueves")   # Agregar un elemento en cualquier posición de la lista

print(lista_1)

print(lista_1.count(2.71))

print(lista_1.count("Mañana es jueves"))

# TUPLAS (SOLO LECTURA): ----------------------------------------------------------------
# Las tuplas son una colección ordenada e inmutable de elementos. 
# No se pueden agregar ni modificar elementos de una tupla después de su creación. Se definen con paréntesis ( ).
# Las tuplas son objetos de "SOLO LECTURA". Una vez definidas, no se pueden modificar de ninguna manera 
# (no podemos modificar elementos, no podemos eliminar ni agregar elementos)

tupla_1 = (10, 20, 30, True, False, True, "Hoy es miércoles", 2.71)

print(tupla_1)

print(tupla_1[4])   # Los procedimientos de acceso a los elementos de una tupla son idénticos a los estudiados para las listas 

lista_2 = []

# DICCIONARIOS: ------------------------------------------------------------------
# Los diccionarios son una colección de elementos no ordenados y mutables
# que se acceden a través de una clave en lugar de un índice numérico. 
# Se pueden agregar, eliminar o modificar elementos del diccionario. 
# Se definen con llaves { } y cada elemento se define como un par clave-valor separado por dos puntos (:).

diccionario_1 = {"green": "verde", "red": "rojo", "blue": "azul"}

print(diccionario_1)

print(diccionario_1["red"]) # Acceso a información por clave (no por índice o posición)

diccionario_1["green"] = "VERDE"    # Modificar un valor del diccionario

print(diccionario_1)

diccionario_1["white"] = "Blanco"   # Agregar un elemento al diccionario (usando una clave nueva)

print(diccionario_1)

diccionario_2 = {1:"uno", 2:"dos", 3:"tres", "valor2": True, "Cuatro": 4.0, 4: True, 5: True}

print(diccionario_2) # Mostrar el diccionario

print(diccionario_2[3]) # Forzar la llave para acceder al valor = "tres"

print(diccionario_2.get("Cuatro")) # Acceso a un valor del diccionario con la llave = 4.0

print(diccionario_2.popitem())  # .popitem() Elimina el último elemento del diccionario

print(diccionario_2)

print(diccionario_2.pop(3)) # .pop(llave) Elimina el elemento en la llave indicada del diccionario

print(diccionario_2)