def suma_1():    #Encabezado basico de una funcion
    resultado = 20 + 15
    print(resultado)    

suma_1() # 35

def suma_2(num1,num2):
    resultado = num1 + num2
    print(resultado)

suma_2(4,2) # 6

def suma_3(num1, num2=6):
    resultado = num1 + num2
    print(resultado)

suma_3(6) #12

def operaciones_matematicas(numero1,numero2):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2
    return suma, resta, multiplicacion, division

suma, resta, multiplicacion, division = operaciones_matematicas(5,3) # Se asigna en orden a cada variable

_ , resta , _ , _ = operaciones_matematicas(5,3) # Se asigna unicamente 'resta = 2'

resultado_tupla = operaciones_matematicas(5,3) # Si se asigna a 1 variable se genera una TUPLA (8,2,15,1.6)

print(resultado_tupla)      # (8, 2, 15, 1.6)  
print(resultado_tupla[2])   # (15)
print(resultado_tupla[-1])  # (1.6)



