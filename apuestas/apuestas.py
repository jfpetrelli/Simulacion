import random
import matplotlib.pyplot as plt
import numpy as np

"""
Analisis matematico de ruleta ante diferentes tipos de apuesta.
Apuestas validas:
Numeros: 0 a 36
Color: R(rojo), N(negro)
Paridad: P (par), I(impar)
Docenas: 1D, 2D, 3D
Columas: 1C, 2C, 3C

"""
class Ruleta:
    def __init__(self):
        self.docena_primera = [x for x in range(1, 13)]
        self.docena_segunda = [x for x in range(13, 25)]
        self.docena_tercera = [x for x in range(25, 37)]
        self.columna_primera = [x for x in range(1, 37, 3)]
        self.columna_segunda = [x for x in range(2, 37, 3)]
        self.columna_tercera = [x for x in range(3, 37, 3)]
        self.numero_par = [x for x in range(1, 37) if x % 2 == 0]
        self.numero_impar = [x for x in range(1, 37) if x % 2 != 0]
        self.numero_rojo = (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36)
        self.numero_negro = (2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35)
        self.tabla_pago = {'C1': 2, 'C2': 2, 'C3': 2, 'D1': 2, 'D2': 2, 'D3': 2, 'P': 1, 'I': 1, 'N': 1, 'R': 1,
                           '0': 35, '1': 35, '2': 35, '3': 35, '4': 35, '5': 35, '6': 35, '7': 35, '8': 35, '9': 35,
                           '10': 35, '11': 35, '12': 35, '13': 35, '14': 35, '15': 35, '16': 35, '17': 35, '18': 35,
                           '19': 35, '20': 35, '21': 35, '22': 35, '23': 35, '24': 35, '25': 35, '26': 35, '27': 35,
                           '28': 35, '29': 35, '30': 35, '31': 35, '32': 35, '33': 35, '34': 35, '35': 35, '36': 35,
                           }

    def columna(self, num):
        if num in self.columna_primera:
            return 'C1'
        elif num in self.columna_segunda:
            return 'C2'
        elif num in self.columna_tercera:
            return 'C3'
        else:
            return '0'

    def docena(self, num):
        if num in self.docena_primera:
            return 'D1'
        elif num in self.docena_segunda:
            return 'D2'
        elif num in self.docena_tercera:
            return 'D3'
        else:
            return '0'

    def paridad(self, num):
        if num in self.numero_par:
            return 'P'
        elif num in self.numero_impar:
            return 'I'
        else:
            return '0'

    def color(self, num):
        if num in self.numero_negro:
            return 'N'
        elif num in self.numero_rojo:
            return 'R'
        else:
            return '0'

    def datosNumero (self, num):
        colum = self.columna(num)
        docen = self.docena(num)
        pari = self.paridad(num)
        color = self.color(num)
        return (str(num), colum, docen, pari, color)

    def pagos(self):
        return self.tabla_pago

class Apostador:
    def __init__(self,id , c, a):
        self.capital = [c]
        self.seleccion_apuesta = a
        self.rondas_ganadas = 0
        self.jugador_id = id
        self.multiplicador = 1
        self.frecuencia_ganadas = [0.0]

    def actualizaCapital(self, monto):
        self.capital[-1] += monto * self.multiplicador
        if monto > len(self.seleccion_apuesta):
            self.rondas_ganadas += 1
        self.frecuencia_ganadas.append(self.rondas_ganadas / len(self.frecuencia_ganadas))

    def apuesta(self):
        self.capital.append(self.capital[-1] - len(self.seleccion_apuesta) * self.multiplicador)
        return None

    def apuestasDeApostador(self):
        return self.seleccion_apuesta

    def resultados(self):
        return (self.jugador_id,
                self.capital,
                self.rondas_ganadas,
                self.frecuencia_ganadas)

    def multi(self):
        return self.multiplicador

class Martingala(Apostador):

    def actualizaCapital(self, monto):
        self.capital[-1] += monto * self.multiplicador
        if monto > len(self.seleccion_apuesta):
            self.rondas_ganadas += 1
            self.multiplicador = 1
        else:
            self.multiplicador += self.multiplicador
        self.frecuencia_ganadas.append(self.rondas_ganadas / (len(self.frecuencia_ganadas)))

