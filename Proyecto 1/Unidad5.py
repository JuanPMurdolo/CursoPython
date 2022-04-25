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


