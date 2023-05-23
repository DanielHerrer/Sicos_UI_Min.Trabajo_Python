import tkinter as tk

def obtener_valor():
    texto = entrada.get()
    print("El valor ingresado es:", texto)

ventana = tk.Tk()

#que podria agregarse para mejorar la interfaz en cuanto a dimesiones?

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Obtener Valor", command=obtener_valor)
boton.pack()

ventana.mainloop()
