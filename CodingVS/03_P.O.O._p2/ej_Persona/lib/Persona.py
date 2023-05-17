class Persona:

    nombre = ""
    edad = 0

    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def self(self):
        print(self.nombre)
        print(self.edad)

    def añadirEdad(self,edad):
        self.edad += edad
    
    def cambiarNombre(self,nombre):
        self.nombre = nombre

    def cambiarNombreSi(self,nombre):
        if len(nombre) > 10:
            print("El nombre "+nombre+" contiene más de 10 letras")
            print("No se cambiará")
        else:
            print("El nombre "+nombre+" contiene menos de 10 letras")
            print("Si se cambiará")
            self.nombre = nombre