#Ejercicio 1
#Hacer la operacion matematica  (3+2) dividido (2*5). Todo elevado al cuadrado
cuenta = ((3+2)/(2*5))**2
print (cuenta)

#Variante Ejercicio1
cuenta = pow(((3+2) / (5*2)), 2)
print(cuenta)

#Ejercicio2
#Una jugueteria tiene mucho exito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa 
#de logistica les cobra  por peso de cada paquete, asi que deben calcular el peso de los payasos y de las muñecas que
#saldran en cada paquete a demanda. Cada payaso pesa 112g y cada muñeca 75g. Un cliente frecuente pide la cantidad
#de 23 payasos y 54 muñecas, realiza un programa que muestre el peso total de toda la venta

PAYASO = 112
MUNIECA = 75

totalVenta = (23 * PAYASO) + (54 * MUNIECA)
totalVenta = totalVenta / 100
print("el peso total de la venta es ", totalVenta, " kilos")

#Ejercicio3
#
