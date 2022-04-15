import scipy.stats as stat #es para sacar el valor de chi cuadrado con N grados de libertad y un alfa.
import random 
import math
import numpy as np
import matplotlib.pyplot as plt
#Generar valores con el GCL
def GenerarValoresPorGCL(z0, a, c, m):
    Ui = []
    Ui.append(z0 / m)
    zant = z0
    for i in range (999):
        zi = (zant * a + c) %m
        Ui.append(zi / m)
        zant = zi
    return Ui

#Generador de python
def llenarVectorAleatorio():
    x = []
    for i in range(1000):
        x.append(math.trunc(random.uniform(200,300)))
    return x



rangos = [range(200,210),range(210,221),range(221,231),
range(231,241),range(241,251),range(251,261),
range(261,271),range(271,281),range(281,291),range(291,301)]

numeros =  [218, 275, 229, 272, 257, 285, 255, 206, 279, 288,
292, 255, 201, 204, 205, 222, 283, 258, 248, 230,
204, 279, 242, 215, 222, 239, 270, 264, 275, 282,
279, 241, 242, 223, 260, 263, 232, 285, 246, 255,
200, 296, 245, 299, 280, 228, 298, 278, 300, 255,
264, 259, 207, 295, 269, 215, 250, 245, 275, 204,
264, 237, 242, 262, 213, 202, 298, 272, 270, 201,
250, 216, 212, 293, 289, 291, 219, 281, 230, 269,
292, 205, 238, 294, 254, 278, 208, 241, 220, 288,
283, 235, 220, 241, 223, 239, 297, 275, 216, 265,
220, 292, 258, 264, 216, 298, 218, 274, 294, 213,
219, 258, 244, 229, 242, 271, 223, 288, 208, 245,
250, 240, 290, 257, 274, 278, 254, 205, 221, 216,
217, 256, 274, 267, 223, 297, 247, 230, 296, 240,
208, 219, 282, 214, 250, 235, 271, 253, 293, 245,
255, 291, 267, 266, 246, 259, 215, 261, 220, 287,
225, 247, 283, 248, 233, 206, 254, 223, 240, 216,
280, 257, 285, 260, 246, 238, 276, 275, 273, 234,
256, 207, 222, 289, 295, 231, 247, 203, 244, 265,
213, 218, 203, 228, 253, 221, 265, 216, 293, 272,
295, 256, 227, 214, 233, 280, 242, 274, 228, 272,
280, 201, 242, 284, 225, 237, 283, 296, 271, 258,
211, 200, 244, 213, 268, 276, 233, 280, 265, 207,
290, 214, 296, 201, 283, 259, 256, 273, 236, 269,
289, 229, 256, 267, 299, 280, 294, 249, 223, 216,
215, 250, 219, 267, 270, 225, 231, 264, 229, 289,
212, 279, 238, 259, 256, 288, 275, 299, 211, 214,
291, 240, 275, 267, 268, 213, 225, 272, 200, 292,
232, 228, 219, 293, 261, 280, 238, 243, 291, 209,
204, 229, 284, 233, 215, 218, 252, 265, 262, 221,
215, 207, 223, 260, 269, 294, 238, 258, 297, 217,
211, 200, 288, 227, 242, 233, 210, 225, 263, 266,
263, 268, 250, 231, 209, 262, 206, 238, 244, 251,
266, 261, 249, 285, 275, 281, 207, 263, 206, 267,
235, 266, 264, 206, 252, 212, 214, 297, 238, 220,
291, 234, 232, 271, 244, 258, 215, 238, 284, 243,
278, 295, 281, 206, 216, 236, 215, 297, 285, 256,
240, 216, 296, 281, 206, 208, 266, 257, 288, 219,
217, 241, 246, 279, 271, 236, 252, 204, 273, 218,
280, 211, 246, 207, 230, 235, 216, 278, 225, 200,
265, 291, 245, 219, 274, 267, 272, 259, 214, 254,
212, 260, 251, 285, 211, 291, 300, 220, 227, 255,
300, 200, 245, 280, 274, 272, 266, 252, 270, 287,
207, 229, 283, 280, 235, 286, 221, 261, 251, 265,
210, 292, 291, 204, 275, 238, 229, 215, 221, 227,
293, 211, 269, 216, 219, 262, 224, 264, 249, 276,
284, 233, 259, 282, 268, 299, 291, 295, 216, 208,
239, 217, 224, 298, 273, 271, 206, 234, 249, 289,
296, 207, 221, 226, 298, 250, 225, 215, 265, 291,
290, 229, 294, 287, 268, 225, 213, 207, 244, 270,
285, 277, 216, 256, 251, 266, 242, 271, 283, 297,
236, 250, 278, 284, 239, 248, 275, 215, 285, 212,
200, 254, 221, 261, 247, 270, 225, 214, 281, 207,
228, 210, 223, 219, 282, 224, 203, 271, 230, 201,
264, 300, 243, 272, 214, 245, 293, 211, 213, 265,
297, 281, 263, 213, 225, 216, 228, 209, 221, 256,
262, 256, 204, 249, 296, 257, 277, 228, 260, 222,
260, 293, 224, 209, 200, 219, 241, 261, 300, 287,
298, 290, 224, 235, 273, 219, 215, 294, 247, 210,
203, 223, 263, 281, 273, 269, 226, 221, 249, 265,
233, 210, 200, 262, 207, 278, 242, 206, 294, 263,
202, 209, 232, 263, 204, 227, 218, 224, 234, 293,
220, 292, 271, 264, 289, 252, 231, 287, 201, 246,
288, 300, 260, 200, 298, 249, 296, 214, 267, 238,
255, 300, 266, 294, 262, 234, 228, 260, 296, 203,
267, 278, 210, 243, 250, 272, 290, 251, 264, 249,
267, 204, 282, 250, 210, 252, 289, 247, 266, 284,
241, 267, 203, 239, 246, 291, 297, 280, 247, 223,
255, 254, 216, 246, 290, 289, 284, 201, 252, 217,
291, 214, 264, 283, 232, 231, 299, 215, 269, 227,
233, 219, 291, 257, 245, 275, 281, 262, 235, 276,
203, 283, 234, 274, 278, 263, 271, 250, 214, 273,
279, 276, 266, 222, 249, 232, 239, 207, 294, 287,
230, 268, 207, 258, 215, 253, 293, 223, 254, 259,
253, 217, 200, 248, 289, 260, 236, 210, 215, 225,
283, 255, 229, 268, 203, 206, 263, 200, 243, 240,
275, 203, 248, 276, 281, 278, 233, 255, 299, 261,
223, 289, 247, 270, 244, 267, 256, 251, 268, 202,
300, 297, 236, 239, 299, 253, 268, 231, 249, 228,
220, 244, 295, 276, 272, 215, 251, 255, 296, 293,
254, 236, 295, 283, 225, 292, 226, 201, 221, 291,
226, 255, 258, 286, 220, 257, 285, 242, 202, 240,
283, 300, 264, 273, 247, 257, 265, 269, 214, 202,
245, 243, 202, 224, 219, 204, 297, 266, 228, 211,
297, 271, 235, 255, 290, 225, 240, 261, 220, 200,
211, 269, 236, 203, 276, 207, 228, 206, 257, 275,
243, 250, 262, 277, 291, 214, 269, 249, 220, 217,
285, 219, 257, 246, 249, 293, 299, 289, 294, 228,
262, 229, 236, 277, 253, 279, 247, 217, 230, 223,
246, 200, 244, 272, 297, 285, 248, 263, 223, 299,
256, 292, 224, 239, 288, 226, 275, 297, 205, 228,
264, 258, 213, 255, 269, 296, 221, 233, 291, 295,
257, 275, 278, 265, 232, 218, 235, 241, 243, 296,
247, 254, 295, 249, 270, 271, 282, 205, 246, 279,
278, 279, 235, 215, 286, 269, 263, 207, 245, 293,
295, 226, 218, 221, 219, 260, 266, 267, 243, 200,
212, 219, 227, 207, 269, 200, 233, 283, 251, 221,
207, 249, 220, 230, 215, 212, 265, 264, 294, 297,
281, 288, 217, 254, 219, 236, 295, 275, 298, 255,
288, 243, 229, 237, 215, 212, 280, 278, 245, 225]

