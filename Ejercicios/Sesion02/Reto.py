#Ejercicio de Reto

fichero = r"Ejercicios\Sesion02\reto.txt"
mode = 'r'

try:

    f = open(fichero, mode)
    fichero = f.readlines()

    def reto(fichero,as1,as2):
        cent = 0
        as1List = []
        asign = []
        for linea in fichero:
            #Eliminamos el \n de cada elemento
            l = linea.strip().split(' ')
            if l[0] not in asign:
                asign.append(l[0])
            #Comprobamos si esa asignatura
            if l[0] == as1:
                as1List.append(l[1])   
        for linea in fichero:
            l = linea.strip().split(' ')
            if l[0] == as2:
                if l[1] in as1List:
                    cent += 1
        return cent,asign

    #Eleccion de 2 Asignaturas
    print("Elige dos asignaturas: ")
    a1 = input("Primera: ")
    a2 = input("SEgunda: ")

    #Comprobacion de las asignaturas
    l = reto(fichero, a1.upper(), a2.upper())
    if a1.upper() in l[1] and a2.upper() in l[1]:
        print("Total alumnos:", l[0])
    else:
        print("Las asignaturas no son correctas")

except FileNotFoundError:
    print("Fichero no encontrado")