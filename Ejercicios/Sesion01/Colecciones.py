#Ejercicios de Colecciones (Listas, Tuplas, Diccionarios y Conjuntos)

a = [1,2,3,4,5,6]
"""
2. Dada la lista a=[1, 2, 3, 4, 5, 6], indique la expresión para obtener las siguientes listas partiendo de
la lista a y utilizando el operador [i:j]
a) [1, 2]
b) [2, 3, 4]
c) [4, 5, 6]
"""

#a
print (a[0:2])

#b
print (a[1:4])

#c
#Peor modo
print (a[3:6])
#Los ultimos 3 digitos
print (a[-3:])


"""
3.- Indique cuáles son las listas generadas usando la función range():
a) a=range(10)
b) b=range(1,10)
c) c=range(1,10,2)
"""

#a
a=range(10)
#Genera una lista de enteros del 0 al 9 (0,1,2,3,4,5..9)

#b
b=range(1,10)
#Genera una lista de enteros del 1 al 9 (1,2,3,4,5..9)

#c
c=range(1,10,2)
#Genera una lista de enteros del 1 al 9 con salto de 2 (1,3,5,7,9)

"""
4. Partiendo de las listas a, b, c del apartado anterior, indique qué se obtiene con las siguientes expresiones:
a) len(a)
b) len(b)
c) len(c)
d) a+b
e) c*3
"""

#a
print(len(a))
#La longitud de a (10, porque es del 0-9)

#b
print(len(b))
#La longitud de b (9, porque es del 1-9)

#c
print(len(c))
#La longitud de c (5, porque es del 1-9, con saltos de dos (los impares del 1 al 9))

#d --> print(a+b)
#Sacara un eror, porque estamos trabajando con rangos, no aceptan operaciones básicas (+ - * /)

#e --> print(c*3)
#Lo mismo, otro error

"""
5.- Se puede definir una matriz como mat= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a) ¿Cómo accedería al elemento (1, 2)?
b) ¿Cómo obtendría la primera fila?
"""
mat= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#a Supongamos que elemento 1 es el primer elemento y no el elemento 1 de la matriz (mat[1])
print([mat[0][1]])

#b
print(mat[0])

""""
6. Represente la siguiente matriz en Python:
                4 1 5
                3 2 4
                9 0 1
"""

mat = [[4,1,5],[3,2,4],[9,0,1]]

#Imprimir la matriz puesta con un bucle
for i in range(len(mat)):
    print (mat[i])


"""
7.- Partiendo de un diccionario vacío mundial={} inserte los siguientes elementos:
Spain - 12
Netherlands - 11
Italy - 10
Germany - 8
France - 6
Portugal - 5
"""
mundial={}
mundial["Spain"] = 12
mundial["Netherlands"] = 11
mundial["Italy"] = 10 
mundial["Germany"] = 8
mundial["France"] = 6
mundial["Portugal"] = 5


"""
8. Sobre el diccionario del apartado anterior:
a) Imprima el diccionario con la sentencia print
b) Obtenga el valor de la clave Spain.
c) Obtenga el valor de la clave Portugal.
d) Incremente el valor de Spain en 3.
e) Decremente el valor de France en 2
"""

#a
print(mundial)
print(mundial["Spain"])
print(mundial["Portugal"])
mundial["Spain"] = mundial["Spain"] + 3
mundial["France"] = mundial["France"] -2

"""
9.A partir del diccionario inventario= {’manzanas’: 430, ’bananas’: 312,
’naranjas’: 525, ’peras’: 217}
a) Incremente las manzanas en 20.
b) Decremente las peras en 110.
"""
inventario= {"manzanas": 430, "bananas": 312, "naranjas": 525, "peras": 217}
#a
inventario["manzanas"] = inventario["manzanas"] + 20

#b
inventario["peras"] = inventario["peras"] -110

del(a,b,c,i, mat, mundial, inventario)



