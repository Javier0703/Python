#Listas
lista = [1,2,3,4]
print (lista)
print (type(lista))
print (lista[0], lista[3])

#Si es negativo, recorre dese el ultimo hasta el primero
print (lista[-1])

#Modificar un array
lista[3] = 77
print(lista)

#Si no tiene ese tamaño, devuelve error
# Error --> list[6]=1  list[6] no esta en el rango

#Añadir al final y eliminar (da igual donde este ese elemento) 
lista.append(6)
lista.append(3)
print(lista)
#El remove elimina el pirer elemento que vea igual que el
lista.remove(77)
lista.remove(3)
print(lista)
#Sacar los elementos desde el x hasta el y, donce el x pertenece y el y no
print (lista[2:3])
#Podeos darle orden
print (lista[2::-1])

#Las listas pueden contener todo tipo de valores
lista = [1,"Dos", "Tres", '4', 5, 6, [1,2,3]]
print (lista)
#Modificar el valor de una lista detro de una lista
lista[6][1]=4
print(lista)

#TUPLAS
print("\n\nTuplas")
tupla = (1,2,3,4,5)
print (tupla)
print (type(tupla))
#Acceder al valor de una tupla
print (tupla[2])
#Podemos meter una lista dentro de una tipla
tupla = (1,2,3,[4,5,6],7)
#Podemos modificar el valor de esa lista, pero no eliminarla
tupla[3][1]=34
print (tupla)


#DICCIONARIO
print("\n\nDiccionario")
d={}
print(d)
#Asociar en el diccionario
d["Juan"] = "Valladolid"
d["Javier"] = "Palencia"
print (d)
#Podemos preguntar el valor de una clave
print(d["Javier"])
print (type(d))

#CONJUNOS
print("\n\CONJUNTOS")
#Basicamte el conjunto te saca las claves, donde puedes bucar y filtrar si existe esa clave
a = set(d)
print(a)
#Busqueda de una clave en un conjunto
print('Juan' in a)

print ("SALIDA Y ENTRADA DE DATOS")
print ("Hola %s de nuevo" % "Prueba")

#Lee la cadena (Un solo caracter (no vale la ñ))
a= input()
print(a)

