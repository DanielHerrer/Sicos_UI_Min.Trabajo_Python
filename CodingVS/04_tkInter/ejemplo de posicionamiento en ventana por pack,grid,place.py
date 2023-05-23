import tkinter as tk

ventana = tk.Tk()
ventana.geometry("500x500")
# Usando pack()
#etiqueta1 = tk.Label(ventana, text="Elemento 1 - Pack")
#etiqueta1.pack()

# Usando grid()
etiqueta2 = tk.Label(ventana, text="Elemento 2 - Grid")
etiqueta2.grid(row=0, column=1)

etiqueta3=tk.Label(ventana, text="Elemento 3 - Grid")
etiqueta3.grid(row=0 , column=2)

etiqueta4=tk.Label(ventana , text="")
etiqueta4.grid(row=0 , column=3)

etiqueta5=tk.Label(ventana, text="Elemento 5 - Grid")
etiqueta5.grid(row=0 , column=4)


#Etiqueta 2             etiqueta 3          etiqueta4( vacia)            etiqueta 5

# Usando place()
#etiqueta3 = tk.Label(ventana, text="Elemento 3 - Place")
#etiqueta3.place(x=100, y=50)

ventana.mainloop()
