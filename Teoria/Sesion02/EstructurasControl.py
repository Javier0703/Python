#Estructuras de Control

#ESTRUCTURA DE CONTROL I

#TIPS: 
#Usar una de las dos: Tabulaciones o Espacios y aplicarlo siempre
#Dos puntos : para todas las estructuras, condicionales, bucles...

#ESTRUCTURA DE CONTROL II

#CONDICIONALES
print("CONDICIONALES")

#Hay dos versiones, la normal, y el ternario.

#NORMAL: tiene esta estructura:

a = input("Numero cualquiera: ")
if a == "1":
    print("Es un uno")
elif a == "2":
    print("Es un dos")
else:
    print("No es ni 1 ni 2")    

#Es de la forma if elif y else.
    
#TERNARIA: Estructura lineal:
    
a = input("\nNumero del 1 al 100: ")
#Suponiendo que lo hemos verificado
result = "Numero menor de 50" if a < "50" else "Numero mayor a 50"
print(result)


#ESTRUCTURA DE CONTROL III

#BUCLE WHILE: (Contador del 1 al 10) En Python no hay i++.
i = 0
while i<10:
    i += 1
    print(i)

#BUCLE DO-WHILE: No existe como tal pero se puede generar
i = 0
while True:
    i += 1
    print(i) 
    if (i == 10):
        break

#FOR: Recorridos de Listas, diccionarios, bucles algo mas diversos
paises = ["Alemania", "Austria", "Bélgica", "Bulgaria", "Chipre", "Croacia", "Dinamarca", "Eslovaquia", "Eslovenia", "España"]
for pais in paises:
    print(pais)

#ESTRUCTURAS DE CONTROL IV
    
#BUCLE FOR con la funcion range (num coge el valor desde 2 al 10)   
#Uso de continue para que salte a la siguiente iteracion
for num in range(2, 10):
    if num % 2 == 0:
        print("Encontrado número par", num)
        continue #Salta a la siguiente iteración
    print("Encontrado número impar", num)

#UNA COSA IMPORTANTE, SI USAMOS UN ELSE EN UN BUCLE, SE EJECUTARA SI NO SE TERMINA CON UN BREAK

#En este caso al variar la k podemos ver si el else lo imprime o no
k = 3 #Si esta dentro del bucle, este se rompera
i= 0
while i<10:
    if(i == k):
        break
    i += 1
else:
    print("No hemos encontrado un 3")


#ESTRUCTURAS DE CONTROL V

#EXCEPCIONES
#En Pthon se trabaja tambien con excepciones, como era normal. Esta tiene una estructura
#Parecida a la de todos los lenguajes. Try-Catch

#Un ejemplo puede ser
try:
    # Código donde puede ocurrir una excepción
    numero = int(input("Introduce un número entero: "))
    resultado = 10 / numero
    print("El resultado es:", resultado)

except ZeroDivisionError:
    # Manejo de la excepción cuando se intenta dividir por cero
    print("¡Error! No se puede dividir por cero.")

except ValueError:
    # Manejo de la excepción cuando la entrada no es un número entero
    print("¡Error! Debes introducir un número entero.")

except Exception as e:
    # Manejo de otras excepciones no especificadas anteriormente
    print("¡Error inesperado!", e)

#Como vemos puede haber excepciones muy generales y otras my específicas
    
#En el If tambien podemos generar Excepciones
valor = int(input("Introduce un número: "))

if valor < 0:
    raise Exception("El número no puede ser negativo")
else:
    print("El número introducido es:", valor)