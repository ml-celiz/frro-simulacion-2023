import random as rm
import matplotlib.pyplot as plt
import numpy as np


n=1 #Numero por el que apuesto
contador=0
r=6 #Corridas
tiradas=1000
dineroIni=5000
apuestaIni=150

#Generar ruletas (6 corridas con 1000 tiradas c/u)
ruletas=[] * r
for j in range(r):
    ruletas.append([] * tiradas)
    for i in range(0, tiradas):
            ruletas[j].append(rm.randint(0, 36))

#Generar salidas
#Salidas es un array que simplifica el resultado de la ruleta con respecto al tipo de apuesta:
# Si sale un cero en la ruleta, salidas tendra un 0.
# Si sale un numero del 1 al 18, salidas tendra un 1.
# Si sale un numero del 19 al 36, salidas tendra un 2.
salidas = [] * r
for i in range(r):
    salidas.append([] * tiradas)
    for j in range (tiradas):
        num=ruletas[i][j]
        if(num==0):
            salidas[i].append(0)
        elif(num<=18 and num!=0):
            salidas[i].append(1)
        elif(num>18):
            salidas[i].append(2)

#Generar billeteras
billeteras= [] * r
for i in range(r):
    billeteras.append([] * tiradas)
    billeteras[i].append(dineroIni) #Por cada tirada, en cada posicion de la sublista se coloca el dinero inicial que es 5k

#Martingala
#Para cambiar entre apuestas con capital finito o infinito, se deben comentar o descomentar las lineas que aquí aclararemos.
#Al comentar las lineas estarías en capital infinito. Al descomentarlas estarías en capital finito.
frecuencias= [] * r
for i in range (r):
    #Comentar la siguiente linea.
    bancarrota=False
    apuesta=apuestaIni
    contador=0
    frecuencias.append([] * tiradas)
    for j in range(1, tiradas):
        #Comentar las siguientes dos lineas.
        if(bancarrota): #Si bancarrota=True la simulacion termina
            break
        #Reemplazar con "elif" para capital finito, reemplazar con "if" para capital infinito en la siguiente linea.
        elif (salidas[i][j]==n): #Si el numero es igual al que aposte -> "gano"
            contador +=1
            valor=(billeteras[i][j-1]+apuesta) #Valor = valor inicial + lo que aposte
            billeteras[i].append(valor)
            apuesta=apuestaIni #Si gano mi apuesta sigue igual
        else: #Si el numero no es igual al que aposte -> "pierdo"
            valor=(billeteras[i][j-1]-apuesta) #Valor = valor inicial - lo que aposte
            billeteras[i].append(valor)
            apuesta *=2 #Si pierdo doblego mi apuesta
            #Comentar las siguientes dos lineas.
            if (billeteras[i][j]<apuesta): #Si mi dinero es mejor que lo que apuesto, estoy en bancarrota
                bancarrota=True    
        fr=contador/(j) #Frecuencia = contador (cuantas veces "gane") / cantidad de numeros
        frecuencias[i].append(fr)

#Graficas p/ 1 simulacion
#Grafica frecuencia relativa
plt.title("Frecuencia Relativa")
plt.xlabel("Cantidad de tiradas")
plt.ylabel("Frecuencia")
plt.axhline(0.486, color='k',ls="dotted", xmax=tiradas)
plt.plot(frecuencias[0],linestyle='solid')
plt.show()

#Grafica frecuencia relativa en grafico de barras
plt.subplot(2,3,1)
n1=plt.bar(np.arange(len(frecuencias[0])), frecuencias[0])
plt.axhline(0.486, color='k',ls="dotted", xmax=tiradas)
plt.xlabel("Cantidad de tiradas")
plt.ylabel("Frecuencia")
plt.show()

#Graficar dinero
plt.title("Dinero en la Billetera")
plt.axhline(dineroIni, color='k',ls="dotted", xmax=tiradas)
plt.axhline(0, color='k',ls="dotted", xmax=tiradas)
plt.xlabel("Cantidad de tiradas")
plt.ylabel("Dinero")
plt.plot(billeteras[0],linestyle='solid')
plt.show()

#Graficas p/ 6 simulaciones
#Grafica frecuencia relativa
plt.title("Frecuencia Relativa")
plt.xlabel("Cantidad de tiradas")
plt.ylabel("Frecuencia")
plt.axhline(0.486, color='k',ls="dotted", xmax=tiradas)
for i in range (r):
    plt.plot(frecuencias[i],linestyle='solid')
plt.show()

#Grafica frecuencia relativa en grafico de barras
plt.subplot(2,3,1)
n1=plt.bar(np.arange(len(frecuencias[0])), frecuencias[0])
plt.axhline(0.486, color='k',ls="dotted", xmax=tiradas)
plt.xlabel("Cantidad de tiradas")
plt.ylabel("Frecuencia")

plt.subplot(2,3,2)
n1=plt.bar(np.arange(len(frecuencias[1])), frecuencias[1])
plt.axhline(0.486, color='k',ls="dotted", xmax=tiradas)
plt.xlabel("Cantidad de tiradas")
plt.ylabel("Frecuencia")

plt.subplot(2,3,3)
n1=plt.bar(np.arange(len(frecuencias[2])), frecuencias[2])
plt.axhline(0.486, color='k',ls="dotted", xmax=tiradas)
plt.xlabel("Cantidad de tiradas")
plt.ylabel("Frecuencia")

plt.subplot(2,3,4)
n1=plt.bar(np.arange(len(frecuencias[3])), frecuencias[3])
plt.axhline(0.486, color='k',ls="dotted", xmax=tiradas)
plt.xlabel("Cantidad de tiradas")
plt.ylabel("Frecuencia")

plt.subplot(2,3,5)
n1=plt.bar(np.arange(len(frecuencias[4])), frecuencias[4])
plt.axhline(0.486, color='k',ls="dotted", xmax=tiradas)
plt.xlabel("Cantidad de tiradas")
plt.ylabel("Frecuencia")

plt.subplot(2,3,6)
n1=plt.bar(np.arange(len(frecuencias[5])), frecuencias[5])
plt.axhline(0.486, color='k',ls="dotted", xmax=tiradas)
plt.xlabel("Cantidad de tiradas")
plt.ylabel("Frecuencia")

plt.show()

#Graficar dinero
plt.title("Dinero en la Billetera")
plt.axhline(dineroIni, color='k',ls="dotted", xmax=tiradas)
plt.axhline(0, color='k',ls="dotted", xmax=tiradas)
plt.xlabel("Cantidad de tiradas")
plt.ylabel("Dinero")
for i in range (r):
    plt.plot(billeteras[i],linestyle='solid')
plt.show()

