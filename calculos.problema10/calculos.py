#1.librerias

import operaciones as v 


from calculos.operaciones import sumar
from calculos.operaciones import restar
from calculos.operaciones import multiplicar
from calculos.operaciones import dividir



MSG_BIENVENIDA="Bienvenido al menú interactivo"
MSG_OPCIONES="""¿Qué quieres hacer? Escribe una opción    
        1)calcula la suma
        2)calcular la resta
        3)calcular el producto
        4)calcular la división
        5)salir 
        """
#3.funciones y/o clases
def main():

    print(MSG_BIENVENIDA)
    while True:
        
        opcion = input() # me devuelve un string ''
        if opcion == '1':
                    #aqui estoy usando  v porque me ayudo del modulo validacion de datos
                
            numero1=v.ingreso_entero("ingrese el primer numero entero:")
            numero2=v.ingreso_entero("ingrese el segundo numero entero:")

            suma=sumar(numero1,numero2)
            print(f"la suma de los numeros es : {suma} ")
            
        elif opcion == '2':

            numero3=v.ingreso_entero("ingrese el primer numero entero:")
            numero4=v.ingreso_entero("ingrese el segundo numero entero:")

            resta=restar(numero3,numero4)
            print(f"la suma de los numeros es : {resta} ")
         
        elif opcion == '3':

            numero5=v.ingreso_entero("ingrese el primer numero entero:")
            numero6=v.ingreso_entero("ingrese el segundo numero entero:")

            producto=multiplicar(numero5,numero6)
            print(f"la suma de los numeros es : {producto} ")
            
        elif opcion == '4':
            numero7=v.ingreso_entero("ingrese el primer numero entero:")
            numero8=v.ingreso_entero("ingrese el segundo numero entero:")

            division=dividir(numero7,numero8)
            print(f"la suma de los numeros es : {division} ")

        elif opcion == '5':
             print("Comando desconocido, vuelve a intentarlo")
             break
        else:
            print("Comando desconocido, vuelve a intentarlo")     
    pass

