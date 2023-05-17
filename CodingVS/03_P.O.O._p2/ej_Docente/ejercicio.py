class Persona():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

class Docente(Persona): #Herencia Simple
    def __init__(self,nombre,edad,puesto):
        super().__init__(nombre,edad)
        self.pusto = puesto

    def Status(self):
        print(self.nombre)
        print(self.edad)
        print(self.puesto)

Persona1 = Docente("Nahuel",18,"Tecnico")
Persona1.Status()