import matplotlib.pyplot as plt
import random
import numpy as np

def define_apuesta():
    apuesta = apuesta_inicial
    return apuesta

def define_apuesta_martingala(n,resultado_anterior,apuesta_anterior):
    apuesta = 0
    if n == 0 or resultado_anterior == 'GANA':
        apuesta = apuesta_inicial
    if resultado_anterior == 'PIERDE':
        apuesta = apuesta_anterior * 2
    return apuesta

def define_apuesta_fibonacci(n,resultado_anterior,apuesta_anterior,apuesta_anterior_2):
    apuesta = 0
    if n == 0 or resultado_anterior == 'GANA':
        apuesta = apuesta_inicial
    if resultado_anterior == 'PIERDE':
        apuesta = apuesta_anterior + apuesta_anterior_2
    return apuesta

def tirar_ruleta(rango_desde, rango_hasta):
  numero_aleatorio = random.randint(rango_desde, rango_hasta)
  if numero_aleatorio in rojos:
    resultado = 'ROJO'
  if numero_aleatorio in negros:
    resultado = 'NEGRO'
  if numero_aleatorio == 0:
    resultado = 'CERO'
  return resultado

def apostar_aleatoriamente():
  apuesta = random.randint(0, 1)
  if apuesta == 0:
    resultado = 'NEGRO'
  if apuesta == 1:
    resultado = 'ROJO'
  return resultado

def apostar_al_rojo():
  resultado = 'ROJO'
  return resultado

def  frecuencia_relativa_resultado_favorable (lista): 
  lista_frecuencias_relativas = []
  for i in range (len(lista)):
    lista_frecuencias_relativas.append(lista[0:i+1].count ('GANA') / len (lista[0:i+1]))
  return lista_frecuencias_relativas

def calcula_cantidad_maxima_rachas_perdedoras(lista):
    cantidad_actual = 0 
    cantidad_maxima = 0 
    for i in range(len(lista)):
        if cantidad_actual > cantidad_maxima:
            cantidad_maxima = cantidad_actual

        if lista[i] == 'PIERDE':
            cantidad_actual = cantidad_actual + 1
        else:
            cantidad_actual = 0
    return cantidad_maxima

#################Inicio
cantidad_n_tiradas = 200
cantidad_p_apostadores = 10
## Espacio muestral [0..36]
rango_desde, rango_hasta = 0, 36
flujo_caja_inicial = 50
apuesta_inicial = 1
apuesta_actual = 0
## Espacio muestral [0..36]
rojos  = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
negros = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]

matriz_flujos_caja_martingala, matriz_flujos_caja_fibonacci = [], []
matriz_flujos_caja_martingala_infinitos, matriz_flujos_caja_fibonacci_infinitos = [], []
matriz_resultados_apuestas_infinito = []
matriz_frecuencia_relativa_resultado_favorable_infinito = []
matriz_frecuencia_relativa_resultado_favorable_fibonacci = []
matriz_frecuencia_relativa_resultado_favorable_martingala = []
ganancia_de_la_casa = 0

