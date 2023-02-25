#Algoritmo que muestre numeros divibles entre 5 de una lista
#Creamos una lista
lista_numeros = [22,14,55,17,20]
#Creamos una lista vacía para almacenar los números divisibles
lista_divisibles = []
#creamos un bucle para leer cada elemento de la lista 
# y comprobamos la divisibilida con condicionales
for a in lista_numeros:
    if a % 5 == 0:
        #True: Agregamos a la lista vacía
        lista_divisibles.append(a)
#Muestra de números divisibles
print(lista_divisibles)


