
#problema 8

#Desarrollar un módulo que contenga las siguientes funciones:

# Que genere 20 números enteros aleatorios entre 0 y 100 y devuelva una lista.
# Mostrar la lista obtenida por pantalla.
#  Ordenar los valores de la lista y mostrarla por pantalla.



# importamos el modulo random
import random
 
# función para generar la lista de valores aleatorio
def numeros():
    lista=[]
    for n in range(20):
        num=random.randint(0,100)    #al azar
        lista.append(num)
    return lista
 
 
def imprimir(lista):                            # función para imprimir y ordenar

    print(lista)
 
def ordenar(lista):

    return lista.sort()     #al azar





