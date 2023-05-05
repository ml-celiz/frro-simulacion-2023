import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp
import math
import random as rm
from NumerosGenerados import *
from Tests import *

n = 1000000
esperanza = 0
desvio = 20
numerosNormal = sp.norm.rvs(size=n, loc = esperanza, scale=desvio)

print("Media: ", round(np.mean(numerosNormal),3))
print("Desvio: ", round(np.sqrt(np.var(numerosNormal)),3))
print("Varianza: ", round(np.var(numerosNormal),3))

plt.hist(numerosNormal, bins=50, color='red', histtype="bar",alpha=0.8,ec="black")
plt.xlabel("valores")
plt.ylabel("Frecuencia Absoluta")
plt.show()

#----------Naylor----------
randomGCL = generarNumeros(n*12)

normales = []

#Distribución Normal
def normal(esperanza, desvio):
    for i in range(n):
        sumatoria = 0
        for j in range (12):
            r=rm.choice(randomGCL)
            sumatoria = sumatoria + r
        normales.append((desvio * (sumatoria-6)) + esperanza)
    
    print("Media: ", round(np.mean(normales),3))
    print("Desvio: ", round(np.sqrt(np.var(normales)),3))
    print("Varianza: ", round(np.var(normales),3))
    plt.title("Distribuciones Normales")
    plt.hist(numerosNormal, bins=50, color='red', histtype="bar",alpha=0.8,ec="black")
    plt.hist(normales, bins=50,color = 'skyblue', histtype="bar",alpha=0.8,ec="black")
    plt.show()

normal(esperanza,desvio)
testNormal(normales,esperanza,desvio)