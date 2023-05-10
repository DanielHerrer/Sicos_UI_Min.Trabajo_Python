# Estructuras condicionales

temperatura = int(input("Ingrese la temperatura actual: "))

if (temperatura<10):
    print("Hoy es un dia frio")
elif (temperatura>=10 and temperatura<=20):
    print("Hoy es un dia templado")
elif (temperatura>=20):
    print("Hoy es un dia caluroso")

print("Fuera del condicional...")