#Metodos en Python

#Informacion acerca de ellos
#No se declara el tipo devuelto ni el de los argumentos.
#Podemos devolver tipos complejos (listas, tuplas, …).
#Argumentos mutables se comportan como paso por referencia
    #Cuidado, con el =, ya que los parametros pueden verse afectados
#Argumentos inmutables: paso por valor (copia). i.e.: tuplas

def modificar(num):
    num += 20

a = 50
print (a)
a = modificar(a)    
print(a)

#Si no asignas un return o un print, este cojera el valor de None

#Metodos que lista los numeros del 1 al numero introducido
def listarNum(num):
    for i in range(1,num+1):
        print(i)

a = input("Numero entero: ")
listarNum(int(a))

#Metodos arbitrarias. Podemos crear una metodos con "parametros infinitos"
# Tiene esta forma: def metodo('Fijo','Var1','Var2','Var3'...)


def metInfit(p,*lista):
    print(p)
    for atr in lista:
        print(atr)

p = "Variable fija"
paisesTupla = ("Estados Unidos", "Canadá", "México", "Brasil", "Argentina")
paisesLista= ["Japón", "Francia", "Alemania", "Italia", "España"]

#Dos formas de utilizar este metodo

metInfit(p,*paisesTupla)
metInfit(p,*paisesLista)
metInfit(p,'España','Francia','Italia')

#Es decir, podemos introducir una lista/tupla dentro de ella o colocarlos directamente

