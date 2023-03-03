#Importamos tkinter
from tkinter import *
#Definimos la función para imprimir los datos
def imprimir_todo():
    #Guardamos los datos en variables y los mostramos 
    dni,apellidos,nombres,direccion,telefono,codigo, cantidad, precio = caja_txt1.get(), caja_txt2.get(), caja_txt3.get(), caja_txt4.get(), caja_txt5.get(), caja_text6.get(), caja_txt7.get(), caja_txt8.get()
    return print("\nDNI:            ",dni, "\nApellidos:      ", apellidos, "\nNombres:        ", nombres, "\nDirección:      ", direccion,"\nTeléfono:       ", telefono,"\nCod_prod:       ", codigo, "\nCantidad:       ", cantidad, "\nPrecio_unidad:  ", precio)

#Creamos la ventana principal(un objeto) a partir de la clase TK
window = Tk()
#Agregamos un titulo y definimos las dimenciones de la ventana
window.title("Ferretería El Tornillo Feliz ")
window.geometry("600x400")
#Añadimos un icono
window.iconbitmap("tornillo.ico")
#Añadimos la clase Label, para crear la primera etiqueta, el cual estara en la ventana principal
caja_dni = Label(window, text="DNI", bg="sky blue")
caja_dni.place(x=10,y=10,width=100, height=30)
#Añadimos una caja de texto, para que el usuario pueda ingresar sus datos
caja_txt1 = Entry(window)
caja_txt1.place(x=120,y=10,width=100,height=30)
#Añadimos la etiqueta para Apellidos
caja_apellidos = Label(window, text="Apellidos", bg="sky blue")
caja_apellidos.place(x=10,y=50,width=100, height=30)
#caja texto
caja_txt2 = Entry(window)
caja_txt2.place(x=120,y=50,width=100,height=30)
#Añadimos la etiqueta para Nombres
caja_nombres = Label(window, text="Nombres", bg="sky blue")
caja_nombres.place(x=10,y=90,width=100, height=30)
#Caja texto
caja_txt3 = Entry(window)
caja_txt3.place(x=120,y=90,width=100,height=30)
#Añadimos la etiqueta para Dirección
caja_direccion = Label(window, text="Dirección", bg="sky blue")
caja_direccion.place(x=10,y=130,width=100, height=30)
#caja texto
caja_txt4 = Entry(window)
caja_txt4.place(x=120,y=130,width=130,height=30)#esta es la caja que amplié
#Añadimos la etiqueta Telefono
caja_telefono = Label(window, text="Telefono", bg="sky blue")
caja_telefono.place(x=310,y=130,width=100, height=30)
#Caja texto
caja_txt5 = Entry(window)
caja_txt5.place(x=420,y=130,width=100,height=30)
#Añadir etiqueta y caja de texto para el código del producto
caja_codigo = Label(window, text="Cod_Prod", bg="sky blue")
caja_codigo.place(x=10,y=180,width=100,height=30)
#caja de texto
caja_text6 = Entry(window)
caja_text6.place(x=120,y=180,width=100,height=30)
#Añadir etiqueta y caja de texto para la cantida
caja_cantidad = Label(window, text="Cantidad", bg="sky blue")
caja_cantidad.place(x=310,y=180,width=100, height=30)
#cja de texto
caja_txt7 = Entry(window)
caja_txt7.place(x=420,y=180,width=100,height=30)
#Añadimos un boton 
boton = Button(window,text="TOTAL")
boton.place(x=310,y=230,width=100,height=30)
#Añadimos una caja de texto, en el cual mostraremos el total
caja_txt8= Entry(window)
caja_txt8.place(x=420,y=230,width=100,height=30)
#Añadimso una etiqueta y caja de texto para precios del producto
caja_precio = Label(window, text="Precio", bg="sky blue")
caja_precio.place(x=10,y=230,width=100, height=30)
#caja de texto
caja_txt9 = Entry(window)
caja_txt9.place(x=120,y=230,width=100,height=30)
#Añadimos un boton para imprimir
imprimir = Button(window,text="IMPRIMIR",command=imprimir_todo)#Ya podemos usar la función  en el boton para imprimir
imprimir.place(x=10,y=290,width=100,height=30)
window.mainloop()
