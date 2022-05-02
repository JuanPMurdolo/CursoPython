#Listas

#Es lo mismo que un array de java

# Se usan corchetes[] y ,
lista = ["juan", "Pepe", "Rogelio"]
listaInicializadaVacia = []
#La listas pueden ser homogeneas o heterogeneas
#Homogeneas = Toda la lista de un mismo dato
#Heterogeneas = Tiene dos o mas tipos de datos

listaHomogenea = ["Python" , "Lista", "Homo" , "Genea"]
listaHeterogenea = ["Python" , 1, 'tema' , 6.16]

#Para imprimir una lista
print(type(lista))
print(type(listaHeterogenea))
print(type(listaHomogenea))
#imprimir un elemento de una lista
print(listaHomogenea[3])

#-len- cuantos espacios ocupados tiene la lista
print(len(listaHomogenea))

#Las listas son mutables
print(listaHomogenea)
listaHomogenea[0] = "python"
print(listaHomogenea)

#Las listas tambien tienen debanado como las strings
count = 0
contenido = 0
lista = []
#Para llenar la lista (El loco del video lo hace a mano)
while count < 10:
    lista.append(contenido)
    count += 1
    contenido += 1
    print(lista)
    print(lista [0 : 5])
    print(lista [ : 2])
    print(lista [1 : 0])
    print(lista[-1])

#Metodos que se pueden usar con las listas
#append se usa para agregar un item al final de la lista
print(lista)
lista.append(12)
print(lista)

#Insert se usa para agregar un valor en una posicion espefica de la lista
#Se usa con lista.insert(posicionEspecifca, valor)
print(lista)
lista.insert(3, 5)
print(lista)

lista= [5 , 4 , 2 , 3 , 1]

#Count funciona para contar la cantidad de veces que aparece un elemento en una lista
#lista.count(elementoAContar)
print(lista.count(5))

#Index
#Va a recibir un parametro y va a buscarlo en toda la lista y devuelve la posicion
#Retorna siempre la primera posicion que encuentra, si tengo un numero repetido usa su primer aparicion
#lista.index(elementoABuscar)
print(lista.index(1))

#Sort
#Se usa para ordenar,  no lleva parametro
print(lista)
lista.sort()
print(lista)

#Reverse ordena la lista al reves
lista.reverse()
print(lista)

#Actualizar datos dentro de las listas
lista = ['Python' , 24 , 'rene' , 'alexander' , 12]

print(lista)
espacioDelDato = lista.index("alexander")
lista[espacioDelDato] = "Alexander"
print(lista)

#Eliminar datos de una lista

#Pop
#No lleva parametros y siempre elimina el ultimo dato de la lista
lista.pop()
print(lista)
lista.pop()
print(lista)

#Remove
#Este metodo va a buscar el elemento y elimina el valor deseado.
#lista.remove(DatoARemover)
lista.remove(24)

#Como llenar una lista vacia
lista = []
edad = int(input("Ingresa tu edad: "))
while edad < 99:
    lista.append(edad)
    edad = int(input("Ingresa tu edad: "))

print(lista)

#Como utilizar operadores aritmeticos para trabajar con listas
#Solo funciona la suma
lista = [1 , 2 , 3]

listaDos = [4, 5, 6]
listaTres = lista + listaDos
#La suma de dos listas
print(listaTres)

