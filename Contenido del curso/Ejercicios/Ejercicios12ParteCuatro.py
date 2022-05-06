'''Crear una clase llamada Marino(), con un metodo que sea hablar, 
en donde muestre un mensaje que diga "Hola...". Luego, crear una clase Pulpo() que herede Marino, 
pero modificar el mensaje de hablar por "Soy un Pulpo". Por ultimo, crear una clase Foca(), 
heredada de Marino, pero que tenga un atributo nuevo llamado mensaje y que muestre ese mesjae como parametro'''

class Marino():
    def Hablar(self):
        return "Hola..."

class Pulpo(Marino):
    def Hablar(self):
        return "Soy un Pulpo"

class Foca(Marino):
    def Hablar(self, message):
        return message

mari = Marino()
print(mari.Hablar())
pulp = Pulpo()
print(pulp.Hablar())
foca = Foca()
print(foca.Hablar("Hola Juan Carlos"))