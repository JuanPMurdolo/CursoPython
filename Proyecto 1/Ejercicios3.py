#Hacer un programa que haga la formula de bascara
import math


valorA = int(input("ingrese el valor de A :"))
valorB = int(input("ingrese el valor de B :"))
valorC = int(input("ingrese el valor de C :"))

solucionUno = ((-valorB)+(math.sqrt(math.pow(valorB, 2)-4*valorA*valorC)))/(2*valorA)
solucionDos = ((-valorB)-(math.sqrt(math.pow(valorB, 2)-4*valorA*valorC)))/(2*valorA)

print("La soluciones son:", solucionUno, solucionDos)

#Se desea obtener un algoritmo que permita determinar y mostrar el promedio que ha obtenido
#un alumno en un determinado curso, conociendo las notas de: tres practicas, el examen parcial y el examen final

valorNota1 = float(input("ingrese el valor de la nota de la practica 1 :"))
valorNota2 = float(input("ingrese el valor de la nota de la practica 2 :"))
valorNota3 = float(input("ingrese el valor de la nota de la practica 3 :"))
valorNota4 = float(input("ingrese el valor de la nota del examen parcial :"))
valorNota5 = float(input("ingrese el valor de la nota del examen final :"))

PP = (valorNota1 + valorNota2 + valorNota3)/3
notaFinal = (PP + (2*valorNota4) + (3*valorNota5))/6
print("la nota final es: " , notaFinal)