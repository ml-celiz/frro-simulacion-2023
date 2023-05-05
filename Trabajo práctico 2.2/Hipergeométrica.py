import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp
import math
import random as rm
import numpy as np
from NumerosGenerados import *
import scipy.interpolate as si

# Graficando Hipergeométrica
M, n, N = 50,20 , 35 # parametros de forma
hipergeometrica = sp.hypergeom(M, n, N) # Distribución
xLine = np.arange(hipergeometrica.ppf(0.01),
hipergeometrica.ppf(0.99))
fmp = hipergeometrica.pmf(xLine) # Función de Masa de Probabilidad
plt.plot(xLine, fmp, '--')
plt.vlines(xLine, 0, fmp, colors='red', lw=5, alpha=0.5,ec="black")
plt.title('Distribución Hipergeométrica')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()
print(xLine,fmp)
print("Media: ", np.mean(xLine))
print("Desvio: ", np.sqrt(np.var(xLine)))
print("Varianza: ", np.var(xLine))

#----------Naylor----------
cant = 10000

randomGCL = generarNumeros(cant)

p=n/M

#M Tamaño Moblación
#n Tamaño Muestra
#N Cantidad de

#Distribución Hipergeométrica
def hiper(M, N, p):
    hipers = []
    for i in range (cant):
        x = 0
        Mn = M
        Pp = p
        for j in range (N):
            r = rm.choice(randomGCL)
            if ((r-Pp)<=0):
                s = 1
                x = x +1
            else:
                s = 0
            Pp = (Mn * Pp - s)/(Mn - 1)
            Mn = Mn - 1
        hipers.append(x)
        
    unicos, cuenta = np.unique(hipers, return_counts=True)
    frec = np.array(cuenta/cant)
    print("Media: ", np.mean(hipers))
    print("Desvio: ", np.sqrt(np.var(hipers)))
    print("Varianza: ", np.var(hipers))
    plt.title("Distribucion Hipergeométrica")
    print(unicos,cuenta)
    xnew = np.linspace(unicos.min(), unicos.max(), 300)
    spl = si.make_interp_spline(unicos, frec, k=3)
    frec_suavizada = spl(xnew)
    plt.plot(xLine, fmp, '--', color = "red")
    plt.vlines(xLine, 0, fmp, colors='black', lw=5, alpha=0.5)
    plt.plot(xnew, frec_suavizada, '--')
    plt.bar(unicos, frec, width=0.2, alpha = 0.7)
    plt.show()

hiper(M, N , p)
