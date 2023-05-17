from lib.Persona import Persona as p

persona_1 = p("Luis",18)

print(persona_1.nombre)

nombre = str(input("Ingrese nuevo nombre"))

persona_1.cambiarNombreSi(nombre)