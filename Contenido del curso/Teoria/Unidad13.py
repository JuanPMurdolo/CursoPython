#Bucles (Loop)
#Se repite tantas veces como se cumpla una codición determinada

#While
#Ejemplo
n = 5
while n > 0:
    print(n)
    n -= 1

#For
#Ejemplo
lista = [1 , 2 , 3 , 4]
for i in lista:
    print(i)

#Funcion Range para for
#Delimita un punto en especifico en el que se va a recorrer un bucle
for i in range(1, 11):
    print("bucle :" , i)
#for i in range(valorInicial, valorFinal, deAcuantosValoresQuiero que tome el bucle por defecto de a uno)
for i in range(1, 11, 2):
    print("bucle :" , i)

for i in range(-10 , 0):
    print("bucle :" , i)


#Continue & Break
for i in range(1, 11):
    print(i)
    if i==5:
        break;#break funciona para cortar en una condicion especifica un for, puede servir para cortar cuando ya se encontro lo que se buscaba en una lista

for j in range(1, 11):
    if j==6:
        continue;#Va a saltearse el 6, haciendo que cuando se cumpla la condición se saltee ese paso y se siga con el siguiente
    print(j)

