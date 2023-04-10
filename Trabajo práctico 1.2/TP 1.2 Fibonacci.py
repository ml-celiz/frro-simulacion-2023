import random as rm
import matplotlib.pyplot as plt
import numpy as np

r=6
tiradas=1000
n=1
fibonacci=[]
a=0
b=150
fibonacci.append(b)
dineroIni=5000

#Generar sucesion fibonacci
for i in range(2,100): 
    c = a + b 
    a = b 
    b = c
    fibonacci.append(b)
print(fibonacci)

#Generar ruletas
ruletas=[] * r
for j in range(r):
    ruletas.append([] * tiradas)
    for i in range(0,tiradas):
            ruletas[j].append(rm.randint(0, 36))

#Generar salidas
#Salidas es un array que simplifica el resultado de la ruleta con respecto al tipo de apuesta:
#   Si sale un cero en la ruleta, salidas tendra un 0.
#   Si sale un numero del 1 al 18, salidas tendra un 1.
#   Si sale un numero del 19 al 36, salidas tendra un 2.
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
    billeteras[i].append(dineroIni)

# k es una variable que define la posicion en el arreglo de la secuencia de fibonacci
# Generar frecuencias y apuestas
#Para cambiar entre apuestas con capital finito o infinito, se deben comentar o descomentar las lineas que aqui aclararemos.
#Al comentar las lineas estarias en capital infinito. Al descomentarlas estarias en capital finito.
frecuencias=[] * r
for i in range (r):
    k=0
    apuesta=fibonacci[k]
    #Comentar la siguiente linea.
    bancarrota=False
    contador=0
    frecuencias.append([] * tiradas)
    for j in range (1,tiradas):
        #Comentar las siguientes dos lineas.
        if(bancarrota):
            break
        #Reemplazar con "elif" para capital finito, reemplazar con "if" para capital infinito en la siguiente linea.
        elif (salidas[i][j]==n):
            contador +=1
            valor=(billeteras[i][j-1]+apuesta)
            billeteras[i].append(valor)
            if(k<2):
                k=0
            else:
                k=k-2
            apuesta=fibonacci[k]
        else:
            valor=(billeteras[i][j-1]-apuesta)
            billeteras[i].append(valor)
            k=k+1
            apuesta = fibonacci[k]
            #Comentar las siguientes dos lineas.
            if (billeteras[i][j]<apuesta):
                bancarrota=True
        fr=contador/j
        frecuencias[i].append(fr)

#Graficas
plt.title("Frecuencia Relativa")
plt.xlabel("Cantidad de tiradas")
plt.ylabel("Frecuencia")
plt.axhline(0.486, color='k',ls="dotted", xmax=tiradas)
plt.plot(frecuencias[0],linestyle='solid')
plt.show()

plt.subplot(2,3,1)
n1=plt.bar(np.arange(len(frecuencias[0])), frecuencias[0])
plt.axhline(0.486, color='k',ls="dotted", xmax=tiradas)
plt.xlabel("Cantidad de tiradas")
plt.ylabel("Frecuencia")
plt.show()

plt.title("Dinero en la Billetera")
plt.axhline(dineroIni, color='k',ls="dotted", xmax=tiradas)
plt.axhline(0, color='k',ls="dotted", xmax=tiradas)
plt.xlabel("Cantidad de tiradas")
plt.ylabel("Dinero")
plt.plot(billeteras[0],linestyle='solid')
plt.show()

#Graficar frecuencia relativa
plt.title("Frecuencia Relativa")
plt.xlabel("Cantidad de tiradas")
plt.ylabel("Frecuencia")
plt.axhline(0.486, color='k',ls="dotted", xmax=tiradas)
for i in range (r):
    plt.plot(frecuencias[i],linestyle='solid')
plt.show()

#Graficar frecuencia relativa en codigo de barras
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
