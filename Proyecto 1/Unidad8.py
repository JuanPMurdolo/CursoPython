#Condicionales

#IF
edad = int((input("Inserte la edad: ")))
if edad >= 18:
    print("Mayor")
else:
    print("Menor de edad")

#ELIF
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

#Condicionales Anidados
#Estructura de un if con un if adentro
nombre = "Juan"
edad = 17
if nombre == "Juan":
    if edad >= 18:
        print("sos juan y sos mayor")
    else:
        print("sos juan y sos menor")
else:
    print("No sos juan")

