# 1. Escribe un programa que sume todos los elementos de una 
#      lista excepto el ultimo número y muestre el resultado en consola.

lista = [9,8,6,7]
print("La lista: "+str(lista))

suma = 0
for num in lista[1:]:
    suma += num

print("La suma es = "+str(suma))