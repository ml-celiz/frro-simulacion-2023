import scipy.stats as sp
import numpy as np
import matplotlib.pyplot as plt

uniformes = []

#Test Distrubución Uniforme
def testUniforme(uniformes):

    k = 200
    salto = 1/k
    confianza = 0.95
    n=len(uniformes)
    uniformes = np.asarray(uniformes)/max(uniformes)

    listaFrAbs = np.array([0] * k)

    for i in uniformes:
        posLista = 0
        for j in np.arange(0,1,salto):
            if j < i < j+salto:
                listaFrAbs[posLista] += 1
                break
            posLista += 1

    listaFr = listaFrAbs/n
    plt.title('Frecuencia relativa de números generados por intervalo')
    plt.bar(range(0,k),(listaFr))
    plt.xlabel("Intervalo")
    plt.ylabel("Frecuencia relativa")
    plt.ylim(0,max(listaFr)*2)
    plt.xlim(-1,k)
    plt.show()

    sumatoriaFrecuencias = 0
    for frec in listaFrAbs:
        print(frec, " ", n, " ", k)
        sumatoriaFrecuencias += (frec-(n/k))**2

    chicuadrado = (sumatoriaFrecuencias)/(n/k)
    print("X^2 = ",chicuadrado)

    valorTabla = sp.chi2.ppf(confianza,k-1)
    print("valor tabla = ",valorTabla)

    if chicuadrado < valorTabla:
        print("Son uniformes")
    else:
        print("No son uniformes")

#Test Distribución Exponencial
def testExpo(exponenciales):
    rvs1 = sp.expon.rvs(size=len(exponenciales), scale=1/2)
    statistic,pValue= sp.ks_2samp(exponenciales, rvs1)
    print(statistic,pValue)

#Test Distribución Normal
def testNormal(data, u, s):
    rvs1 = sp.norm.rvs(size=1000000, scale=u,loc=s)
    statistic,pValue= sp.ks_2samp(data, rvs1)
    print(statistic,pValue)
