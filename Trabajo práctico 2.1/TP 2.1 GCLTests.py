import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from scipy.stats import chisquare
import math


#Tests
#Test Chi Cuadrado
def chi2():
    salto=1/k
    listaFA = np.array([0] * k)
    
    for i in numeros:
        intervalo = 0
        for j in np.arange(0,1,salto):
            if j < i < j+salto:
                listaFA[intervalo] += 1 
                break
            intervalo += 1

    print(listaFA)
    listaFr = listaFA/n
    #Grafica frecuencia relativa
    plt.title('Frecuencia relativa de los números generados por cada intervalo')
    plt.bar(range(0,k),(listaFr))
    plt.xlabel("Intervalo")
    plt.ylabel("Frecuencia absoluta")
    plt.ylim(0,max(listaFr)*2)
    plt.xlim(-1,k)   
    plt.show()

    sumatoriaFrecuencias = 0
    for frec in listaFA:
        print(frec, " ", n, " ", k)
        sumatoriaFrecuencias += (frec-(n/k))**2

    chicuadrado = (k/n)*(sumatoriaFrecuencias)

    print("X^2 = ",chicuadrado)

    valorTabla = stats.chi2.ppf(confianza,k-1)
    print("Valor tabla = ",valorTabla)

    if chicuadrado > valorTabla:
        print("No son uniformes")
    else:
        print("Son uniformes")

#Test Independencia de Corridas Arriba y Abajo de la Media
def corridas():
	media=np.mean(numeros)
	print(media)
	secuencia= []
	for i in range(len(numeros)):
		if numeros[i]<media:
			secuencia.append(0)
		else: 
			secuencia.append(1)


	c0=secuencia.count(0)
	c1=secuencia.count(1)
	num=secuencia[0]
	co=1
	for j in range(1,len(secuencia)):
		if (num!=secuencia[j]):
			co=co+1
			num=secuencia[j]
	print("Cantidad de ceros: ",c0)
	print("Cantidad de unos: ",c1)
	print("Cantidad de corridas: ",co)

	uco=(2*c0*c1)/n+1/2
	u2co=(2*c0*c1*(2*c0*c1-n))/(n**2*(n-1))
	z0=(co-uco)/u2co

	print("Valor estadistico: ",z0)

	zalfa=1.645

	if (-zalfa<z0<zalfa):
		print("Independientes")
	else:
		print("No son independientes.")

#Test de Autoccorelacion
def autocorrelacion():

	for w in range (0, len(numeros)):
	    numeros[w] = round(numeros[w],5)
	i=2
	l=5
	N=n
	rs=0
	M= math.trunc((N - i)/l -1)
	if ((i+(M+1)*l)<N):
		print (M, "M sirve")
	else:
		print (M, "M No sirve")


	while i+l <= N :
		rs = rs + numeros[i-1]*numeros[i-1+l]
		i=i+l
		
	R = 1/(M+1) * rs
	print ("R: ",R)

	D = round((math.sqrt(13*M + 7))/(12*(M+1)),3)

	Z = (R - 0.25)/D
	Z=abs(Z)
	print("D: ",D)
	print("Z: ",Z)
	print("Z tabla: 1.28")
	if (Z<1.28):
		print("Son aleatorios")
	else:
		print("No son aleatorios")

#Test de Kolmogorov-Smirnov
def smirnov():
    salto=1/k
    listaFA = np.array([0] * k)
    
    for i in numeros:
        intervalo = 0
        for j in np.arange(0,1,salto):
            if j < i < j+salto:
                listaFA[intervalo] += 1 
                break
            intervalo += 1
    listaFAA = []
    listaPA = []
    listaPAA = []
    FAA=0
    PA = 0
    PAA=0
    PEA=0
    PE=1/k
    listaPEA = []
    listaDMcalculado = []
    DM = 0
    for v in range(len(listaFA)):
        FAA= FAA + listaFA[v]
        listaFAA.append(FAA)
        PA = listaFA[v]/n
        listaPA.append(PA)
        PAA=PAA + PA
        listaPAA.append(PAA)
        PEA = PEA + PE
        listaPEA.append(PEA)
        listaDMcalculado.append(abs(PEA-PAA))

    print("Lista Probabilidades Esperadas Acumuladas: ")
    print(listaPEA)
    print("Lista Probabilidades Absolutas Acumuladas: ")
    print(listaPAA)
    DM=max(listaDMcalculado)
    DMcritico = 1.22/math.sqrt(n)
    print("DM: ",DM)
    print("DM Critico: ",DMcritico)
    if (DM<DMcritico):
        print("Son uniformes")
    else: 
        print("No son uniformes")
    print(stats.kstest(numeros, 'uniform'))

    plt.plot(listaPAA,linestyle='solid', color='r')
    plt.plot(listaPEA,linestyle='solid', color='g')
    plt.title("Probabilidades Acumuladas")
    plt.xlabel("Numeros")
    plt.ylabel("Probabilidad")
    plt.xlim(left=-2)
    plt.show()


#Menu
def menu():
	print ("Selecciona una opción")
	print ("\t1 - Test Chi Cuadrado GCL")
	print ("\t2 - Test de Corridas Arriba-Abajo de la Media GCL")
	print ("\t3 - Test Autocorrelación GCL")
	print ("\t4 - Test Smirnov GCL")
	print ("\t9 - Salir")


#Generador GLC
n = 1000
k = 10
a= 48271
c= 0
m= 2**31-1
x= 8763/n
numeros=[]
numeros.append(x)

confianza = 0.90

for i in range(n):
    x = ((a*x + c)%m)
    num=x/(m-1)
    numeros.append(num)
 
while True:
	menu()
	opcionMenu = input("Inserta un numero valor >> ")
	if opcionMenu=="1":
		chi2()
		input("Pulsa una tecla para continuar")
	elif opcionMenu=="2":
		corridas()
		input("Pulsa una tecla para continuar")
	elif opcionMenu=="3":
		autocorrelacion()
		input("Pulsa una tecla para continuar")
	elif opcionMenu=="4":
		smirnov()
		input("Pulsa una tecla para continuar")
	elif opcionMenu=="9":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")