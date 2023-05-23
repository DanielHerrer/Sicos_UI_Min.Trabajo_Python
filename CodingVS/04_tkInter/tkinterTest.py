import tkinter as tk

def enviar():
    print("Se cargo correctamente")

def crearVentana():
    ventana = tk.Tk()
    ventana.geometry("500x500") 
    return ventana

def crearLabel(ventana, valor):
    etiqueta=tk.Label(ventana,text="Ingrese "+valor)
    etiqueta.pack()
    CajaTexto=tk.Entry(ventana)
    CajaTexto.pack()

def crearBoton(ventana,enviar):
    Boton=tk.Button(ventana,text="Enviar Texto",command=enviar)
    Boton.pack()

ventana = crearVentana()
crearLabel(ventana,"Nombre")
crearLabel(ventana,"Apellido")
crearLabel(ventana,"Edad")
crearLabel(ventana,"Sexo")
crearLabel(ventana,"Carrera")

crearBoton(ventana,enviar)

ventana.mainloop()