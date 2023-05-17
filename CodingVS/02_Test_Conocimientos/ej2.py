# 2. Escriba una funcion que verifique numeros impares de una lista. (Puede estar precargada).

lista_nums = [1,2,3,4,5,6,7,8,9]

def numerosImpares(lista):
    numImpares = []
    for i in lista:
        if i % 2 != 0:
            numImpares.append(i)
    return numImpares

print(lista_nums)
print(numerosImpares(lista_nums))