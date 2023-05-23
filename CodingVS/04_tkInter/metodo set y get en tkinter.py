
import tkinter as tk

def Enviar():
    print("Se cargo correctamente")

ventana= tk.Tk()
ventana.geometry("500x500")

etiqueta=tk.Label(ventana,text="Ingrese:Nombre")
etiqueta.pack()
CajaTexto=tk.Entry(ventana)
CajaTexto.pack()

etiqueta1=tk.Label(ventana,text="Ingrese Apellido:")
etiqueta1.pack()
CajaTexto1=tk.Entry(ventana)
CajaTexto1.pack()

etiqueta2=tk.Label(ventana,text="Ingrese su edad:")
etiqueta2.pack()
CajaTexto2=tk.Entry(ventana)
CajaTexto2.pack()

etiqueta3=tk.Label(ventana,text="Ingrese Telefono:")
etiqueta3.pack()
CajaTexto3=tk.Entry(ventana)
CajaTexto3.pack()

etiqueta4=tk.Label(ventana,text="Ingrese Domicilio:")
etiqueta4.pack()
CajaTexto4=tk.Entry(ventana)
CajaTexto4.pack()


Boton=tk.Button(ventana,text="Enviar Texto",command=Enviar)
Boton.pack()

ventana.mainloop()