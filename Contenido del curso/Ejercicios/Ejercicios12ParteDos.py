'''Ejercicio 1

Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. 
Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. 
Llamar a la clase Calculadora.'''

class Calculadora():
    def __init__(self, a , b) -> None:
        self._a = a
        self._b = b

    @property
    def Suma(self):
        return self._a + self._b

    @property
    def Resta(self):
        return self._a - self._b

    @property
    def Multiplicacion(self):
        return self._a * self._b

    @property
    def Division(self):
        try:
            return self._a / self._b
        except ZeroDivisionError:
            return "No se puede dividir por 0"

numA =  float(input("Ingresa un numero: "))
numB =  float(input("Ingresa otro numero: "))

calcu = Calculadora(numA, numB)
print(calcu.Suma)
print(calcu.Resta)
print(calcu.Multiplicacion)
print(calcu.Division)