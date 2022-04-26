#Ejercicio 1
#Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las ultimas 3 letras
#tiene que decir que riman. Si coinciden solo las dos ultimas tiene que decir que riman un poco y si no
#que no riman
palabraUno = input("ingrese la primer palabra: ").lower()
palabraDos = input("ingrese la segunda palabra: ").lower()
if palabraUno[-3 : ] == palabraDos[-3 : ]:
    print("Riman")
elif palabraUno[-2 : ] == palabraDos[-2 : ]:
    print("Riman un poco")
else:
    print("no riman")

#Ejercicio 2
#Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son:
#candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul.
#Segun el candidato elegido (A, B o C) se le debe imprimir el mensaje "Usted ha votado por el partido
# [color que corresponda]". Si el usuario ingresa una opcion que no corresponda a ninguno de los candidatos
# disponibles, indicar "Opcion incorrecta"

candidato = input("Ingrese A B o C para elegir su voto: ").upper()

if candidato == "A":
    print("Voto por el partido rojo")
elif candidato == "B":
    print("Voto por el partido verde")
elif candidato == "C":
    print("Voto por el partido azul")
else:
    print("Opcion incorrecta")