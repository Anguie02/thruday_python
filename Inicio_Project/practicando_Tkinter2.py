#importamos las clases que queremos usar
from tkinter import Tk, Label, Button, Entry
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

caja3 = Label(vent_principal, text="Resultado",bg="sky blue")
caja3.place(x=10,y=120,width=100,height=30)

vent_principal.mainloop()