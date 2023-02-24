#Desarrolle un algoritmo en la que muestra la suma del numero actual y su anterior

#Pedimos el ingreso del numero
numero = int(input("Ingrese un número :"))
#creamos un bucle 
for a in range(1, numero):
    numero = a
    #Realizamos la suma del numero actual y el anterior
    suma = numero + (numero -1)

    #Mostramos la suma
    print("La suma de ",numero ,"+", numero -1, "es", suma)

