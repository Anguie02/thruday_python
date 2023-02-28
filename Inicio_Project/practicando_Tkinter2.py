#importamos las clases que queremos usar
from tkinter import Tk, Label, Button, Entry
#Creamos una función para el boton sumar
def fsumar():
    n1 = caja_text.get()#con el método get obtenemos el valor de la caja de texto
    n2 = caja_text2.get()
    r = float(n1) +float(n2) 

#creamos la ventana principal
vent_principal = Tk()
vent_principal.title("Hello back")
vent_principal.geometry("600x400")
#Añadimos Label  y lo ubicamos
caja = Label(vent_principal,text="Primer numero",bg="sky blue")
caja.place(x=10,y=10,width=100,height=30)
#Añadimos cajas de texto con Entry
caja_text= Entry(vent_principal,bg="pink")
caja_text.place(x=120,y=10,width=100,height=30)
#Añadimos otros Label
caja2 = Label(vent_principal,text="Segundo número", bg="sky blue")
caja2.place(x=10,y=50,width=100,height=30)
#Segunda caja de texto
caja_text2= Entry(vent_principal,bg="pink")
caja_text2.place(x=120,y=50,width=100,height=30)
#Añadimos un boton
caja_suma = Button(vent_principal,text="Sumar", command=fsumar)
caja_suma.place(x=230,y=50,width=80,height=30)

caja3 = Label(vent_principal, text="Resultado",bg="sky blue")
caja3.place(x=10,y=120,width=100,height=30)
#Tercera caja de texto
caja_text3= Entry(vent_principal,bg="pink")
caja_text3.place(x=120,y=120,width=100,height=30)
vent_principal.mainloop()