class MartingalaFinito(Martingala):
    def __init__(self,id , c, a):
        self.capital = [c]
        self.seleccion_apuesta = a
        self.rondas_ganadas = 0
        self.jugador_id = id
        self.multiplicador = 1
        self.frecuencia_ganadas = [0.0]
        self.estado = True

    def apuesta(self):
        if (self.capital[-1] - len(self.seleccion_apuesta) * self.multiplicador) >= 0:
            self.capital.append(self.capital[-1] - len(self.seleccion_apuesta) * self.multiplicador)
        else:
            self.capital[-1] = 0
            self.estado = False
        return self.estado

class Dalembert(Apostador):
    def __init__(self,id , c, a):
        self.capital = [c]
        self.seleccion_apuesta = a
        self.rondas_ganadas = 0
        self.jugador_id = id
        self.multiplicador = 1
        self.frecuencia_ganadas = [0.0]
        self.estado = True

    def actualizaCapital(self, monto):
        self.capital[-1] += monto * self.multiplicador
        if monto > len(self.seleccion_apuesta):
            self.rondas_ganadas += 1
            if self.multiplicador != 1:
                 self.multiplicador -= 1
        else:
            self.multiplicador += 1
        self.frecuencia_ganadas.append(self.rondas_ganadas / (len(self.frecuencia_ganadas)))

class DalembertFinito(Dalembert):

    def apuesta(self):
        if (self.capital[-1] - len(self.seleccion_apuesta) * self.multiplicador) >= 0:
            self.capital.append(self.capital[-1] - len(self.seleccion_apuesta) * self.multiplicador)
        else:
            self.capital[-1] = 0
            self.estado = False
        return self.estado

class Fibonacci(Apostador):
    def __init__(self,id , c, a):
        self.capital = [c]
        self.seleccion_apuesta = a
        self.rondas_ganadas = 0
        self.jugador_id = id
        self.multiplicador = 1
        self.frecuencia_ganadas = [0.0]
        self.estado = True

    def actualizaCapital(self, monto):
        self.capital[-1] += monto * self.multiplicador
        if monto > len(self.seleccion_apuesta):
            self.rondas_ganadas += 1
            if self.multiplicador != 1:
                 self.multiplicador -= 1
        else:
            self.multiplicador += 1
        self.frecuencia_ganadas.append(self.rondas_ganadas / (len(self.frecuencia_ganadas)))

class FibonacciFinito(Fibonacci):

    def apuesta(self):
        if (self.capital[-1] - len(self.seleccion_apuesta) * self.multiplicador) >= 0:
            self.capital.append(self.capital[-1] - len(self.seleccion_apuesta) * self.multiplicador)
        else:
            self.capital[-1] = 0
            self.estado = False
        return self.estado


# Genera variables
tiradas = 200
apostadores = []
numeros_obtenidos = []

#Genera la Ruleta
rul = Ruleta()
tabla_pagos_actual = rul.pagos()


#Genera los apostadores
apostadores.append(Martingala('Mart. Color N', 50, 'N'))
apostadores.append(Apostador('N unitario', 50, 'N'))



for tirada in range(tiradas):
# Apuestas:
    for apostad in range(len(apostadores)):
        apostadores[apostad].apuesta()

# saca numero y obtiene datos
    numeros_obtenidos.append(random.randint(0, 36))
    numero_actual = rul.datosNumero(numeros_obtenidos[tirada])

# verifica ganadores y paga
    for apostad in range(len(apostadores)):
        pago = 0
        multiplica = apostadores[apostad].multi()
        apuesta_actual = apostadores[apostad].apuestasDeApostador()
        for apuesta in range(len(apuesta_actual)):
            if apuesta_actual[apuesta] in numero_actual:
                pago += tabla_pagos_actual[apuesta_actual[apuesta]] + 1    #el 1 es la ficha apostada
        apostadores[apostad].actualizaCapital(pago)

# Grafia y resultados finales:

