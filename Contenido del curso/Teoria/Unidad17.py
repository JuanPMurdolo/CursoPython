#OOP
#Encapsulamiento
#Aplicar el alcance sobre un atributo de una clase

from mailbox import NoSuchMailboxError


class A():
    def __init__(self):
        self.contador = 0
    
    def incrementar(self):
        self.contador += 1

    def cuenta(self):
        return self.contador

class B():
    def __init__(self):
        self._contador = 0
    
    def incrementar(self):
        self._contador += 1

    def cuenta(self):
        return self._contador

a = A()
print(a.cuenta())
a.incrementar
print(a.cuenta())
print(a.contador)

print("Objeto B")
b = B()
print(b.cuenta())
b.incrementar
print(b.cuenta())
print(b._contador);#Es to no se hace, porque en el momento en el que quiero llamar a un atributo privado


#Profundizar encapsulamiento
class C():
    def __init__(self, contador, cuenta):
        self._contador = contador
        self._cuenta = cuenta
    
    def incrementar(self):
        self._comntador +=1
    
    def cuenta(self):
        return self._contador

c = C(0, 1)
c.cuenta = 20
#la linea de arriba va a funcionar, si bien funciona no es una buena practica, para esto 
#estan los setters y getters. python admite hacer set y get sobre un atributo haciendo objeto.atributo = algo o print(objeto.atributo)

#Metodo get y set
class D():
    def __init__(self) -> None:
        self._cuenta = 0
        self._contador = 0

    #Getters
    #Sin este @Property, el getter habria que llamarlo en la instancia con (), con esto se puede llamar simplemente objeto.funcion
    @property
    def cuenta(self):
        return self._cuenta

    @property
    def contador(self):
        return self._contador
    
    #Setters
    #la anotacion reservada @atributo.setter hace que python ya sepa que el metodo va a modificar un atributo
    @cuenta.setter 
    def cuenta(self , valor):
        self._cuenta = valor
    
    @contador.setter
    def contador(self , valor):
        self._contador = valor


d = D()
print(d.cuenta);#esto es un get bien hecho
print(d.contador)
i = 1
d.contador = i
d.cuenta = i + 1
print(d.cuenta);#esto es un get bien hecho
print(d.contador)

#Herencia
print("--------------------Herencia------------------")
#2 o mas clases que hereden metodos o atributos a la clase hija
#Clase padre
class Animales():
    def __init__(self, nombre):
        self.nombre = nombre
    
    def test(self):
        print("test")
    
    def descripcion(self):
        print("Yo soy un {}".format(self.animal))

#Clases Hijas
class Perro(Animales):
    def __init__(self, nombre, sonido):
        super().__init__(nombre)
        self.sonido = sonido

class Abeja(Animales):
    def __init__(self, animal):
        self.animal = animal

#animal = Animales()
#animal.test()

perro = Perro("Jorgito", "Ladrido")
perro.test()
print(perro.nombre)
print(perro.sonido)

abeja = Abeja("Abeja")
abeja.descripcion()

#Herencia Multiple
print("---------------------Herencia Multiple-----------------------------")
class Y():
    def primera(self):
        return "Esta es la clase Y"

class X():
    def segunda(self):
        return "Esta es la clase X"

class Z(Y,X):
    pass

z = Z()
print(z.primera())
print(z.segunda())

#Polimorfismo
#Modificacion de metodos cuando se heredan de otras clases
print("--------------------------Polimorfismo-----------------------------------")
class EjemplosA():
    def __init__(self, mensaje) -> None:
        self.mensaje = mensaje
    
    def hablar(self):
        print(self.mensaje)

class EjemplosB(EjemplosA):
    def hablar(self):
        print("Ejemplo B")

class EjemplosC(EjemplosA):
    def hablar(self):
        print("Este es ejemplo C")

b = EjemplosB("Example B")
b.hablar()