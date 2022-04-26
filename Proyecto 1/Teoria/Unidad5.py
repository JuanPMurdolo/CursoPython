#Strings
#Los strings pueden ser con comillas simples o dobles es indistinto

# \ esta barra mas el string va a hacer que el string tenga un comportamiento particular
#pasa lo mismo si usas ' en el ejemplo de abajo
cadenaLiteral = "Esto es un ejemplo\"ejemplo\" de cadena"
print(cadenaLiteral)

#salto de linea \n
cadenaSalto = "Esto es un ejemplo: \n Ejemplo de cadena \n con salto"
print(cadenaSalto)

#tabulacion \t
cadenaTab = "Esto es un ejemplo: \t Ejemplo de cadena \t con tabulacion"
print(cadenaTab)

#\b saca un espacio entre
#\f coloca el simbolo &
#\r elimina todo lo que tenga delante

#Concatenacion de cadenas
cadena1 = "Hola"
cadena2 = "Mundo"
numero = 1
print(cadena1 + " " + cadena2)
#* repite una palabra una cantidad x de veces
print(cadena2 * 5)
#la coma tambien sirve para concatenar
print("Hola usuario:", cadena2)
print(numero, cadena1, cadena2)
print(type(str(numero)))

#Debanado de Cadenas Substrings
cadenaDebanado = "Hola vengo a contar la cantidad de caracteres de esta cadena"
print(len(cadenaDebanado))
print(cadenaDebanado[2]) #Toma la l de la cadena anterior, por que es el caracter 3 (la cuenta empieza en 0)
print(cadenaDebanado[0 : 10])
print(cadenaDebanado[0 : 32])
print(cadenaDebanado[-10 : -3]) #Esto es desde el final hacia atras
print(cadenaDebanado [: : 2]) #Imprime la cadena cada 2 caracteres
print(cadenaDebanado[: : -1]) #Imprime la cadena invertida
print (cadenaDebanado + cadenaDebanado[: : -1]) #Imprime la cadena y concatena la cadena invertida

#Metodos de Python
cadena = "Estoy utilizando metodos de Python"
#convierte todas las Mayusculas a minusculas
print(cadena.lower())
#inverso
print(cadena.upper())
#Capitalize hace que la primer letra se convierta en mayusucula
print(cadena.capitalize())
#Title va a convertir la primer letra de cada palabra en mayuscula
print(cadena.title())
#Swapcase convierte las letras en su contraria (Si es mayuscula en miniscula si no al reves)
print(cadena.swapcase())