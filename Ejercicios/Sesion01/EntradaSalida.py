#Ejercicios de Entrada y Salida de Datos
import math

def tipo_numero(entrada):
    if entrada.isdigit():
        return 1
    elif entrada.count('.') == 1 and all(caracter.isdigit() or caracter == '.' for caracter in entrada):
        return 2
    else:
        return 3
    
def transformar_numero(v, num):
    if v == 1:
        num = int(num)
        return num
    elif v == 2:
        num = float(num)
        return num

"""
10. Elabore un programa que lea una hora expresada en segundos transcurridos desde las 12 de la noche y muestre
por pantalla el equivalente en horas, minutos y segundos.
"""

a = input("Escribe los segundos (enteros): ")
v = tipo_numero(a)
if v == 1 or v == 2:
    a = transformar_numero(v,a)
    print(a//3600,"h ", (a%3600)//60,"m ", a % 60,"s")   
else:
    print("No es un numero") 

"""
11. Construya un programa que pida al usuario su nombre, sus apellidos y su fecha de nacimiento. A continuación
tiene que mostrar los datos por pantalla formateados como en el siguiente ejemplo:
Nombre: Fernando
Primer apellido: Alonso
Segundo apellido: Díaz
Fecha de nacimiento
Día: 29
Mes: julio
Año: 1981
Fernando Alonso Díaz nació el 29 de julio de 1981.
"""

n = input("Nombre: ")
pa = input("Primer apellido: ")
sa = input("Segundo apellico: ")
d = input("Fecha de nacimiento\n Dia: ")
m = input(" Mes: ")
a = input(" Año: ")
print (n,pa,sa,"nacio el",d,"de",m,"de",a)

"""
12.- Elabore un programa que lea el radio de un círculo e imprima por pantalla el área del mismo (recuerde que el
área es πr2).
Nota: el valor de π se obtiene con math.pi, incluyendo import math al inicio del programa.
"""

r = input("Racio de la circunferencia: ")
v = tipo_numero(r)
if v == 1 or v == 2:
    r = transformar_numero(v,r)
    print("Area del circulo:", math.pi*(r**2))   
else:
    print("No es un numero")

    
"""
13. Construya un programa que lea el valor de un producto sin IVA y muestre por pantalla el valor del producto con
IVA (18 %).
"""

r = input("Precio sin IVA: ")
v = tipo_numero(r)
if v == 1 or v == 2:
    r = transformar_numero(v,r)
    print("Precio con IVA", r + (r*0.18),"€")   
else:
    print("No es un numero")

"""
Elabore un programa que lea el valor de x y que evalúe el polinomio 
x4 + x3 + 2x2 − x.
"""
x = input("Valor de la x: ")
v = tipo_numero(x)
if v == 1 or v == 2:
    x = transformar_numero(v,x)
    print("Valor de X:", x, "En X^4 + x^3 + 2x^2 -x:")   
    print("X =",x**4 + x**3 + 2*(x**2) - x)
else:
    print("No es un numero")

"""
15. Construya un programa que pida el valor de los dos lados de un rectángulo y muestre el valor de su perímetro
y de su área.
"""

b = input("Valor de la base: ")
a = input("Valor de la altura: ")
ba = tipo_numero(b)
al = tipo_numero(a)
if (ba == 1 or ba == 2) and (al == 1 or al == 2):
    b = transformar_numero(ba,b)
    a = transformar_numero(al,a)
    print ("Perimetro:",a*2 + b*2)
    print ("Area:", a*b)
   
else:
    print("No es un numero")