datos = []
for aposta in range(len(apostadores)):
    datos.append(apostadores[aposta].resultados())
    print('nombre: ', datos[aposta][0],
              'capital inicial: ', datos[aposta][1][0],
              'capital final: ', datos[aposta][1][-1],
          'Frecuencia de rondas Ganadas:', datos[aposta][3][-1])

for aposta in range(0, len(apostadores), 2):
    x = np.linspace(0, tiradas + 1, tiradas + 1)
    plt.title('Mart.: Evolucion de capital')
    plt.plot(x, datos[aposta][1], color="Red", markersize=1, lw=1, label='Martingala')
    plt.plot(x, datos[aposta+1][1], color="Blue", markersize=1, lw=1, label='Apuesta unitaria')
    y = np.linspace(datos[aposta][1][0], datos[aposta][1][0], tiradas + 1)
    plt.plot(x, y, color="Black", markersize=1, lw=1)
    plt.grid(True)
    plt.xlabel('Tiradas')
    plt.ylabel('Capital')
    plt.legend(loc='upper left')
    plt.show()


for aposta in range(0, len(apostadores), 2):
    x = np.linspace(0, tiradas + 1, tiradas + 1)
    plt.title('Mart.: Frec. Relativa de rondas ganadas')
    plt.plot(x, datos[aposta][3], color="Red", markersize=1, lw=1)
    plt.grid(True)
    plt.xlabel('Tiradas')
    plt.ylabel('Frecuencia')
    plt.show()



### 10 Rondas distintas de tiradas

rondas = 10
datos = []
frecuencias = []
#Si se extrae esta parte de codigo hay que generar nuevamente las variables, la ruleta
#solo se reinicia el contadore de numeros en cada iteracion y el apostador

for ron in range(rondas):
    numeros_obtenidos = []
    apostadores = []
    apostadores.append(Martingala('Mart. Color N', 50, 'I'))
    for tirada in range(tiradas):
# Apuestas:
        apostadores[0].apuesta()
# saca numero y obtiene datos
        numeros_obtenidos.append(random.randint(0, 36))
        numero_actual = rul.datosNumero(numeros_obtenidos[tirada])

# verifica ganadores y paga
        pago = 0
        apuesta_actual = apostadores[0].apuestasDeApostador()
        for apuesta in range(len(apuesta_actual)):
            if apuesta_actual[apuesta] in numero_actual:
                pago += tabla_pagos_actual[apuesta_actual[apuesta]] + 1    #el 1 es la ficha apostada
        apostadores[0].actualizaCapital(pago)

#Fin de ronda recolecta resultados
    datos_total = apostadores[0].resultados()
    datos.append(datos_total[1])
    frecuencias.append(datos_total[3])

#finalizadas las rondas grafica
x = np.linspace(0, tiradas + 1, tiradas + 1)
plt.title('Mart.: Capital en 10 jugadas')
for ron in range(rondas):
    plt.plot(x, datos[ron], markersize=1, lw=1)
plt.grid(True)
plt.xlabel('Tiradas')
plt.ylabel('Capital')
plt.show()

#FRECUENCIAS
x = np.linspace(0, tiradas + 1, tiradas + 1)
plt.title('Mart.: Frec. Relativa en 10 jugadas')
for ron in range(rondas):
    plt.plot(x, frecuencias[ron], markersize=1, lw=1)
plt.grid(True)
plt.xlabel('Tiradas')
plt.ylabel('Frecuencia')
plt.show()


## MARTINGALA CAPITAL FINITO


rondas = 10
datos = []
frecuencias = []

#Si se extrae esta parte de codigo hay que generar nuevamente las variables, la ruleta
#solo se reinicia el contadore de numeros en cada iteracion y el apostador

for ron in range(rondas):
    numeros_obtenidos = []
    apostadores = []
    cont = 0
    apostadores.append(MartingalaFinito('Impar capital finito', 20, ['I']))
    for tirada in range(tiradas):
# Apuestas:
        
        estado = apostadores[0].apuesta()
        if estado:
            cont += 1
# saca numero y obtiene datos
            numeros_obtenidos.append(random.randint(0, 36))
            numero_actual = rul.datosNumero(numeros_obtenidos[tirada])

