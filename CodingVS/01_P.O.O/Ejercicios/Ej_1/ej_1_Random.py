# Clase 11
# Ejercicio 1
# Crear una clase con una funcion que retorne un
# numero aleatorio entre 1 y otro numero.
# Este otro numero debe ser aportado por el usuario
# de la aplicacion, por teclado. Imprimir el 
# valor aleatorio generado por la funcion.

# import random

# numero_Aleatorio = random.randInt(1,200)
import random as r

class Aleatorio(object):

    def numAleatorio(self, hasta):
        
        numero_Aleatorio = r.randint(1,hasta) 
        return numero_Aleatorio    