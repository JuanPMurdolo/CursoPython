'''Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; 
luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. 
Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes. 
Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno'''

class Fabrica():
    def __init__(self, llantas, color, precio) -> None:
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    @property
    def llantas(self):
        return self._llantas
    
    @property
    def color(self):
        return self._color
    
    @property
    def precio(self):
        return self._precio

class Moto(Fabrica):
    def __init__(self, color, precio) -> None:
        super().__init__(2, color, precio)

class Auto(Fabrica):
    def __init__(self, color, precio) -> None:
        super().__init__(4, color, precio)

auto = Auto("negro", 120000)
print(auto.color)
print(auto.llantas)
print(auto.precio)

auto = Moto("negro", 120000)
print(auto.color)
print(auto.llantas)
print(auto.precio)