# verifica ganadores y paga
            pago = 0
            apuesta_actual = apostadores[0].apuestasDeApostador()
            for apuesta in range(len(apuesta_actual)):
                if apuesta_actual[apuesta] in numero_actual:
                    pago += tabla_pagos_actual[apuesta_actual[apuesta]] + 1    #el 1 es la ficha apostada
            apostadores[0].actualizaCapital(pago)
        else:
            tirada = tiradas
            
    print('Jugada ', ron+1, 'capital 0 en ', cont, 'jugadas')
#Fin de ronda recolecta resultados
    datos_total = apostadores[0].resultados()
    datos.append(datos_total[1])
    frecuencias.append(datos_total[3])
    print(datos [0])
    print('Rondas hasta perder todo el capital : ', len(datos[0]))
#GRAFICAS 1 COLUMNERO
x = np.linspace(0, len(datos[0]), len(datos[0]))
plt.title('Mart.: Capital finito')
plt.plot(x, datos[0], markersize=1, lw=1)
plt.grid(True)
plt.xlabel('Tiradas')
plt.ylabel('Capital')
plt.show()

#FRECUENCIAS
x = np.linspace(0, len(frecuencias[0]), len(frecuencias[0]))
plt.title('Mart.: Frec. Relativa de capital finito')
plt.plot(x, frecuencias[0], markersize=1, lw=1)
plt.grid(True)
plt.xlabel('Tiradas')
plt.ylabel('Frecuencia')
plt.show()


#GRAFICAS PARA 10 capital finito
plt.title('Mart.: Capital finito en 10 jugadas')
for ron in range(rondas):
    x = np.linspace(0, len(datos[ron]), len(datos[ron]))
    plt.plot(x, datos[ron], markersize=1, lw=1)
plt.grid(True)
plt.xlabel('Tiradas')
plt.ylabel('Capital')
plt.show()

#FRECUENCIAS
plt.title('Mart.: Frec. Relativa capital finito en 10 jugadas')
for ron in range(rondas):
    x = np.linspace(0, len(frecuencias[ron]), len(frecuencias[ron]))
    plt.plot(x, frecuencias[ron], markersize=1, lw=1)
plt.grid(True)
plt.xlabel('Tiradas')
plt.ylabel('Frecuencia')
plt.show()

# -----------------------------------------------------------------------------------------------# 

#Otro tipo de apuesta a D'alembert infinito

rondas = 10
datos = []
frecuencias = []

#Si se extrae esta parte de codigo hay que generar nuevamente las variables, la ruleta
#solo se reinicia el contadore de numeros en cada iteracion y el apostador

for ron in range(rondas):
    numeros_obtenidos = []
    apostadores = []
    apostadores.append(Dalembert('D\'Alembert: Impar capital finito', 500, ['I']))

    for tirada in range(tiradas):
# Apuestas:
            apostadores[0].apuesta()

# saca numero y obtiene datos

            numeros_obtenidos.append(random.randint(0, 36))
            numero_actual = rul.datosNumero(numeros_obtenidos[tirada])

# verifica ganadores y paga
            pago = 0
            apuesta_actual = apostadores[0].apuestasDeApostador()
            for apuesta in range(len(apuesta_actual)):
                if apuesta_actual[apuesta] in numero_actual:
                    pago += tabla_pagos_actual[apuesta_actual[apuesta]] + 1    #el 1 es la ficha apostada
            apostadores[0].actualizaCapital(pago)


#Fin de ronda recolecta resultados
    datos_total = apostadores[0].resultados()
    print(len(datos_total[1]))
    datos.append(datos_total[1])
    frecuencias.append(datos_total[3])

#GRAFICAS 1 COLUMNERO
x = np.linspace(0, len(datos[0]), len(datos[0]))
plt.title('D\'Alembert: Evolucion capital')
plt.plot(x, datos[0], color="Red", markersize=1, lw=1)
plt.grid(True)
plt.xlabel('Tiradas')
plt.ylabel('Capital')
plt.show()

