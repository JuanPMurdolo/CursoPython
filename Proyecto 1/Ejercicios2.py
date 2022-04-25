#Ejercicio1
#Crear un programa que tenga una variable con la cadena "Te quiero solo como amigo", y muestre los siguientes datos
#Imprima los dos primeros caracteres
#Imprima los 3 ultimos caracteres
#Imprima dicha cadena cada dos caracteres
#Imprima dicha cadena en sentido inverso
#Imprima la cadena en un  sentido y en  sentido inverso

cadena = "Te quiero solo como amigo"
print(cadena[0 : 1])
print(cadena[-3 : ])
print(cadena [: : 2])
print(cadena[: : -1])
print (cadena + cadena[: : -1])

#Ejercicio2
#Crear un programa que tenga una varitable con la cadena "Separado" y un caracter de ,; e inserte
# el caracter entre cada letra de la cadena. 
cadena2 = "Separado"
print(cadena2)
cadenaReemplazo = cadena2.replace("", ",")
print(cadenaReemplazo)