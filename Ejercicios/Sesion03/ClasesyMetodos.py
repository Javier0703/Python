#Ejercicios de Clases y Métodos
"""
1.- Desarrolle una clase Cafetera con atributos capacidad_maxima (la cantidad máxima de café 
que puede contener la cafetera) y cantidad_actual (la cantidad actual de café que hay en la 
cafetera). Implemente, al menos, los siguientes métodos:
    - Constructor: establece la capacidad máxima y la cantidad actual.
    - llenar_cafetera: hace que la cantidad actual sea igual a la capacidad máxima.
    - servir_taza: simula la acción de servir una taza con la cantidad indicada como parámetro. 
    Si la cantidad actual de café no alcanza para llenar la taza, se sirve lo que quede.
    - vaciar_cafetera: pone la cantidad de café actual en cero.
    - agregar_cafe: añade a la cafetera la cantidad de café indicada como parámetro.
Construya un programa que cree un objeto Cafetera y pruebe todos sus métodos.
"""
class Cafeteria():
    def __init__(self,cap_max,cant_actual):
        self.cap_max = cap_max
        self.cant_actual = cant_actual

    def llenar_cafetera(self):
        self.cant_actual = self.cap_max
    
    def servir_taza(self,cant):
        cant = int(cant)
        if cant>=0:
            if cant<self.cant_actual:
                print("Se sirven", cant ,"ml de cafe")
                self.cant_actual -= cant
            else:
                print("No queda tanto cafe, servimos lo que queda,", self.cant_actual)
                self.cant_actual = 0
        else:
            print("La cantidad debe ser positiva")

    def vaciar_cafetera(self):
        self.cant_actual = 0
    
    def agregar_cafe(self,cant):
        cafeRestante= self.cap_max - self.cant_actual
        if cant>cafeRestante:
            print("No cabe tanto cafe, se llena la cafetera con", cafeRestante,"ml")
            self.cant_actual = self.cap_max
        else:
            self.cant_actual += cant
            print("Agregamos a la cafetera", cant,"ml de cafe")

#Objeto con capacidad maxima y cantidad actual de cafe respectivamente
primeraCafetera = Cafeteria(1000,500)

#Cantidad maxima y actual
print(primeraCafetera.cap_max, primeraCafetera.cant_actual)

#Llenamos la cafetera
primeraCafetera.llenar_cafetera()
print(primeraCafetera.cant_actual)

#Servimos taza
primeraCafetera.servir_taza(500)
print(primeraCafetera.cant_actual)  
#Servimos mas cafe de lo que hay
primeraCafetera.servir_taza(700)
print(primeraCafetera.cant_actual)

#Agregamos la cafetera con una cantidad
primeraCafetera.agregar_cafe(300)
print(primeraCafetera.cant_actual)
#Agregamos mas de lo que entra
primeraCafetera.agregar_cafe(1100)
print(primeraCafetera.cant_actual)

#Vaciamos la cafetera
primeraCafetera.vaciar_cafetera()
print(primeraCafetera.cant_actual)

"""
2. Cree una clase Termometro que almacene una temperatura. La temperatura interna se almacenará 
siempre en grados Kelvin y la clase tendrá un constructor al que se pasará la temperatura inicial
en grados Kelvin. El termómetro debe proporcionar métodos de lectura y escritura de su valor de 
temperatura interna. Los métodos de lectura serán get_kelvin, get_celsius y get_fahrenheit que 
devolverán la temperatura en la escala que se le indica. Los métodos de escritura serán set_kelvin,
set_celsius y set_fahrenheit. Cree también un método que permita comparar dos objetos de la clase 
Termometro. Para la conversión de temperaturas se utilizarán las fórmulas siguientes:
    - C = K − 273,15
    - K = C + 273,15
    - F = 9/5 × K − 459,67
    - K = (F + 459,67) ×5/9
siendo K grados Kelvin, C grados Celsius y F grafos Fahrenheit.
Construya un programa que cree varios objetos de la clase Termometro y pruebe todos sus métodos.
"""

