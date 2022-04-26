#Unidad8
#Crear un programa que pida al usuario una  letra, y si es vocal, muestre el mensaje es vocal. Sino decirle al usuario que no es vocal 
letra = input("Ingrese una vocal: ")

if letra.lower() == "a":
    print("Esta vocal es la A")
elif letra.lower() == "e":
    print("Esta vocal es la E")
elif letra.lower() == "u":
    print("Esta vocal es la U")
elif letra.lower() == "i":
    print("Esta vocal es la I")
elif letra.lower() == "o":
    print("Esta vocal es la O")
else:
    print("no es una vocal")

#Ejercicio2
#Escribir un programa que, dado un numero entero, muestre su valor absoluto.

ingreso = int(input("ingrese un numero: "))
if (ingreso < 0):
    print("valor absoluto de ingreso es:", ingreso * -1)
else:
    print("valor absoluto de ingreso es:", ingreso)