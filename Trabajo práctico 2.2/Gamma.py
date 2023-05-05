import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp
import math
import random as rm
from NumerosGenerados import *
from Tests import *

n = 100000
inicio = 0
ancho = 20
k = 3
alfa = 1
numerosGamma = sp.gamma.rvs(size=n, a=k)

print("Media: ", round(np.mean(numerosGamma),3))
print("Desvio: ", round(np.sqrt(np.var(numerosGamma)),3))
print("Varianza: ", round(np.var(numerosGamma),3))

plt.hist(numerosGamma, bins=50, color='red', histtype="bar",alpha=0.8,ec="black")
plt.xlabel("valores")
plt.ylabel("Frecuencia Absoluta")
plt.show()

#----------Naylor----------
randomGCL = generarNumeros(n)

gammas = []

#Distribución Gamma
def gamma(k,alfa):
    for i in range(n):
        tr=1
        for j in range(k):
            r=rm.choice(randomGCL)
            tr= tr * r
        x=(-math.log(tr))/alfa
        gammas.append(x)

    print("Media: ", round(np.mean(gammas),3))
    print("Desvio: ", round(np.sqrt(np.var(gammas)),3))
    print("Varianza: ", round(np.var(gammas),3))
    plt.title("Distribucion Gamma")
    plt.hist(numerosGamma, bins=50, color='red', histtype="bar",alpha=0.8,ec="black")
    plt.hist(gammas, bins=50, edgecolor="black", histtype="bar",alpha=0.6)
    plt.show()

gamma(k,alfa)