for j in range(cantidad_p_apostadores):
    lista_resultados_apuestas_martingala = []
    lista_resultados_apuestas_fibonacci = []
    lista_resultados_apuestas_infinito = []
    #MARTINGALA
    lista_flujos_caja_martingala = []
    lista_flujos_caja_martingala_infinitos = []
    flujo_caja_martingala = flujo_caja_inicial
    flujo_caja_martingala_infinito = flujo_caja_inicial
    #FIBONACCI
    lista_flujos_caja_fibonacci = []
    lista_flujos_caja_fibonacci_infinitos = []
    flujo_caja_fibonacci = flujo_caja_inicial
    flujo_caja_fibonacci_infinito = flujo_caja_inicial

    resultado_anterior = ''
    apuesta_anterior_martingala, apuesta_anterior_fibonacci, apuesta_anterior_2_fibonacci = 0, 0, 0
    for i in range(cantidad_n_tiradas):
        color_apostado = apostar_al_rojo()
        apuesta_actual_martingala = 0
        apuesta_actual_martingala = define_apuesta_martingala(i,resultado_anterior,apuesta_anterior_martingala)
        apuesta_actual_fibonacci = 0
        apuesta_actual_fibonacci = define_apuesta_fibonacci(i,resultado_anterior,apuesta_anterior_fibonacci,apuesta_anterior_2_fibonacci)

        resultado_tirada = tirar_ruleta(rango_desde, rango_hasta)
    
        if color_apostado == resultado_tirada:
            resultado_apuesta = 'GANA'
            #MARTINGALA
            flujo_caja_martingala_infinito = flujo_caja_martingala_infinito + (apuesta_actual_martingala)
            if flujo_caja_martingala >= 0:
                # Si el dinero disponible es menor a lo que debo apostar apuesto lo que tengo
                if flujo_caja_martingala < apuesta_actual_martingala:
                    ganancia_de_la_casa = ganancia_de_la_casa - flujo_caja_martingala
                    flujo_caja_martingala = flujo_caja_martingala + (flujo_caja_martingala)
                else: 
                    ganancia_de_la_casa = ganancia_de_la_casa - apuesta_actual_martingala
                    flujo_caja_martingala = flujo_caja_martingala + (apuesta_actual_martingala)

            #FIBONACCI
            flujo_caja_fibonacci_infinito = flujo_caja_fibonacci_infinito + (apuesta_actual_fibonacci)
            if flujo_caja_fibonacci >= 0:
                # Si el dinero disponible es menor a lo que debo apostar apuesto lo que tengo
                if flujo_caja_fibonacci < apuesta_actual_fibonacci:
                    ganancia_de_la_casa = ganancia_de_la_casa - flujo_caja_fibonacci
                    flujo_caja_fibonacci  = flujo_caja_fibonacci  + (flujo_caja_fibonacci)
                else: 
                    ganancia_de_la_casa = ganancia_de_la_casa - apuesta_actual_fibonacci
                    flujo_caja_fibonacci  = flujo_caja_fibonacci  + (apuesta_actual_fibonacci)

        if color_apostado != resultado_tirada:
            resultado_apuesta = 'PIERDE'
            #MARTINGALA
            flujo_caja_martingala_infinito = flujo_caja_martingala_infinito - (apuesta_actual_martingala)
            if flujo_caja_martingala >= 0:
                # Si el dinero disponible es menor a lo que debo apostar apuesto lo que tengo
                if flujo_caja_martingala < apuesta_actual_martingala:
                    ganancia_de_la_casa = ganancia_de_la_casa + flujo_caja_martingala
                    flujo_caja_martingala = flujo_caja_martingala - (flujo_caja_martingala)
                else:
                    ganancia_de_la_casa = ganancia_de_la_casa +    apuesta_actual_martingala
                    flujo_caja_martingala = flujo_caja_martingala - (apuesta_actual_martingala)

            #FIBONACCI
            flujo_caja_fibonacci_infinito = flujo_caja_fibonacci_infinito - (apuesta_actual_fibonacci)
            if flujo_caja_fibonacci >= 0:
                # Si el dinero disponible es menor a lo que debo apostar apuesto lo que tengo
                if flujo_caja_fibonacci < apuesta_actual_fibonacci:
                    ganancia_de_la_casa = ganancia_de_la_casa + flujo_caja_fibonacci
                    flujo_caja_fibonacci = flujo_caja_fibonacci - (flujo_caja_fibonacci) 
                else: 
                    ganancia_de_la_casa = ganancia_de_la_casa +   apuesta_actual_fibonacci
                    flujo_caja_fibonacci = flujo_caja_fibonacci - (apuesta_actual_fibonacci)
        if flujo_caja_fibonacci > 0:
            lista_resultados_apuestas_fibonacci.append(resultado_apuesta)
        if flujo_caja_martingala > 0:
            lista_resultados_apuestas_martingala.append(resultado_apuesta)

        lista_resultados_apuestas_infinito.append(resultado_apuesta)
        lista_flujos_caja_martingala.append(flujo_caja_martingala)
        lista_flujos_caja_martingala_infinitos.append(flujo_caja_martingala_infinito)
        lista_flujos_caja_fibonacci.append(flujo_caja_fibonacci)
        lista_flujos_caja_fibonacci_infinitos.append(flujo_caja_fibonacci_infinito)
        apuesta_anterior_martingala = apuesta_actual_martingala

        if resultado_apuesta == 'PIERDE' and resultado_anterior != 'PIERDE':
            apuesta_anterior_2_fibonacci = 0
        else: 
            apuesta_anterior_2_fibonacci =apuesta_anterior_fibonacci

        apuesta_anterior_fibonacci = apuesta_actual_fibonacci
        resultado_anterior = resultado_apuesta

    matriz_frecuencia_relativa_resultado_favorable_infinito.append(frecuencia_relativa_resultado_favorable (lista_resultados_apuestas_infinito))
    matriz_frecuencia_relativa_resultado_favorable_fibonacci.append(frecuencia_relativa_resultado_favorable (lista_resultados_apuestas_fibonacci))
    matriz_frecuencia_relativa_resultado_favorable_martingala.append(frecuencia_relativa_resultado_favorable (lista_resultados_apuestas_martingala))
    matriz_flujos_caja_martingala.append(lista_flujos_caja_martingala)
    matriz_flujos_caja_martingala_infinitos.append(lista_flujos_caja_martingala_infinitos)
    matriz_flujos_caja_fibonacci.append(lista_flujos_caja_fibonacci)
    matriz_flujos_caja_fibonacci_infinitos.append(lista_flujos_caja_fibonacci_infinitos)
    matriz_resultados_apuestas_infinito.append(lista_resultados_apuestas_infinito)
