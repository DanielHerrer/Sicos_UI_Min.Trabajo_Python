# Daniel Franco Herrera (SIN TERMINAR)

import tkinter as tk

ventana = tk.Tk()   # Se crea la ventana
ventana.title("Reloj y Temporizador")

def sumar():
    rSuma = num1 + num2
    return rSuma

def restar():
    return num1 - num2

def multiplicar():
    return num1 * num2

def dividir():
    return num1 / num2

formula = tk.Label(ventana, font=("Arial", 12))
formula.grid(row=1,column=1)

titulo_calc = tk.Entry(ventana, font=("Arial", 24))
titulo_calc.grid(row=1,column=1)

boton_1 = tk.Button(ventana, text="1", command=1)
boton_1.grid(row=2,column=1)
boton_2 = tk.Button(ventana, text="2", command=2)
boton_2.grid(row=2,column=2)
boton_3 = tk.Button(ventana, text="3", command=3)
boton_3.grid(row=2,column=3)
boton_sumar = tk.Button(ventana, text="+", command=sumar())
boton_sumar.grid(row=2,column=4)

boton_4 = tk.Button(ventana, text="4", command=4)
boton_4.grid(row=3,column=1)
boton_5 = tk.Button(ventana, text="5", command=5)
boton_5.grid(row=3,column=2)
boton_6 = tk.Button(ventana, text="6", command=6)
boton_6.grid(row=3,column=3)
boton_restar = tk.Button(ventana, text="+", command=restar())
boton_restar.grid(row=3,column=4)

boton_7 = tk.Button(ventana, text="7", command=7)
boton_7.grid(row=4,column=1)
boton_8 = tk.Button(ventana, text="8", command=8)
boton_8.grid(row=4,column=2)
boton_9 = tk.Button(ventana, text="9", command=9)
boton_9.grid(row=4,column=3)
boton_multiplicar = tk.Button(ventana, text="+", command=multiplicar())
boton_multiplicar.grid(row=4,column=4)

boton_0 = tk.Button(ventana, text="0", command=0)
boton_0.grid(row=5,column=3)
boton_dividir = tk.Button(ventana, text="+", command=dividir())
boton_dividir.grid(row=4,column=4)


# boton_calcular = tk.Button(ventana, text="Calcular", command=mostrar_alerta)

ventana.mainloop()