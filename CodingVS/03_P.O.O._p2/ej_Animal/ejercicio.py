class Animal:
    def __init__(self,nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass    # pass: instruccion nula

class Perro(Animal): # Polimorfismo
    def hacer_sonido(self):
        print(self.nombre+": 'Guau'")

class Gato(Animal): # Polimorfismo
    def hacer_sonido(self):
        print(self.nombre+": 'Miau'")

# Ejemplo de uso
perro1 = Perro("Firulais")
gato1 = Gato("Garfield")

perro1.hacer_sonido()
gato1.hacer_sonido()