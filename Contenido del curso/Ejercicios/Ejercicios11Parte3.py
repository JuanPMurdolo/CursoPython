'''
Ejercicio 1

Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado con argumentos 
de base y altura; y la otra el area de un circulo con argumento de radio
'''
import math
def cuadrado(base, altura):
    if base != altura:
        print("el area del rectangulo es: ", base * altura)
    else:
        print("el area del cuadrado es:" , math.pow(base, 2))

def circulo(radio):
    print("El area del circulo es: ", math.pi * math.pow(radio, 2))


'''
Ejercicio 2

Escribir una función que reciba una muestra de números en una lista y devuelva su medida.
'''
def medida(*datos):
    lista2 = tuple(datos[0])
    print(len(lista2))
    return(lista2)

bas = int(input("Ingresa la base: "))
alt = int(input("Ingrese altura: "))
rad = int(input("Ingrese el radio: "))
cuadrado(bas, alt)
circulo(rad)
lista = []
numero1 = int(input("Ingresa un numero: "))
while numero1 != -1:
    lista.append(numero1)
    print(lista)
    numero1 = int(input("Ingresa un numero: "))
print(medida(lista))
