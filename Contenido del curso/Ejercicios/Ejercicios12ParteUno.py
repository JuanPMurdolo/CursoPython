'''Ejercicio 1
Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del alumno. 
Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.'''

class Estudiante():
    def __init__(self, nombre, nota) -> None:
        self._nombre = nombre
        self._nota = nota

    #Getters
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def nota(self):
        return self._nota
    
    def aprobado(self):
        if self.nota > 4:
            print("El alumno {} aprobo con una nota de {}".format(self.nombre, self.nota))
        else:
            print("El alumno {} desaprobo con una nota de {}".format(self.nombre, self.nota))

nombre =  input("Ingresa el nombre del alumno: ")
nota = float(input("Ingresa la nota del alumno {}: ".format(nombre)))

while nota != -1:
    alumno = Estudiante(nombre, nota)
    alumno.aprobado()
    nombre =  input("Ingresa el nombre del alumno: ")
    nota = float(input("Ingresa la nota del alumno {} o ingrese -1 para salir: ").format(nombre))