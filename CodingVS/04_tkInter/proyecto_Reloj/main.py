# Daniel Franco Herrera

import tkinter as tk
import time

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
    etiqueta_temporizador.config(text="¡Tiempo completado!")    # Finalizado while configura etiqueta temp. como "¡tiempo completado!"

ventana = tk.Tk()   # Se crea la ventana
ventana.title("Reloj y Temporizador")

etiqueta_reloj = tk.Label(ventana, font=("Arial", 24))  # Se crea un label, se vincula a ventana y le damos font size
etiqueta_reloj.pack()   # Se empaqueta de forma predeterminada la etiqueta reloj

etiqueta_temporizador = tk.Label(ventana, font=("Arial", 24))
etiqueta_temporizador.pack()    # Se empaqueta de forma predeterminada la etiqueta temporizador

entry_temporizador = tk.Entry(ventana, font=("Arial", 18))
entry_temporizador.pack()   # Se empaqueta de forma predeterminada el input entry

boton_iniciar_temporizador = tk.Button(ventana, text="Iniciar Temporizador", command=iniciar_temporizador)
boton_iniciar_temporizador.pack()   # Se empaqueta de forma predeterminada el boton

actualizar_RelojPorSeg()
ventana.mainloop()