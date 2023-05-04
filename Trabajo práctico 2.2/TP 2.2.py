import random as rm
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.stats as sp

cant = 10000

# Distribución Uniforme según el libro de Naylor
def uniform(a,b):
    uniformes = []
    for i in range (cant):
        r = rm.random()
        x = a + (b - a) * r
        uniformes.append(x) 

    print("Media: ", np.mean(uniformes))
    print("Desvio: ", np.sqrt(np.var(uniformes)))
    print("Varianza: ", np.var(uniformes))
    plt.title("Distribucion Uniforme")
    plt.hist(uniformes, bins=15, edgecolor="black", alpha = 0.5)
    plt.show()

    pyuniformes = []
    for i in range (cant):
        pyuniformes.append(rm.uniform(a,b))
    print("Media: ", np.mean(pyuniformes))
    print("Desvio: ", np.sqrt(np.var(pyuniformes)))
    print("Varianza: ", np.var(pyuniformes))
    plt.title("Distribucion Uniforme Teorica vs. Python")
    plt.hist(uniformes, bins=15, edgecolor="black", alpha = 0.5)    
    plt.hist(pyuniformes, bins=15, edgecolor="black", alpha = 0.5)
    plt.show()

    #Test
    stat, pvalue = sp.kstest(uniformes, 'uniform', args=(a, b))
    print("P VALUE: ", pvalue)
    if pvalue > 0.05:
        resultado = 'Pasa el test'
    else:
        resultado = 'No pasa el test'
    print(resultado)


#Distribución Exponencial según el libro de Naylor
def exponencial(alfa):
    exponenciales=[]
    for i in range (cant):
        r= rm.random()
        exponenciales.append(((-1/alfa)*math.log(r)))
    print("Media: ", np.mean(exponenciales))
    print("Desvio: ", np.sqrt(np.var(exponenciales)))
    print("Varianza: ", np.var(exponenciales))
    plt.title("Distribucion Exponencial")
    plt.hist(exponenciales, bins=30, edgecolor="black", alpha= 0.5)
    plt.show()

    pyexponenciales = sp.expon().rvs(cant)

    print("Media: ", np.mean(pyexponenciales))
    print("Desvio: ", np.sqrt(np.var(pyexponenciales)))
    print("Varianza: ", np.var(pyexponenciales))
    plt.title("Distribucion Exponencial Teorica vs. Python")
    plt.hist(exponenciales, bins=30, edgecolor="black", alpha=0.5 )
    plt.hist(pyexponenciales, bins=30, edgecolor="black", alpha = 0.5)
    plt.show()   
    
    #Test
    statistic, critical, significance= sp.anderson(exponenciales, dist='expon')
    if (statistic>critical[2]):
        resultado= 'No pasa el test'
    else:
        resultado='Pasa el test'
    print("Statistic: ", statistic)
    print("Critical: ", critical[2])
    print(resultado)

#Distribución Gamma según el libro de Naylor
def gamma(k, alfa):
    gammas= []
    for i in range (cant):
        tr=1
        for j in range (k):
            r=rm.random()
            tr= tr * r
        x= -math.log(tr)/alfa
        gammas.append(x)
    print("Media: ", np.mean(gammas))
    print("Desvio: ", np.sqrt(np.var(gammas)))
    print("Varianza: ", np.var(gammas))
    plt.title("Distribucion Gamma")
    plt.hist(gammas, bins=15, edgecolor="black", alpha = 0.5)
    plt.show()

    pygammas= sp.gamma(alfa).rvs(size=cant)
    print("Media: ", np.mean(pygammas))
    print("Desvio: ", np.sqrt(np.var(pygammas)))
    print("Varianza: ", np.var(pygammas))
    plt.title("Distribucion Gamma Teorica vs. Python ")
    plt.hist(gammas, bins=15, edgecolor="black", alpha = 0.5)
    plt.hist(pygammas, bins=15, edgecolor="black", alpha= 0.5)
    plt.show()

