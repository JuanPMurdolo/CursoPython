#Tuplas

#Ejercicio 1
#Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla
tuplaMes = ("Enero" , "Febrero" , "Marzo" , "Abril" , "Mayo" , "Junio" , "Julio" , "Agosto" , "Septiembre" , "Octubre" , "Noviembre" , "Diciembre")
dato = int(input("Ingresa un numero: "))
print(tuplaMes[dato - 1])

#Ejercicio 2
#Escribir una tupla que tenga las letras del alfabeto. Luego, debes pedir al usuario un número, el que haya ingresado, es la letra que debe imprimir el programa
tuplaAbecedario = ("a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j", "k" , "l", "m" , "n", "ñ" , "o" , "p", "q" , "r", "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z")
dato = int(input("Ingresa un numero: "))
print(tuplaAbecedario[dato - 1])