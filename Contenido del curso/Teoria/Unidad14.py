#FUnciones de Python

#Ejemplo muy basico sin argumentos
def Funcion():
    print("Hello world")
Funcion()
Funcion()

#Funcion con argumentos
def FuncionArgumentos(mensaje):
    print(mensaje)

FuncionArgumentos("Hola mundo")
FuncionArgumentos("Hola mundo")

#Funciones integradas de Python
'''
Ejemplos de funciones ya usadas

type(usada para saber el tipo de una variable)
int(funcion usada para convertir un dato a entero)3
float(lo mismo que la anterior pero a flotante)
len(sacar la cantidad de caracteres de un String o la cantidad de elementos de una lista)
max y min(sacar los valores mas altos y mas bajos de una lista por ejemplo)
'''

#Con la palabra def python ya entiende que vamos a definir una funcion
'''
def <nombre de la funcion>(<argumentos> o vacio):
    <sentencias>; Importante dejar identado, python maneja la identacion para  definir donde empieza y termina una funcion, loop o if
    return <valor>; sirve para que la funcion retorne un valor como en java
'''

def Saludo():
    print("Hola")
Saludo()
def Tabla7():
    for i in range(10):
        print("7 x {} = {}".format(i, i*7))
Tabla7()


#LIbrerias y/o modulos de Python

#Importacion de librerias
import math
import random
#pow por ejemplo eleva un numero a un exponiente
print(math.pow(10 , 2))
print(math.sqrt(64))
print(math.isqrt(64))
print(math.sin(90))
print(math.cos(90))
print(math.tan(90))
print(math.factorial(10))
print(random.randint(1, 100))

#Argumentos y parametros
#Igual que en pascal,etc
#Al definir una funcion
'''
def suma(num1, num2):
    return num1 + num2
siendo num1 y num2 los argumentos
'''

#Variables Globales
'''
def valores():
    global num1
    global num2
    Primeror hay que englobar las variables y despues si asignarles un valor
    no se puede hacer
                        global num = 0; esto tiraria error
    num1 = 110
    num2 = 40
    resultado = num1 + num2
    return resultado

print(valores())

resta = num1 - num2; esto va a tirar error si las variables num1 y num2 
no tienen la palabra reservada global adelante al ser definidas en 
la funcion, en caso contrario estan aisladas del programa principal(estan encapsuladas)

print(resta) 
'''


#Argumentos indefinidos
'''
def argumento(num):
    return type(num)

print(argumento(10)); imprime integer
print(argumento(56.562)); imprime float
print(argumento("Hola")); imprime str

def argumento2(*num)
    return type(num)

print(argumento2(10 , 20 , 22 , 23 , 24)); imprimiria tupla

def argumento2(*num)
    for i in num
    return type(i)

print(argumento2(10 , 20 , 22 , 23 , 24)); imprimiria int por cada valor de la tupla
'''