#Distribución Normal según el libro de Naylor
def normal(u, s):
    normales = []
    for i in range (cant):
        sum = 0
        for j in range (12):
            r = rm.uniform(0,1)
            sum = sum + r
        normales.append(s * (sum-6) + u )
    print("Media: ", np.mean(normales))
    print("Desvio: ", np.sqrt(np.var(normales)))
    print("Varianza: ", np.var(normales))
    plt.title("Distribucion Normal")
    plt.hist(normales, bins=15, edgecolor="black",weights=np.zeros_like(normales)+1./len(normales), alpha=0.5)
    plt.show()

    normal = sp.norm(u,s)
    data=np.random.normal(loc=u, scale=s, size=cant)
    plt.hist(normales, bins=15, weights=np.zeros_like(normales)+1./len(normales), edgecolor="black" , alpha=0.5)
    plt.hist(data, bins=15,weights=np.zeros_like(data)+1./len(data) ,edgecolor="black" , alpha=0.5)
    print("Media: ", np.mean(data))
    print("Desvio: ", np.sqrt(np.var(data)))
    print("Varianza: ", np.var(data))
    plt.title("Distribucion Normal Teorica vs. Python")
    plt.show()
    
    #Test
    stat, pvalue = sp.kstest(data, 'norm', args=(u, s))
    print("P VALUE: ", pvalue)
    if pvalue > 0.05:
        resultado = 'Pasa el test'
    else:
        resultado = 'No pasa el test'
    print(resultado)

#Distribución Pascal según el libro de Naylor
def pascal(k, q):
    pascales= []
    for j in range (cant):
        tr=1
        qr = math.log(q)
        for i in range (k):
            r = rm.uniform(0,1)
            tr = tr * r
        nx = math.log(tr)//qr
        pascales.append(nx)
    print("Media: ", np.mean(pascales))
    print("Desvio: ", np.sqrt(np.var(pascales)))
    print("Varianza: ", np.var(pascales))
    plt.title("Distribucion Binomial Negativa (Pascal)")
    plt.hist(pascales, bins=100, weights=np.zeros_like(pascales)+1./len(pascales), edgecolor="black", alpha=0.5)
    plt.show()

    pypascales = np.random.negative_binomial(k, q, size= cant)

    print("Media: ", np.mean(pypascales))
    print("Desvio: ", np.sqrt(np.var(pypascales)))
    print("Varianza: ", np.var(pypascales))
    plt.title("Distribucion Binomial Negativa (Pascal) Teorica vs. Python")
    plt.hist(pascales, bins=100, weights=np.zeros_like(pascales)+1./len(pascales), edgecolor="black", alpha=0.5)
    plt.hist(pypascales, bins=100, weights=np.zeros_like(pypascales)+1./len(pypascales), edgecolor="black", alpha=0.5)
    plt.show()

#Distribución Binomial según el libro de Naylor
def binomial (n, p):
    binomiales= []
    for i in range (cant):
        x= 0
        for j in range (n):
            r=rm.uniform(0,1)
            if ((r-p)<=0):
                x = x + 1
        binomiales.append(x)
    print("Media: ", np.mean(binomiales))
    print("Desvio: ", np.sqrt(np.var(binomiales)))
    print("Varianza: ", np.var(binomiales))
    plt.title("Distribucion Binomial")
    plt.hist(binomiales, weights=np.zeros_like(binomiales)+1./len(binomiales) , bins=100, edgecolor="black", alpha=0.5)
    plt.show()

    pybinomiales = sp.binom.rvs(n, p, size= cant)
    print("Media: ", np.mean(pybinomiales))
    print("Desvio: ", np.sqrt(np.var(pybinomiales)))
    print("Varianza: ", np.var(pybinomiales))
    plt.title("Distribucion Binomial Teorica vs. Python")
    plt.hist(pybinomiales, weights=np.zeros_like(binomiales)+1./len(binomiales) ,  bins=100, edgecolor="black", alpha=0.5)
    plt.hist(binomiales , weights=np.zeros_like(pybinomiales)+1./len(pybinomiales), bins=100, edgecolor="black", alpha=0.5)
    plt.show()

    #Test
    statistic, critical, significance = sp.anderson_ksamp([binomiales,pybinomiales])
    if (statistic>critical[2]):
        resultado= 'No pasa el test'
    else:
        resultado='Pasa el test'
    print("Statistic: ", statistic)
    print("Critical: ", critical[2])
    print(resultado)

