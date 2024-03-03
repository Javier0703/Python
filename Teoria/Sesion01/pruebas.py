#Importacion de librerias (hacerlo siempre arriba si es posible)
import math

#Pruebas básicas de funcionamiento de variables, prints, transofmacion de tipos...
#Prints y variables
print ("Hola mundo")
a=4
print (a)
cadena="hola mundo"
print (cadena, "hola mundo")

#Division normal (decimales) o redondeada
print (a*a/3)
print (a*a//3)

#Transformar en mayusculas o minusculas
print (cadena.upper())
print (cadena.lower)

#Octal (0oXXX) y Hexadecimal (0xXXX)
#Octal
o1 =0x564; hex2 = 0xFA3CB4
print (o1, hex2)

#Transformar de String <=> Int
a="123"
print(123 + int(a))
print (a+str(123))

#Suma de entero y flotante
a=2.45
print(a+5)


#NUMEROS COMPLEJOS
a=2+4j
print(a*5+3j)
print(a*459)

#Exponencial y modulo (resto)
print(4**3)
print(456.44543%56)

#5 OR 2 EN BINARIO
print(5&2)
#5 AND 2 EN BINARIO
print(5 | 2)
#5 XOR 2 EN BINARIO
print (5^2)
#complemento del bit. 5 = 0000 0101 -> 1111 1010
print(~5)
#t = tab n = salto de linea
a="\tHOLA\nHOLA"
print (a)
print ("A es de tipo" , type(a))

#Lo que esta usando Python en este momento 
print (dir())

#Deshacer variable
del (a)

#Si usamos barra baja, _ se refiere al ultimo resultado (Modo interactivo)

#Para usar el tipo math., necesitamos importar librerias:
print (math.sqrt(16))
print (math.exp(0))

# Hay veces que hay que poner l /usr/bin/python para decirle al S.O que tipo de archivo va a tratar

#el end="" sirve para decir que no haga salto de linea
print("Hola","Mundo",end="")
print("Hola")

#Si queremos imprimir comillas, hacemos el print con comilla simple '...':
print('Hola "Que tal"')