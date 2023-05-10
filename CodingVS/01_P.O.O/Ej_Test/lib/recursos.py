# Ejercicio: Definir una clase que se encargue de hacer las 4 operaciones matematicas
#   y retorne los resultados de estas operaciones.

class OperacionesMatematicas(object):

    def suma(self,num1,num2): # self= las funciones declaradas DENTRO de una clase deben llevar self como parametro
        return num1 + num2
    
    def resta(self,num1,num2):
        return num1 - num2
    
    def division(self,num1,num2):
        return num1 / num2
    
    def multiplicacion(self,num1,num2):
        return num1 * num2



