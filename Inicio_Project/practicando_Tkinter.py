#importamos Tkinter
from tkinter import *
#creando función
def mifuncion():
    print("Presionaste click")
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
botón = Button(ventana, text="CLICK", command=mifuncion)#creamos una función para que sea ejecutada
botón.pack()#lo empaquetamos para que funcione
#añadimos el bucles
ventana.mainloop()
