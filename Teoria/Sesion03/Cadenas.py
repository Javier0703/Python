# CADENAS DE CARACTERES I

# Logintitud: Medir su longiud
print(len("cadena")) # 6

# Comparación (cuidado con mayúsculas y minúsculas)
# Con .lower() lo transforma en minusculas, y .upper() en mayusculas
print("cadena" == "cadena") # True
print("cadena" != "Cadena") # True
print("CADENA".lower() == "cadena".upper()) # False

# División de elementos
a = "AMPLI 451 PARAD 729"
b = a.split(' ') 
# El Split es un delimitador, puede ser cualquier elemento
print(b) # ['AMPLI', '451', 'PARAD', '729'])


# CADENAS DE CARACTERES II

# Búsqueda de elementos
# find() devuelve -1 si no encuentra, index() devuelve una excepción
print("cadena".find('e')) # 3
print("cadena".find('una')) # -1
print('i' in "cadena") # False

# Con index hay que trabajar con excepciones
# La ideal es el ValueError, pero podemos trabajar con Exception
try:
    print("cadena".index('45'))

except ValueError:
    print("Subcadena no encontrada")

# Acceso a las cadenas
print("cadenas"[0]) #c
print("cadenas"[-1]) #s
print("cadenas"[-2]) #a
#Concatenación
print("cadena" + "s largas") # cadenas largas

# CADENAS DE CARACTERES III

# Slicing (subcadenas)
print("cadena"[0:]) # cadena
print("cadena"[:-2]) # cade
print("cadena"[2:-2]) # de
#Basicamente los puntos indican hasta donde queremos llegar o de donde partimos
#Si les ponemos despues X: --> Desde X en adelante
#Si les ponemos antes :X --> Desde el inicio hasta donde queramos
#Si les ponemos entre dos numeros X:Y desde X hasta Y

# Empieza:Acaba-1:Número_saltos
print("cadena muy larga"[2:-2:3]) # daul

# Reemplazamiento
# Devuelve una copia, porque String es inmutable
print("cadena larga".replace("a", "W", 3)) # cWdenW lWrga
# Conteo
print("cabeza".count('a')) # 2

# CADENAS DE CARACTERES IV
# Última ocurrencia de un caracter (fórmula)
cadena = "Paradigmas es un grupo ejemplar"
print(len(cadena)) #31
print(cadena[::-1]) #ralpmeje opurg nu se samgidaraP
#Con ::-1 Da la vuelta al string

#lastIndexOf de Java en Python -->
#Queremos saber el lastIndexOf de una e:
l = cadena[::-1].find('e')
#A ello le restas del tamaño, la l y el 1 (porque empieza desde el 0)
print(len(cadena) - l - 1) #25

# Eliminación de todos los espacios al inicio y fin
print(' Hello    '.strip()) # Hello
# Comienzo/fin por
print("Casa del campo".startswith("Casa")) # True
print("Casa del campo".endswith("ampa")) # False

# CADENA DE CARACTERES VI

# Unión de elementos
a = ['this', 'is', 'a', 'string']
print("-".join(a)) # this-is-a-string
# Repetición de elementos
a = '^'
print(a * 45) # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#Piramide
for i in range(1,10):
    print(a*i)

# CADENA DE CARACTERES VI
# 15. Expresiones regulares (subcadenas con cierta forma)
#Libreria necesaria
import re
# Coincide con una letra ‘a’, seguida de al menos (+) 1 dígito entre 2 y 6 [2-6]
patron = re.compile('a[2-6]+')
print(patron)
cadena = 'ba3425 a6' # La coincidencia del patrón no está al principio!

# findall() devuelve todas las ocurrencias en forma de lista
print(patron.findall(cadena) ) # ['a3425', 'a6']

# search() busca en la cadena alguna ocurrencia del patrón

print(patron.search(cadena)) # <_sre.SRE_Match object at 0x0311C3D8>
# match() igual que search() pero coincidencia sólo al comienzo de la cadena
print(patron.match(cadena)) # None

