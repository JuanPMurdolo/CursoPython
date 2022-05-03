'''
Ejercicio 1
Crear una funcion que pida dos numeros. Si el primero es mayor al segundo, 
el programa debe retornar el valor 1; si el segundo es mayor al primero, debe retornar -1; si ambos son iguales, debe retornar 0
'''
def FuncionNumero():
    numero1 = int(input("Ingresa un numero: "))
    numero2 = int(input("Ingresa otro numero: "))
    if numero1 > numero2:
        return 1
    elif numero2 > numero1:
        return -1
    elif numero1 == numero2:
        return 0
'''
Ejercicio 2

Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, 
y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
'''
def Factura(valor, iva):
    if iva != 0:
        if iva > 0:
            total = float(((valor * iva)/100)+valor)
            return total
        else:
            return "El monto del iva es negativo y no se puede calcular"
    else:
        total = float(valor * 1.21)
        return total


print(FuncionNumero())
numero = float(input("Ingresa el valor de la factura sin IVA: "))
numero2 = float(input("Ingresa el valor del IVA: "))
print(Factura(numero, numero2))