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