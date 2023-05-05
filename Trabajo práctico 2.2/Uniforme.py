import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp
import random as rm
from NumerosGenerados import *
from Tests import *

n = 100000
inicio = 0
ancho = 20
numeros_uniformes = sp.uniform.rvs(size=n, loc = inicio, scale=ancho)

plt.hist(numeros_uniformes, bins=50, color='skyblue', histtype="bar",alpha=0.8,ec="black")
plt.title("Distribución Uniforme")
plt.xlabel("valores")
plt.ylabel("Frecuencia Absoluta")
plt.show()

#----------Naylor----------
randomGCL = generarNumeros(n)

uniformes = []

#Distribución Uniforme
def uniforme(a,b):
    for r in randomGCL:
        x = a + (b - a) * r
        uniformes.append(x)

    print("Media: ", round(np.mean(uniformes),3))
    print("Desvio: ", round(np.sqrt(np.var(uniformes)),3))
    print("Varianza: ", round(np.var(uniformes),3))
    plt.title("Distribuciones Uniformes")
    plt.hist(uniformes, bins=50, edgecolor="black",color='darkgrey',alpha=0.8)
    plt.hist(numeros_uniformes, bins=50, color='red', histtype="bar",alpha=0.3,ec="black")
    plt.show()

uniforme(inicio,ancho)
testUniforme(uniformes)