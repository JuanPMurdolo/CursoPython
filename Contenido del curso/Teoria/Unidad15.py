#Errores
#Exception (Try, Catch)
while True:
    try:
        edad = int(input("ingresala: "))
        print("Tu edad es: ", edad)
        break
    except:
        print("Ingresaste un valor que no es un numero")
    finally:
        print("La ejecucion finalizo")
#Excepciones multiples
while True:
    try:
        num1 = int(input("Ingresa un numero"))
        resultado = 100/num1
        print(resultado)
        break
    except ZeroDivisionError:
        print("no se puede dividir por 0")

while True:
    try:
        edad = int(input("Ingresa edad"))
        print(edad)
        break
    except ValueError:
        print("valor erroneo")

while True:
    try:
        edad = int(input("Ingresa edad"))
        print(edad)
        break
    except KeyboardInterrupt:
        print("ejecucion cancelada")
        break
