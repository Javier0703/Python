#Trabajo con ficheros en Python

#Se pone 1 -> Archivo.  2 -> Modo.  3-> Tamaño(Opcional)
#Modos que hay: 'r' (lectura) 'w' (escritura) 'a' (añadir) 'b' (binario) 
#'+' (lectura/escritura)
#Se pueden combinar 'wab' por ejemplo

#Archivo a utilizar (Cuidado con el directorio donde estemos que afecta)
arc = 'prueba.txt'

#MODO LECTURA

#Apertura de un fichero en modo lectura
f = open(arc, 'r')

#Leer todas las lineas generando una lista
print(f.readlines())

#Escribe una a una con print
print(f.read())

#Lee una linea
print(f.readline())

#Cerrar el arhivo. IMPORTANTE HACERLO SIEMPRE
f.close()


#MODO ESCRITURA
f = open(arc,'w')

#Escribir una linea (BORRA LO QUE HAY Y COLOCA LO QUE TIENES)
f.write("Prueba escritura desde Python")

a = "\nPrueba 2"
b = "\nPrueba 3"

#No borra lo anterior (RECOMENDABLE) Podemos agregar todas las lineas que queramos en una Lista
#Lo guarda seguido. Recomendable escribir un \n para cada linea
f.writelines([a,b])

#Guardado (Recomendado)
f.flush()
f.close()