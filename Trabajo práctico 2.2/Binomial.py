import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp
import math
import random as rm
import scipy.interpolate as si
from NumerosGenerados import *
from Testsdiscretos import *

#Graficando Binomial
n, p = 30, 0.4
xLine = np.arange(sp.binom.ppf(0.01, n, p),
sp.binom.ppf(0.99, n, p))
fmp = sp.binom.pmf(xLine, n, p)
plt.plot(xLine, fmp, '--')
plt.vlines(xLine, 0, fmp, colors='b', lw=5, alpha=0.5)
plt.title('Distribución Binomial')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()
print("Media: ", round(np.mean(xLine),3))
print("Desvio: ", round(np.sqrt(np.var(xLine)),3))
print("Varianza: ", round(np.var(xLine),3))

#----------Naylor----------
cant = 10000

randomGCL = generarNumeros(cant)

binomiales= []

def funBinomial(n, p):
    for i in range (cant):
        x= 0
        for j in range (n):
            r=rm.uniform(0,1)
            if ((r-p)<=0):
                x = x + 1
        binomiales.append(x)

    unicos, cuenta = np.unique(binomiales, return_counts=True)
    frec = np.array(cuenta/cant)
    print("Media: ", round(np.mean(binomiales),3))
    print("Desvio: ", round(np.sqrt(np.var(binomiales)),3))
    print("Varianza: ", round(np.var(binomiales),3))
    plt.title("Distribucion Binomial")
    xnew = np.linspace(unicos.min(), unicos.max(), 300)
    spl = si.make_interp_spline(unicos, frec, k=3)
    frec_suavizada = spl(xnew)
    plt.plot(xLine, fmp, '--')
    plt.vlines(xLine, 0, fmp, colors='black', lw=5, alpha=0.5)
    plt.plot(xnew, frec_suavizada, '--')
    plt.bar(unicos, frec, width=0.2, alpha = 0.7)
    plt.show()

funBinomial(n,p)
binomialTeorica = np.random.binomial(n, p, cant)
testBinomial(binomiales,binomialTeorica)