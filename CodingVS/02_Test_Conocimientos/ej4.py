# 4. Escriba una funcion que recorra una lista de palabras, 
#     y devuelva el largo de la primera palabra de la lista. 
#       Si es mayor a 5 letras que la borre.

def primeroEnLaLista(lista):
    print(lista)
    if len(lista[0]) > 5:
        print("La primer palabra contiene más de 5 letras, SE BORRARÁ")
        lista.remove(lista[0])
    else:
        print("La primer palabra contiene menos de 5 letras, NO SE BORRARÁ")

listaPalabras = ["mansion","perro","auto","pan","sol","computadora"]
primeroEnLaLista(listaPalabras)
print(listaPalabras)