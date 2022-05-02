#Estructuras de Datos
#Diccionarios

diccionario = {'Usuario' : 'wcoto' , 'Password' : 123456}
print(diccionario)

#Elementos de un diccionario
diccionario = {'Nombre' : "Walter" , "Apellido" : "White" , "Estatura" : 1.8}
print(diccionario)

#Solo claves
print(diccionario.keys())
#Solo valores
print(diccionario.values())

#El valor de una clave en especifico
print(diccionario["Estatura"])

diccionario["Peso"] = "58 kg"
print(diccionario)

diccionario["Nombre"] = "El Walter"
print(diccionario)

#--------------------------------------
diccionario = { "uno" : 2, "dos" : 3, "tres" : 4 }
diccionarioDos = {"cuatro" : 5 , "cinco" : 6 , "seis" : 7}
print(diccionario)

#Aca el metodo pop va a recibir una clave y va a eliminarla
diccionario.pop("tres")
print(diccionario)

#get va a recibir un parametro que es la llave
print(diccionario.get("dos"))

#SetDefault, va a recibir el valor y la clave para setear un nuevo elemento en el diccionario
diccionario.setdefault("cuatro" , 5)
print(diccionario)

#Update sirve para combinar dos diccionarios, actualizando el diccionario original
#En caso de existir una clave repetida, se mantendra una sola
diccionario.update(diccionarioDos)
print(diccionario)

#Copy sirve para copiar un diccionario
diccionario3 = diccionario.copy()
print(diccionario, diccionario3)

#Clear vacia el diccionario
diccionario.clear()
print(diccionario)



