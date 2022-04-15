import matplotlib.pyplot as plt
import random
from math import sqrt

def genera_lista_muestras(cantidad_numeros_aleatorios,rango_desde, rango_hasta):
    lista = []
    for i in range(cantidad_numeros_aleatorios):
        numero_aleatorio = random.randint(rango_desde, rango_hasta)
        lista.append(numero_aleatorio)
    return lista

def  frecuencia_relativa (lista,rango_hasta): 
  lista_frecuencias_relativas = []
  for i in range (rango_hasta):
    lista_frecuencias_relativas.append(lista.count (i) / len (lista))
  return lista_frecuencias_relativas

def media(lista):
  promedio = sum(lista) / len(lista)
  return promedio
 
def varianza(lista):
  s = 0
  m = media(lista)
  for elemento in lista:
    s += (elemento - m) ** 2
  return s / float(len(lista))
 
def desviacion_estandar(lista):
  return sqrt(varianza(lista))

def dibujar_media(lista):
    suma = 0
    lista_promedios_ejecucion_x = []
    for i in range (cantidad_numeros_aleatorios):
        suma = suma + lista[i]
        lista_promedios_ejecucion_x.append(suma / (i+1))
    plt.plot(lista_promedios_ejecucion_x)

def dibujar_varianza(lista):
    lista_varianza_ejecucion_x = []
    for i in range (cantidad_numeros_aleatorios+1):
        lista_varianza_ejecucion_x.append(varianza(lista[:i+1]))
    plt.plot(lista_varianza_ejecucion_x)
   
def dibujar_desvio_estandar(lista):
    desvio_estandar_ejecucion_x = []
    for i in range (cantidad_numeros_aleatorios):
        desvio_estandar_ejecucion_x.append(desviacion_estandar(lista[:i+1]))
    plt.plot(desvio_estandar_ejecucion_x) 

#################Inicio
print("Numeros aleatorios" )
cantidad_numeros_aleatorios = 5000
## Espacio muestral [0..36]
rango_desde = 0
rango_hasta = 36
promedio = 0

lista = []
lista_promedios_muestra_n = []
lista_desvio_estandar = []
lista_varianza = []
suma = 0

matriz_muestras = []

for i in range(5):
   matriz_muestras.append(genera_lista_muestras(cantidad_numeros_aleatorios,rango_desde, rango_hasta))

for i in range(len(matriz_muestras)):
    dibujar_media(matriz_muestras[i])

plt.axhline(rango_hasta/2, color='r', linestyle='-', label = "vpe valor promedio esperado")
plt.legend()
plt.xlabel("n (número de tiradas)")
plt.ylabel("vp valor promedio de las tiradas")
plt.title('Promedio en 3 jugadas de 5000 tiradas')
plt.show()

for i in range(len(matriz_muestras)):
    dibujar_varianza(matriz_muestras[i])
#plt.axhline([valor], color='r', linestyle='-', label = "vve valor de la varianza esperada")
plt.legend()
plt.xlabel("n (número de tiradas)")
plt.ylabel("vv valor de la varianza")
plt.title('Varianza en 3 jugadas de 5000 tiradas')
plt.show()

for i in range(len(matriz_muestras)):
    dibujar_desvio_estandar(matriz_muestras[i])
#plt.axhline([valor], color='r', linestyle='-', label = "vve valor de la varianza esperada")
plt.legend()
plt.xlabel("n (número de tiradas)")
plt.ylabel("vd valor del desvío")
plt.title('Desvio en 3 jugadas de 5000 tiradas')
plt.show()

x1 = []
for i in range (rango_hasta+1):
    x1.append(i)

frecuencia_esperada = 1/(rango_hasta+1)
print("Frecuencia relativa esperada" )
print(frecuencia_esperada)
lista_frecuencias = frecuencia_relativa (matriz_muestras[1],rango_hasta+1)
plt.ylim(0,0.1)
plt.axhline(frecuencia_esperada, color='g', linestyle='-', label = "Frecuencia esperada")
plt.legend()
plt.bar(x1, lista_frecuencias)
plt.ylabel('Frecuencia relativa')
plt.xlabel('Valores posibles')
plt.title('Frecuencias relativas')
plt.show()