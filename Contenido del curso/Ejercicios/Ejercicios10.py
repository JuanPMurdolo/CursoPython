#Bucles

#WHILE
'''Ejercicio 1

Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero
'''
numero = int(input("Ingresa un numero: "))
i = 1
while i < 10:
    print(numero * i)
    i += 1

'''
Ejercicio 2

Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).'''
numero = int(input("Ingresa su edad: "))
while numero > 0:
    print(numero)
    numero -= 1

#FOR

'''
Ejercicio 1
Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros y mostrar el rango de numeros entre ambas cifras
'''
lista = []
for i in range(1 , 11):
    lista.append(i)
print(lista)
lista.clear()
numero1 = int(input("Ingresa un numero: "))
numero2 = int(input("Ingresa otro numero: "))
for i in range(numero1, numero2+1):
    lista.append(i)
print(lista)
lista.clear()

'''
Ejercicio 2
Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango de esos 2 números, pero, solo imprimiendo los números que sean impares
'''
numero1 = int(input("Ingresa un numero: "))
numero2 = int(input("Ingresa otro numero: "))
for i in range(numero1, numero2+1):
    if i % 2 == 0:
        continue
    lista.append(i)
print(lista)
lista.clear()