#Ejercicios de la Sesion 2
import math

"""
1- La letra del DNI puede calcularse a partir del número. Para ello sólo hay que dividir el número por 23 y quedarse
con el resto. La letra correspondiente se obtiene de la siguiente tabla:
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
T R W A G M Y F P D X B N J Z S Q V H L C K E
Construya un programa que lea un número de DNI y muestre por pantalla la letra correspondiente.
"""
#Creamos la lista
lista = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
dni = input("Dime tu DNI para calcular la letra: ")
if dni.isdigit() and len(dni)==8:
    print("La letra correspondiente es",lista[int(dni)%23])
else:
    print("DNI no válido")

"""
2.En el juego NIM dos jugadores están delante de una pila de 50 piedras. En cada turno, el jugador puede coger
entre 1 y 5 piedras (suponiendo que queden piedras en la pila). El jugador que retire la última piedra gana.
Elabore un programa en Python para que dos jugadores puedan jugar al Nim
"""
#Juego Nim
piedras = 50
player = 1
min = 1
max = 5
while piedras>0:
    print("Turno J" + str(player) + ".", piedras , " piedras restantes. Elija entre", min , "y" , max)
    l = input("Seleccion: ")
    l = int(l)
    if l>=min and l<=max and l<=piedras:
        piedras = piedras - l
        if piedras == 0:
            print("Enhorabuena, has ganado J" + str(player))
            break
        player = 2 if player == 1 else 1       
    else:
        print ("Numero de piedras introducidas no valido")        

""""
3.Modifique el programa anterior de manera que el número de piedras inicial y el máximo de piedras que puede
coger un jugador en un turno se indiquen al empezar el juego.
"""
piedras = int(input("Seleccione el numero de piedras para jugar: "))
max = int(input("Seleccione el numero máximo de piedras por turno: "))
min = 1
player = 1
while piedras>0:
    print("Turno J" + str(player) + ".", piedras , " piedras restantes. Elija entre", min , "y" , max)
    l = input("Seleccion: ")
    l = int(l)
    if l>=min and l<=max and l<=piedras:
        piedras = piedras - l
        if piedras == 0:
            print("Enhorabuena, has ganado J" + str(player))
            break
        player = 2 if player == 1 else 1       
    else:
        print ("Numero de piedras introducidas no valido") 

"""
4. Un número primo es un número natural que tiene exactamente dos divisores distintos: 
él mismo y el 1. Construya una función que reciba un número y devuelva True si es un número primo
y False si no lo es. Usandoesa función construya un programa que muestre por 
pantalla los números primos comprendidos entre 1 y 100.
"""

def numPrimo(num):
    cent = 0
    for i in range(1, num + 1):
        if num % i == 0:
            cent += 1
    return True if cent == 2 and num!=2 else False

for i in range(1,100):
    if numPrimo(i):
        print(i, "es primo")

"""
5. Una cadena es palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda. 
Escriba una función que reciba una cadena como parámetro y que devuelva True si es un palíndromo 
y False si no lo es. Usando esa función construya un programa que lea un cadena e indique si es o
no palíndromo."""

c = str(input("Cadena para comprobar si es palindromico: ")).replace(" ", "")
for i in range (0,math.ceil(len(c)/2)):
    if c[i] != c[len(c) - (i+1)]:
        print("No es palindromica")
        break
else:
    print("Es palindromica") 

"""
6. Elabore las siguientes funciones:
    Una función que reciba una lista de números y calcule la media.
    Una función que reciba una lista de números y calcule el máximo.
    Una función que reciba una lista de números y calcule el mínimo.
Construya un programa que lea un número n, y a continuación lea n números y los guarde en una lista. 
El programa debe mostrar por pantalla la media, el máximo y el mínimo de los números leídos.
"""

num = int(input("Cancidad de numeros a comparar: "))
l = []
for i in range(1,num+1):
    a = input("Escriba el numero: ")
    l.append(int(a))

def calcMedia (*nums):
    c = 0
    for num in nums:
        c += num
    return c/len(nums)  

def calcMax(*nums):
    if not nums: 
        return None
    maximo = nums[0]
    for num in nums:
        if num > maximo:
            maximo = num
    return maximo

def calcMin (*nums):
    if not nums: 
        return None
    maximo = nums[0]
    for num in nums:
        if num < maximo:
            maximo = num
    return maximo   

print("Media de los numeros:",calcMedia(*l), "Maximo", calcMax(*l), "Minimo", calcMin(*l))

""""
7.Escriba un programa que lea una matriz 5 * 5 de enteros e imprima por pantalla la media aritmética de cada fila
y la media aritmética de cada columna
"""

#Definir tamaño de la matriz
matriz = [[1,3,5,6,7],[5,3,6,0,8],[2,5,8,1,3],[4,5,6,7,2],[9,0,0,3,2]]

for i in range(0,len(matriz)):
    print("Fila", i+1,"-->", calcMedia(*matriz[i]))
    l=[]
    for j in range(0, len(matriz)):
        l.append(matriz[j][i])
    print("Columna", i+1, "-->", calcMedia(*l))

"""
8.Diseñe una función que reciba dos listas y devuelva una lista con los elementos comunes a ambas, sin repetir
ninguno.
Ejemplo: si se recibe [1, 2, 1] y [2, 3, 2, 4] devolverá [2].
"""
lista = [[1,2,3,4,56,7,83,3,213,4,543],[1,2,4,6,733,5,4,65,7,876,3,1]]
def compareElementList(*lista):
    c = []
    for i in range(0,len(lista[0])):
        if lista[0][i] in lista[1]:
            if lista[0][i] not in c:
                c.append(lista[0][i])
    return c
print(compareElementList(*lista))

""""
9.Elabore un programa que cuente el número de líneas, palabras y caracteres de un fichero introducido como
argumento.
"""
archivo = r"Ejercicios\Sesion02\texto.txt"
mode = "r"

try:
    f = open(archivo,mode)
    l = f.readlines()
    palabras= 0
    caracteres= 0
    print("Numero de lineas:", len(l))
    for line in l:
        j = line.split()
        palabras += len(j)
        for palabra in j:
            caracteres += len(palabra)
    print("Palabras:", palabras,"\nCaracteres", caracteres)

except FileNotFoundError:
    print("Error de archivo")
