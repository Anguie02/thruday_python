#importamos las clases que queremos usar
from tkinter import Tk, Label, Button, Entry
#creamos la ventana principal
vent_principal = Tk()
vent_principal.title("Hello back")
vent_principal.geometry("600x400")
#Añadimos Label  y lo ubicamos
caja = Label(vent_principal,text="Primer numero",bg="sky blue")
caja.place(x=10,y=10,width=100,height=30)


vent_principal.mainloop()