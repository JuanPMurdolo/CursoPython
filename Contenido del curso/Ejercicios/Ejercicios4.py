#Ejercicio1
#Escribir un programa que solicite al usuario una vocal en minuscula y luego una letra en mayusculas
#El programa debe convertir la letra en minuscula y la vocal en mayuscula, y al final deben ser concatenadas ambas.

vocal = input("ingrese una vocal en minuscula: ")
letra = input("ingrese una letra en mayuscula: ")
print(vocal.swapcase() + letra.swapcase())

#Ejercicio2
#Hacer un programa que pida al usuario su nombre, su edad y su sexo y los muestra de la siguiente forma
# Te llamas: <nombre>
# Tu edad es: <edad>
# Eres <Sexo>
nombre = input("ingresa tu nombre: ")
edad = int(input("ingresa tu edad: "))
sexo = input("ingresa tu sexo: ")
print("Te llamas: {}, Tu edad es {}, eres {}".format(nombre,  edad, sexo))