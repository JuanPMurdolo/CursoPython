'''Crear un programa con tres clases Universidad, con atributos nombre (Donde se almacena el nombre de la Universidad). 
Otra llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante). 
Una ultima llamada Estudiante, que tenga como atributos su nombre y edad. 
El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona.'''

from mailbox import NoSuchMailboxError


class Universidad():
    def __init__(self, nombre) -> None:
        self._nombreUni = nombre

class Carrera():
    def __init__(self, especialidad) -> None:
        self._especialidad = especialidad
    
    def carrera(self,especialidad):
        self._especialidad = especialidad

class Estudiante(Universidad, Carrera):
    def datos(self,nombre,edad):
        self._nombre = nombre
        self._edad = edad
        print("Mi nombre es {}, tengo {} años, mi especialidad es {}. Estudio en la Universidad {}".format(self._nombre,self._edad,self._especialidad,self._nombreUni))

persona = Estudiante("UCALP")
persona.carrera("Sistemas")
persona.datos("Juan", 30)