class Termometro():
    def __init__ (self, kelvin):
        self.kelvin = kelvin

    def getKelvin(self):
        return round(self.kelvin,2)
    
    def getCelsius(self):
        c = self.kelvin - 273.15
        return round(c,2)
    
    def getFahrenheit(self):
        f = (9/5) * self.kelvin - 459.67
        return round(f,2)
    
    def setKelvin(self, temp):
        if temp>=0:
            self.kelvin = temp
            print("Temperatura en Kelvin modificada")
        else:
            print("Temperatura en Kelvin inválida")

    def setCelsius(self,temp):
        if temp>=-273.15:
            self.kelvin = temp + 273.15
            print("Temperatura en Celsius modificada")
        else:
            print("Temperatura en Celsius inválida")

    def setFahrenheit(self,temp):
        if temp>=-459.67:
            self.kelvin = (temp + 459.67) * (5/9)
            print("Temperatura en Fahrenheit modificada")
        else:
            print("Temperatura en Fahrenheit inválida")

temp1 = Termometro(300)
temp1.setFahrenheit(200)
print(temp1.getKelvin(), temp1.getCelsius(), temp1.getFahrenheit())
#Temperatura invalida
temp1.setCelsius(-500)


def compareTemps(t1,t2):
    if t1>t2:
        return "Temperatura mayor la primera, "+str(t1)
    elif t1<t2:
        return "Temperatura mayor la primera, "+str(t2)
    else:
        return "Temperaturas iguales, "+str(t1)
    
temp2 = Termometro(400)
l = compareTemps(temp1.getKelvin(),temp2.getKelvin())
print (l)  

"""
3.- Escriba una clase Reloj que simule el comportamiento de un cronómetro digital. 
Se deben implementar los siguientes métodos:
    - puesta_a_cero: pone a cero el cronómetro.
    - incremento: incrementa el cronómetro en 1 segundo.
    - imprime: imprime el valor del cronómetro por pantalla.
Cuando el contador llegue a 23:59:59 y reciba el mensaje de incremento deberá pasar a 00:00:00.
Construya un programa que cree un objeto Cronometro y pruebe todos sus métodos.
"""

class Reloj():
    def __init__(self, h,m,s):
        self.h = h%24 if h>=24 else h
        self.m = m%60 if m>=60 else m
        self.s = s%60 if s>=60 else s
    
    def puestaCero(self):
        self.h = self.m = self.s = 0
    
    def incremento(self):
        self.s +=1
        if self.s >= 60:
            self.s = 0
            self.m +=1
        if self.m >= 60:
            self.m =0
            self.h +=1
        if self.h >= 24:
            self.h = 0

    def imprimirHora(self):
        h = self.h
        if h<10:
            h = "0"+str(h)
        m = self.m
        if m<10:
            m ="0"+str(m)
        s = self.s
        if s<10:
            s = "0"+str(s)
        return str(h)+str(":")+str(m)+str(":")+str(s)

reloj = Reloj(3,59,59)
print(reloj.imprimirHora())
reloj.incremento()
print(reloj.imprimirHora())

"""
4. Cree una clase Punto que modele un punto en un espacio bidimensional. Tendrá dos atributos, x e y,
que guardan las coordenadas cartesianas y un constructor al que se le pasan las coordenadas 
cartesianas del punto. La clase debe proporcionar dos métodos para obtener las coordenadas polares 
del punto: distancia al origen (rho) y ángulo respecto al origen de coordenadas (theta). 
También habrá un método para obtener la distancia a otro punto (distancia), un método para aplicar un factor de escalado (escala), un método para aplicar
una traslación (traslada) y un método para imprimir el punto con el formato (x, y).
Construya un programa que cree varios objetos de la clase Punto y pruebe todos sus métodos.
"""