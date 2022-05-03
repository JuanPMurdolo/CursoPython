#Conjuntos (set)
#La funcion set es la que se usa para crear conjuntos
conjuntos = set([(1, 2, 3, 4, 5)])
print(type(conjuntos))
conjunto = { 1 , 2 , 3 , 4 , 5}
print(type(conjunto))
conjuntoTupla = (1 , 2, 3, 4 ,5)
print(type(conjuntoTupla))

#Metodos de los conjuntos
conjunto = { 1, 1, 2,  2, 3, 3 , 4, 4,  5, 5}
lista = [1 , 1 , 2, 3, 4 , 4]
print(lista)
#El comportamiento de un conjunto hace que si tiene valores repetidos no los tenga en cuenta
print(conjunto)

conjunto = { 1 , 2 , 3 , 4, 5}
print(conjunto)
#Add agrega un elemento al principio del conjunto
conjunto.add(32)
print(conjunto)
#Remove
#Elimina el elemento definido
conjunto.remove(1)
#En este caso elimina el 1
print(conjunto)
#Discard
#Funciona igual que el remove
conjunto.discard(2)
print(conjunto)

#Pop elimina  un elemento del conjunto, pero no se sabe cual va a ser el dato que se va a eliminar
conjunto.pop()
print(conjunto)

#Update, agregar un set o lista al conjunto. Si existieran en el conjunto previo al update, no impactaria
conjunto.update([6 , 7, 8 ])
print(conjunto)

#Clear, vacia el conjunto.
conjunto.clear()
print(conjunto)

#Tuplas
#Las tuplas no tienen metodos porque no se pueden agregar o quitar elementos
tupla = (1 , 2 , 3 , 4 , 5)                 ;#buena practica
tuplaSinParentesis = 1 , 2 , 3  , 4 , 5     ;#Funciona igual pero mala practica
tupla2 = ( 6 , 7, 8, 9 , 10)
print(tupla)
print(type(tupla))

print(tuplaSinParentesis)
print(type(tuplaSinParentesis))
print(tupla[2])
print(tupla [0 : 3])
print(tupla + tupla2)
#EN la tupla no se pueden modificar sus valores
