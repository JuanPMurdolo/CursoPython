#--------------------------------Variables en Python
#<nombre var> = <valor>
nombre = "juan carlos"
numero = 10
flotante = 3.14

print(type(nombre))
print(nombre)
print (type(numero))
print(numero)
print(type(flotante))
print(flotante)

#3 Comillas simples para comentarios de varias lineas
'''En Pythono existen las constantes formalmente pero como una forma comun de  usarlas es
Definir en mayusuclas el nombre de la variable sabiendo que va a ser una constante'''
CONSTANTE = 100

#--------------Seccion 4----------------------
#Numeros
#En lo que es numeros para python existe entero y flotante, nada mas

numeroUno = 140
numeroDos = 100.10

#float(<numero entero>) convierte a flotante un  numero  entero o un string si es posible, hay que asignarlo para usarlo
print(type(numeroUno))
print(numeroUno)
numeroUno = float(numeroUno)
print(type(numeroUno))
print(numeroUno)

#int(<numero flotante>) convierte un flotante o un string a un numero entero, hay que asignarlo
print(type(numeroDos))
print(numeroDos)
numeroDos = int(numeroDos)
print(type(numeroDos))
print(numeroDos)

#------------------Operaciones Aritmeticas-----------------------
#Suma Suma = numero + numero
#Resta Resta = numero - numero
#Division Division = numero / numero
#Multiplicacion Multiplicacion = numero * numero
#Exponenciacion Exponeenciacion = numero ** numero
#Division Entera DivisionEntera = numero // numero
#Tomar el resto de una division Resto = numero % numero
