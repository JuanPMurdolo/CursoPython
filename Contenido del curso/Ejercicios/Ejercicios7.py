#Ejercicios de Listas

#Ejercicio1
#En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir 
#dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar

from re import I


lista = [20, 50, "Curso" , "Python", 3.14]
print(lista)
dato = input("Ingresa un dato: ")
lista[0] = dato
dato = input("Ingresa un dato: ")
lista[1] = dato
print(lista)

#Ejercicio2
'''Escribe una lista que tenga los numeros del 1 al 10. Luego, debes hacer que los datos que estan en las posiciones 4, 7 y 9
sean multiplicados por 2, mostrar la lista con los nuevos datos'''
lista = []
i = 0
while i<10:
    i += 1
    lista.append(i) 
    

print(lista)
i = 0

while i<10:
    if i == 4 or i == 7 or i == 9:
        lista[i] = lista[i] * 2
    i += 1

print(lista)
