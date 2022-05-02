#Diccionarios
#Ejercicio1
'''En el siguiente diccionario se encuentran las capitales de los paises del mundo, debes realizar un programa que pida un pais un al usuario
y muestre la capital de ese pais, en dado caso el pais no este en el diccionario, se debe mostrar un mensaje diciendo que el pais no se encuentra'''

paises = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

dato = input("Ingresa un pais: ")
if dato in paises:
    pais = paises.get(dato)
    print("la capital de", dato , 'es:' , pais)
else:
    print(dato, "no existe en la base de datos")
    
#Ejercicio 2
'''Con el siguiente diccionario, debes crear un programa que pregunte al usuario por un número; 
el programa debe imprimir el jugador al que hace referencia ese número'''
jugadores = {1 : "Casillas", 15 : "Ramos", 3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"
}
dato = int(input("Ingresa un numero: "))
if dato in jugadores:
    jugador = jugadores.get(dato)
    print("El numero", dato , 'corresponde a:' , jugador)
else:
    print(dato, "no existe en la base de datos")