#Distribución Hipergeométrica según el libro de Naylor
def hiper(N, n, p):
    hipers = []
    for i in range (cant):
        x = 0
        Nn= N
        Pp = p
        for j in range (n):
            r = rm.uniform(0,1)
            if ((r-Pp)<=0):
                s = 1
                x = x +1
            else:
                s = 0
            Pp = (Nn * Pp - s)/(Nn - 1)
            Nn = Nn - 1
        hipers.append(x)
    print("Media: ", np.mean(hipers))
    print("Desvio: ", np.sqrt(np.var(hipers)))
    print("Varianza: ", np.var(hipers))
    plt.title("Distribucion Hipergeometrica")
    plt.hist(hipers ,weights=np.zeros_like(hipers)+1./len(hipers) , bins=100, edgecolor="black")
    plt.show()

#Distribución Poisson según el libro de Naylor
def poisson(lamda):
    poissons = []
    for i in range (cant):
        x = 0
        b = np.exp(-lamda)
        tr = 1
        r = rm.uniform(1,0)
        tr = tr * r
        while((tr-b)>=0):
            x = x + 1
            r = rm.uniform(1,0)
            tr = tr * r
        poissons.append(x)
    print("Media: ", np.mean(poissons))
    print("Desvio: ", np.sqrt(np.var(poissons)))
    print("Varianza: ", np.var(poissons))
    plt.title("Distribucion de Poisson")
    plt.hist(poissons, weights=np.zeros_like(poissons)+1./len(poissons) , bins=100, edgecolor="black",  alpha=0.5)
    plt.show()

    pypoisson = np.random.poisson(lamda, cant)

    print("Media: ", np.mean(pypoisson))
    print("Desvio: ", np.sqrt(np.var(pypoisson)))
    print("Varianza: ", np.var(pypoisson))
    plt.title("Distribucion de Poisson")
    plt.hist(poissons, weights=np.zeros_like(poissons)+1./len(poissons) , bins=100, edgecolor="black", alpha=0.5)
    plt.hist(pypoisson, weights=np.zeros_like(pypoisson)+1./len(pypoisson) , bins=100, edgecolor="black", alpha=0.5)
    plt.show()

    #Test
    statistic, critical, significance = sp.anderson_ksamp([poissons,pypoisson])
    print("Statistic: ", statistic)
    print("Critical: ", critical[2])
    if (statistic>critical[2]):
        resultado= 'No pasa el test'
    else:
        resultado='Pasa el test'
    print(resultado)

#Distribución Empírica según el libro de Naylor
def empirica ():
    empiricos=[]
    x=[1,2,3,4,5,6]
    frec=[0.2, 0.1, 0.15 ,0.1, 0.25, 0.2]
    acum=[0.2, 0.3, 0.45, 0.55, 0.8, 1]
    for i in range (cant):
        r = rm.uniform(0,1)
        for j in range (len(x)):
            if (r <= acum[j]):
                empiricos.append(x[j])
                break
    print("Media: ", np.mean(empiricos))
    print("Desvio: ", np.sqrt(np.var(empiricos)))
    print("Varianza: ", np.var(empiricos))
    plt.title("Distribucion Empirica Discreta")
    plt.hist(empiricos ,weights=np.zeros_like(empiricos)+1./len(empiricos), bins=30, edgecolor="black", alpha=0.5)
    plt.show()
    num = []
    for i in range (20):
        num.append(1)
        num.append(6)
    for i in range(10):
        num.append(2)
        num.append(4)
    for i in range(15):
        num.append(3)
    for i in range(25):
        num.append(5)
    print("Media: ", np.mean(num))
    print("Desvio: ", np.sqrt(np.var(num)))
    print("Varianza: ", np.var(num))
    plt.title("Distribucion Empirica Discreta")
    plt.hist(empiricos ,weights=np.zeros_like(empiricos)+1./len(empiricos), bins=30, edgecolor="black", alpha=0.5)
    plt.hist(num ,weights=np.zeros_like(num)+1./len(num), bins=30, edgecolor="black", alpha=0.5)
    plt.show()

    #Test
    statistic, critical, significance = sp.anderson_ksamp([empiricos,num])
    if (statistic>critical[2]):
        resultado= 'No pasa el test'
    else:
        resultado='Pasa el test'
    print("Statistic: ", statistic)
    print("Critical: ", critical[2])
    print(resultado)

uniform(0,20)
#exponencial(1)
#gamma(5, 2)
#normal(0, 4)
#pascal(10, 0.4)
#binomial(15,0.2)
#hiper(50, 20, 0.7)
#poisson(5)
#empirica()