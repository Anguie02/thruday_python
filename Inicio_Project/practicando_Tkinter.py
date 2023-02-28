#importamos Tkinter
from tkinter import *
#creamos la raiz o ventana a partir de la clase Tk
ventana = Tk()
#añadimos un titulo
ventana.title("Hello !")
#configuramos las dimenciones de la ventana
ventana.geometry("600x400")
#añadimos widgest o controles que van dentro de la ventana
etiqueta = Label(ventana, text="Esto es un label")
etiqueta.pack()
#añadimos  otro widget que será el botón
botón = Button(ventana, text="CLICK")
botón.pack()#lo empaquetamos para que funcione
#añadimos el bucle
ventana.mainloop()