print('ganancia_de_la_casa')
print(ganancia_de_la_casa)
frecuencia_relativa_esperada = 18/37
print('frecuencia_relativa_esperada')
print(frecuencia_relativa_esperada)

print('Cantidad de apuestas de los jugadores')
for j in range(cantidad_p_apostadores):
    print('Jugador ',j+1, ' fibonacci:      ',len(matriz_frecuencia_relativa_resultado_favorable_fibonacci[j]),' máx cant rachas perdedoras ' ,calcula_cantidad_maxima_rachas_perdedoras(matriz_resultados_apuestas_infinito[j][0:len(matriz_frecuencia_relativa_resultado_favorable_fibonacci[j])]) )
    print('Jugador ',j+1, ' martingala:       ' ,len( matriz_frecuencia_relativa_resultado_favorable_martingala[j]),' máx cant rachas perdedoras ' ,calcula_cantidad_maxima_rachas_perdedoras(matriz_resultados_apuestas_infinito[j][0:len(matriz_frecuencia_relativa_resultado_favorable_martingala[j])]) )
    print()

plt.ylim(0,1)
plt.axhline(frecuencia_relativa_esperada, color='g', linestyle='-', label = "Frecuencia relativa esperada")
plt.legend()
for j in range(cantidad_p_apostadores):
    plt.plot(matriz_frecuencia_relativa_resultado_favorable_martingala[j])
#plt.bar(x1, matriz_frecuencias_relativas[0],width = 0.5)
plt.ylabel('Frecuencia relativa')
plt.xlabel('Número de tiradas')
plt.title('Martingala: Frecuencias relativas de apuestas favorables con capital finito')
plt.show()

plt.ylim(0,1)
plt.axhline(frecuencia_relativa_esperada, color='g', linestyle='-', label = "Frecuencia relativa esperada")
plt.legend()
for j in range(cantidad_p_apostadores):
    plt.plot(matriz_frecuencia_relativa_resultado_favorable_fibonacci[j])
#plt.bar(x1, matriz_frecuencias_relativas[0],width = 0.5)
plt.ylabel('Frecuencia relativa')
plt.xlabel('Número de tiradas')
plt.title('Fibonacci: Frec. relativa capital finito en 10 jugadas')
plt.show()

plt.ylim(0,1)
plt.axhline(frecuencia_relativa_esperada, color='g', linestyle='-', label = "Frecuencia relativa esperada")
plt.legend()
for j in range(cantidad_p_apostadores):
    plt.plot(matriz_frecuencia_relativa_resultado_favorable_infinito[j])
#plt.bar(x1, matriz_frecuencias_relativas[0],width = 0.5)
plt.ylabel('Frecuencia relativa')
plt.xlabel('Número de tiradas')
plt.title('Frecuencias relativas de apuestas favorables con capital infinito')
plt.show()

print('flujo de caja inicial')
print(flujo_caja_inicial)
#flujo de caja

plt.axhline(flujo_caja_inicial, color='g', linestyle='-', label = "Flujo de caja inicial")
plt.legend()
for j in range(cantidad_p_apostadores):
    plt.plot(matriz_flujos_caja_martingala[j])

plt.ylabel('Cantidad de capital')
plt.xlabel('Número de tiradas')
plt.title('Martingala: Flujos de caja finita de las N tiradas')
plt.show()

plt.axhline(flujo_caja_inicial, color='g', linestyle='-', label = "Flujo de caja inicial")
plt.legend()
for j in range(cantidad_p_apostadores):
    plt.plot(matriz_flujos_caja_martingala_infinitos[j])
plt.ylabel('Cantidad de capital')
plt.xlabel('Número de tiradas')
plt.title('Martingala: Flujos de caja infinita de las N tiradas')
plt.show()

plt.axhline(flujo_caja_inicial, color='g', linestyle='-', label = "Flujo de caja inicial")
plt.legend()
for j in range(cantidad_p_apostadores):
    plt.plot(matriz_flujos_caja_fibonacci[j])

plt.ylabel('Cantidad de capital')
plt.xlabel('Número de tiradas')
plt.title('Fibonacci: Capital finito en 10 jugadas')
plt.show()

plt.axhline(flujo_caja_inicial, color='g', linestyle='-', label = "Flujo de caja inicial")
plt.legend()
for j in range(cantidad_p_apostadores):
    plt.plot(matriz_flujos_caja_fibonacci_infinitos[j])
plt.ylabel('Cantidad de capital')
plt.xlabel('Número de tiradas')
plt.title('Fibonacci: Capital infinito en 10 jugadas')
plt.show()

# Bibliografía https://www.casino.org/es/ruleta/estrategia/
# Bibliografía https://www.casino.org/es/ruleta/como-jugar/