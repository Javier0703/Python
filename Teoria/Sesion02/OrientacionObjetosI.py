#Orientacion a Objetos en Python

#Creacion de una Clase básica

#Creacion de la Clase
class Coche:
    modelo = ""
    matricula = ""
    cv = 0

#Creacion de un Objeto (Laguna)
#Aqui decimos que coche sea 
coche = Coche()
coche.modelo = "Laguna"
coche.matricula = "2350 JKL"
coche.cv = 150

print(coche.cv)

#Esta no es la mejor manera de crear una clase en Python. Debe ser atribuyendo el self (__init__)

#Ahora creamos una que es la que se suele usar y es la recomendable.
class Persona():
    #Clase Persona que contiene parametros como altura,edad y profesion
    #Contiene funciones para cambiar estos parametros y para imprimirlo por pantalla
    def __init__(self):
        self.__altura = 0
        self.__edad = 0
        self.__profesion = ""
        return None
    
    def setAltura(self,alt):
        if alt<0 or alt>260:
            print("Altura Invalida (0 -260 cm)")
        else:
            self.__altura = alt 
            return None 

    def setEdad(self,edad):
        if edad<0 or edad>130:
            print("Rango de edad invalido (0 - 130)")
        else:
            self.__edad = edad
            return None
    
    def setProfesion(self,profesion):
        self.__profesion = profesion
        return None
    
    def getAtributes(self):
        return self.__altura, self.__profesion, self.__edad

#Hemos generado una clase mas completa donde podemos modificarle las cosas.
#La clase por tiene valores por defecto, asi a la hora de crear un objeto debemos de modificarle
    #los atributos que tiene
        
#Creacion de un objeto
Javier = Persona()

#Uso de una funcion dentro de el
print(Javier.getAtributes())
#Como vemos lo devuelve en una tupla, por lo que podemos devolverlo mas formal con un bucle..

#Asignacion de atributos
#Atributo valido
edad = input("Dime la edad de Javier: ")
Javier.setEdad(int(edad))

#Atributo invalido
edad = input("Dime la edad de Javier: ")
Javier.setEdad(int(edad))


