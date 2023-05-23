import tkinter as tk
from tkinter import messagebox

def mostrar_alerta():
    messagebox.showinfo("Alerta", "Hola mundo")

# Crear la ventana
ventana = tk.Tk()

# Configurar la ventana
ventana.title("Ejemplo de GUI")
ventana.geometry("300x200")

# Crear el botón
boton = tk.Button(ventana, text="Mostrar alerta", command=mostrar_alerta)
boton.pack(pady=50)
# Iniciar el bucle principal de la ventana
ventana.mainloop()