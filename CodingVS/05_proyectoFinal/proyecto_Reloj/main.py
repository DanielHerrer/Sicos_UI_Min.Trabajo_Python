# Daniel Franco Herrera

import time
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def mostrar_alerta():
    messagebox.showinfo("Alerta", "¡Tiempo completado!")

def actualizar_RelojPorSeg():
    hora_actual = time.strftime("%H:%M:%S") # Toma la hora actual
    etiqueta_reloj.config(text=hora_actual) # Configura etiqueta reloj con la hora actual
    ventana.after(1000,actualizar_RelojPorSeg) # Actualiza la ventana cada 1000 ms llamandose a si mismo

def iniciar_temporizador():
    tiempo_restante = int(entry_temporizador.get()) # Recibe el input de temporizador
    while tiempo_restante > 0:
        etiqueta_temporizador.config(text=tiempo_restante)  # Configura la etiqueta temp. como tiempo_restante
        tiempo_restante -= 1    # Se resta seg por seg
        ventana.update()    # Se asegura que se va a actualizar la interfaz del usuario
        time.sleep(1)   # Se realiza una pausa de 1 segundo
    etiqueta_temporizador.config(text="¡Tiempo completado!")  
    mostrar_alerta()  # Finalizado while configura etiqueta temp. como "¡tiempo completado!"

window = tk.Tk()   # Se crea la ventana
window.title("- Reloj Temporizador -")

ventana = tk.Frame(window, padx=20, pady=20)  # Crea un Frame con padding de 20 píxeles en cada lado
ventana.pack()
ventana.configure(background='#1D1B2F')

etiqueta_reloj = tk.Label(ventana, font=("Montserrat", 36, "bold"), bg='#1D1B2F', fg='light green')
etiqueta_reloj.grid(row=1, column=0)

etiqueta_temporizador = tk.Label(ventana, font=("Montserrat", 18), bg='#1D1B2F', fg='light green')
etiqueta_temporizador.grid(row=2, column=0)

entry_temporizador = tk.Entry(ventana, font=("Arial", 18), bg='#1D1B2F', fg='light green', insertbackground='light green')
entry_temporizador.grid(row=3, column=0)

boton_iniciar_temporizador = tk.Button(ventana, text="Iniciar Temporizador", command=iniciar_temporizador, font=('Arial', 12), bg='light green', fg='black', padx=10, pady=5, bd=0, relief=tk.SOLID)
boton_iniciar_temporizador.configure(borderwidth=2, highlightthickness=2)
boton_iniciar_temporizador.grid(row=4, column=0, pady=(20))

actualizar_RelojPorSeg()

ventana.mainloop()