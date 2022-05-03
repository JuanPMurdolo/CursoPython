#POO
#Clases en Python
'''
class <nombreDeLaClase>():
    definicion
'''


class FabricaTelefono():
    pass

print(type(FabricaTelefono));#devuelve Type porque una clase en python es tipo Type

celular = FabricaTelefono()
print(type(celular));#Devuelve el tipo FabricaTelefono

def fabricaTelefono():
#No importa si las funciones y clases tienen los mismos nombres
#Pero si entra en conflicto cuando haces el type de FabricaTelefono
    pass

print(type(fabricaTelefono()));#aca va a estar el error
#Solucion: Las clases empiezan en mayuscula las funciones en minuscula

#Metodos y atributos
def funcion():
    pass

#Pero en una clase una funcion definida pasa a ser un metodo
class Vehiculos():
    marca = "Ford"
    color = "Negro"
    motor = "V12"
    puertas = 3

    def llamar(self, mensaje):
        return mensaje

auto = Vehiculos()
print(auto.llamar("HOLA"))

#Self e Init
class Fabrica():
    marca = "Samsung"

    def ElaborarHuawei(self):
        marca = "Huawei";#esto no cambiara la marca 
        print(self.marca)
        self.marca = "Huawei";#Esto si va a cambiar la marca por el contexto
        print(self.marca)

telefono = Fabrica()
print(telefono.marca)
telefono.ElaborarHuawei()
print(telefono.marca)

class FabricaDos():
    marca = ""
    color = ""
#Es lo mismo que un constructor de java
    def __init__(self, marca , color) -> None: 
        print("Ejecutando init porque se inicializo un nuevo objeto");#El init se ejecuta siempre que se instancia un objeto
        print("El objeto {} fue creado".format(self.marca))
        self.marca = marca
        self.color = color
    #Otros Metodos
    def __del__(self):
        print("El objeto {} fue destruido".format(self.marca))
    #Sirve para que al momento de imprimir un objeto en lugar de mostrar su espacio en memoria muestre un dato
    def __str__(self):
        return "El objeto es {}".format(self.marca)


prueba = FabricaDos("Samsung", "Blanco")
print(prueba.marca)
print(prueba.color)




#Ultimo video
class EjemploFinal():
    def __init__(self , marca, *colores, **modelos):
        self.marca = marca
        self.colores = colores
        self.modelos = modelos


ejemplo = EjemploFinal("SAMSUNG", "NEGRO", "BLANCO", "AZUL", m1=500 , m2=600, m3=540)
print(ejemplo.marca)
for i in ejemplo.colores:
    print(i)
for j in ejemplo.modelos:
    print(j)
#Tambien se le pueden asignar atributos asi pero son para la instancia del objeto sobre la que se crea y no sobre la clase en si misma.
ejemplo.memoria = 500
print(ejemplo.memoria)