# print(numeros)
#CALCULO FO
def pruebaDeHuecos(arr):
    numeros = arr
    i = 0
    k = 0
    CANTNUM=1000
    TABLA = [
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],
                [0,0,0,0,0,0,0,0,0,0]
            ]
    for numero in numeros:
        k = 0
        for rango in rangos:
            if numero in rango:
                (TABLA[0])[k] += 1
            k += 1
        i+=1
    #CALCULO FOA , POA , |PEA - POA|
    i = 0
    acum = 0
    for frecuencia in TABLA[0]:
        acum += frecuencia 
        (TABLA[1])[i] = acum
        (TABLA[2])[i] = acum/CANTNUM
        (TABLA[4])[i] = abs((TABLA[3])[i] - (TABLA[2])[i])
        i += 1
    maxIndex = np.where(TABLA[4] == np.amax(TABLA[4]))
    maxIndex = (maxIndex[0])[0] 
    DMCrit = (1.36/math.sqrt(CANTNUM))
    print(' RANGO           |  FO     |  FOA    |   POA  |  PEA  |   (|PEA - POA|)    |')
    print('---------------------------------------------------------------------------')
    i = 0
    for c in TABLA[1]:
        if ( i == maxIndex):
            print(" %(5)s | %(0)s      | %(1)s     | %(2)s  |   %(3)s |  %(4)s  |" % {'0':  (TABLA[0])[i], '1': (TABLA[1])[i],
                                                                                        '2': (TABLA[2])[i],'3': (TABLA[3])[i],
                                                                                        '4': '\033[93m'+str((TABLA[4])[i])+'\033[0m','5':rangos[i]})
            print('---------------------------------------------------------------------------')
        else:
            print(" %(5)s | %(0)s      | %(1)s     | %(2)s  |   %(3)s |  %(4)s  |" % {'0':  (TABLA[0])[i], '1': (TABLA[1])[i],
                                                                                    '2': (TABLA[2])[i],'3': (TABLA[3])[i],
                                                                                    '4': (TABLA[4])[i],'5':rangos[i]})
            print('---------------------------------------------------------------------------')
        i +=1 
    if(TABLA[4][maxIndex]<=DMCrit):
        print(('\033[92m'+' %(0)s SE ACEPTA HIPOTESIS'+'\033[0m')%{'0':str(TABLA[4][maxIndex]) + ' <= ' + str(DMCrit)})
    else:
        print(('\033[91m'+' %(0)s SE RECHAZA HIPOTESIS'+'\033[0m') % {'0':str(TABLA[4][maxIndex]) + ' > ' + str(DMCrit)})
    print('---------------------------------------------------------------------------')
pruebaDeHuecos(numeros)
pruebaDeHuecos(llenarVectorAleatorio())