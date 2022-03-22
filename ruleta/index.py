#librerias necesarias
import random
import matplotlib.pyplot as plt
import statistics


#Datos
n = 10000
valores_obtenidos = []
for i in range(n):
	valores_obtenidos.append(random.randrange(37))

valor = random.randrange(37)

print('Valor obtenido:', valor)

#--------------------------------#

#Frecuencia relativa
lista_frec_relativa = []
total_tiradas = []
num_apariciones = 0
for i in range(1,n):
    numero_sale = random.randrange(37)
    if valor == numero_sale:
        num_apariciones += 1
    
    f_r = num_apariciones/i
    lista_frec_relativa.append(f_r)
    total_tiradas.append(i)

#Grafica frecuencia relativa    
plt.title('Frecuencia relativa del número '+ str(valor)) 
plt.plot(total_tiradas, lista_frec_relativa,'ro-', markersize=0.5, lw=0.5)
plt.grid(True)
plt.xlabel('Tiradas')
plt.ylabel('Fr')
plt.show()

#--------------------------------#
#Esperanza
esperanza = statistics.mean(valores_obtenidos)
print('Esperanza: ',esperanza)
lista_esperanza = []
total_tiradas = []
for i in range(n):
    esperanza = statistics.mean(valores_obtenidos[:i+1]) #Esperanza en ese momento
    lista_esperanza.append(esperanza)
    total_tiradas.append(i)

#Grafica esperanza
plt.title('Esperanza en {} tiradas'.format(n))
plt.plot(total_tiradas, lista_esperanza,'ro-', markersize=0.5, lw=0.5)
plt.grid(True)
plt.xlabel('Tiradas')
plt.ylabel('Esperanza')
plt.show()

#--------------------------------#

#Varianza
varianza = statistics.pvariance(valores_obtenidos)
print('Varianza: ', varianza)
lista_varianza = []
total_tiradas = []    
for i in range(n):
    varianza = statistics.pvariance(valores_obtenidos[:i+1]) #Varianza en ese momento
    lista_varianza.append(varianza)
    total_tiradas.append(i)

#Grafica Varianza
plt.title('Varianza en {} tiradas'.format(n))
plt.plot(total_tiradas, lista_varianza,'ro-', markersize=0.5, lw=0.5)
plt.grid(True)
plt.xlabel('Tiradas')
plt.ylabel('Varianza')
plt.show()

#--------------------------------#

#Desvio
varianza = statistics.pstdev(valores_obtenidos)
print('Desvio: ', varianza)
lista_desvio = []
total_tiradas = []    
for i in range(n):
    desvio = statistics.pstdev(valores_obtenidos[:i+1]) #Desvio en ese momento
    lista_desvio.append(desvio)
    total_tiradas.append(i)

#Grafica Varianza
plt.title('Desvio en {} tiradas'.format(n))
plt.plot(total_tiradas, lista_desvio,'ro-', markersize=0.5, lw=0.5)
plt.grid(True)
plt.xlabel('Tiradas')
plt.ylabel('Desvio')
plt.show()
