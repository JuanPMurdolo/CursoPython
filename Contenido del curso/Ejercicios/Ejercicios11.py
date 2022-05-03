'''
Ejercicios de funciones

Ejercicio 1
Crear un programa que tenga una lista, luego crear una funcion con la cual se van a 
pedir numeros al usuario para agregar a la lista. Debes crear una segunda funcion en donde se ordenen 
los numeros pares e impares dentro de dos listas nuevas
'''

def FuncionLlenar(dato, lista1):
    lista1.append(dato)

def FuncionOrdernar(listaInicial, listaPar1, listaImpar1):
    indexado = len(listaInicial)
    i = 0
    while i < indexado:
        if listaInicial[i] % 2 == 0:
            listaPar1.append(listaInicial[i])
        else:
            listaImpar1.append(listaInicial[i])
        i += 1
    print("Lista Par:" ,listaPar1)
    print("Lista Impar:" ,listaImpar1)



'''
Ejercicio 2
Escribir una función que reciba un número entero positivo y devuelva su factorial.
'''
def FuncionRecursiva(valor):
    if valor == 0 or valor==1:
        resultado = 1
    elif valor > 1:
        resultado = valor*FuncionRecursiva(valor - 1)
    elif valor < 1:
        resultado = "El numero es negativo no se puede hacer"
    return resultado

#Programa principal
lista = []
listaPar = []
listaImpar = []
numero = int(input("Ingresa un numero: "))
while numero != 100:
     FuncionLlenar(numero, lista)
     numero = int(input("Ingresa un numero: "))
FuncionOrdernar(lista, listaPar, listaImpar)

numero = int(input("Ingresa un numero: "))
print(FuncionRecursiva(numero))



