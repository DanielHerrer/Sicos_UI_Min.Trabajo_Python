from ej_1_Random import Aleatorio as aleat

a = aleat()

print("Bienvenido! Numeros aleatorios desde 1 hasta X !!!")
numero_entero = int(input("Ingrese un numero entero, '0' para finalizar: "))
while(numero_entero!=0):
    print(a.numAleatorio(numero_entero))
    numero_entero = int(input("Ingrese un numero entero, '0' para finalizar: "))
if(numero_entero==0):
    print("Finalizando..")
