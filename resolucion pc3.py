
#____________________________________________________________

#problema 1

print("introducir la palabra: ")
my_string = str(input())

j = 0
for i in my_string:
    if i!=' ':
        j+= 1
    else:
        j = 0

print(f"el numero de letras de la palabra es : {j} ")

#____________________________________________________________

#problema 2


string1="clasedepython"

print("la palabra despues de comenzar con mayuscula es  :  ")

a =print(string1.capitalize())
    

#____________________________________________________________


#problema 3

import math

class circulo:
    def __init__(self,radio):  #definir el radio del circulo
        self.radio=radio

    def hallararea(self):
        a=math.pi*self.radio**2     #usando la libreria math , math.pi*self.radio**2 
        print(f"el area es :{a}")



radio=int(input("ingresar radio: "))   #creacion del ojeto

circulo1=circulo(radio)       #funcionalidades
circulo1.hallararea()

#____________________________________________________________

#problema 4

class rectangulo:
    def __init__(self,largo,ancho)->int:  #definir el largo y ancho del rectangulo
        self.largo=largo
        self.ancho=ancho

    def hallararea(self):
        a=self.largo*self.ancho     #usando la libreria math
        print(f"el area es :{a}")


largo=int(input("ingresar largo: "))        #creacion del ojeto                                                         
ancho=int(input("ingresar ancho: ")) 


rectangulo1=rectangulo(largo,ancho)       #funcionalidades

rectangulo1.hallararea()


#____________________________________________________________

#problema 5




#____________________________________________________________

#problema 7

def triangulopascal(nfilas):
    fila=[1]         #variables
    cero=[0]      

    for i in range(nfilas):
        print(fila)

        fila=[i+ d for i,d in zip(fila+ cero,cero+ fila)]
                             #tupla uso de zip para comprimir los datos


triangulopascal(8)    

#____________________________________________________________

#problema 9