#FRECUENCIAS
x = np.linspace(0, len(frecuencias[0]), len(frecuencias[0]))
plt.title('D\'Alembert: Frec. Relativa')
plt.plot(x, frecuencias[0], color="Red", markersize=1, lw=1)
plt.grid(True)
plt.xlabel('Tiradas')
plt.ylabel('Frecuencia')
plt.show()


#GRAFICAS PARA 10 capital finito
plt.title('D\'Alembert: Capital en 10 jugadas')
for ron in range(rondas):
    x = np.linspace(0, len(datos[ron]), len(datos[ron]))
    plt.plot(x, datos[ron], markersize=1, lw=1)
plt.grid(True)
plt.xlabel('Tiradas')
plt.ylabel('Capital')
plt.show()

#FRECUENCIAS
plt.title('D\'Alembert: Frec. Relativa en 10 jugadas')
for ron in range(rondas):
    x = np.linspace(0, len(frecuencias[ron]), len(frecuencias[ron]))
    plt.plot(x, frecuencias[ron], markersize=1, lw=1)
plt.grid(True)
plt.xlabel('Tiradas')
plt.ylabel('Frecuencia')
plt.show()




#Otro tipo de apuesta a D'alembert finito

rondas = 10
datos = []
frecuencias = []

#Si se extrae esta parte de codigo hay que generar nuevamente las variables, la ruleta
#solo se reinicia el contadore de numeros en cada iteracion y el apostador

for ron in range(rondas):
    numeros_obtenidos = []
    apostadores = []
    cont = 0
    apostadores.append(DalembertFinito('D\'Alembert: Apuesta Impar con cap. finito', 20, ['I']))
    for tirada in range(tiradas):

        estado = apostadores[0].apuesta()
        if estado:
            cont += 1
# saca numero y obtiene datos

            numeros_obtenidos.append(random.randint(0, 36))
            numero_actual = rul.datosNumero(numeros_obtenidos[tirada])

# verifica ganadores y paga
            pago = 0
            apuesta_actual = apostadores[0].apuestasDeApostador()
            for apuesta in range(len(apuesta_actual)):
                if apuesta_actual[apuesta] in numero_actual:
                    pago += tabla_pagos_actual[apuesta_actual[apuesta]] + 1    #el 1 es la ficha apostada
            apostadores[0].actualizaCapital(pago)
        else:
            tirada = tiradas
    print('Jugada ', ron+1, 'capital 0 en ', cont, 'jugadas')
#Fin de ronda recolecta resultados
    datos_total = apostadores[0].resultados()
    print(len(datos_total[1]))
    datos.append(datos_total[1])
    frecuencias.append(datos_total[3])

#GRAFICAS 1 COLUMNERO
x = np.linspace(0, len(datos[0]), len(datos[0]))
plt.title('D\'Alembert: Capital finito')
plt.plot(x, datos[0], color="Red", markersize=1, lw=1)
plt.grid(True)
plt.xlabel('Tiradas')
plt.ylabel('Capital')
plt.show()

#FRECUENCIAS
x = np.linspace(0, len(frecuencias[0]), len(frecuencias[0]))
plt.title('D\'Alembert: Frec. Relativa capital finito')
plt.plot(x, frecuencias[0], markersize=1, lw=1)
plt.grid(True)
plt.xlabel('Tiradas')
plt.ylabel('Frecuencia')
plt.show()


#GRAFICAS PARA 10 capital finito
plt.title('D\'Alembert: Capital finito en 10 jugadas')
for ron in range(rondas):
    x = np.linspace(0, len(datos[ron]), len(datos[ron]))
    plt.plot(x, datos[ron], markersize=1, lw=1)
plt.grid(True)
plt.xlabel('Tiradas')
plt.ylabel('Capital')
plt.show()

#FRECUENCIAS
plt.title('D\'Alembert: Frec. Relativa capital finito en 10 jugadas')
for ron in range(rondas):
    x = np.linspace(0, len(frecuencias[ron]), len(frecuencias[ron]))
    plt.plot(x, frecuencias[ron], markersize=1, lw=1)
plt.grid(True)
plt.xlabel('Tiradas')
plt.ylabel('Frecuencia')
plt.show()
