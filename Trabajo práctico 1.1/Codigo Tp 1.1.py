import random as rm
import matplotlib.pyplot as plt
import numpy as np

#Parametros
numero=23
contador=0
corridas=5
tiradas=1000

#Crear "ruletas"
#"ruletas" tiene n elementos (dado por el parametro "corridas") donde cada uno es una sublista de m numeros aleatorios (dado por el parametro "tiradas") entre 0 y 36
ruletas=[] * corridas #Lista con el tamaño dado por "corridas"
for j in range(corridas): #En cada posicion de la lista coloco una...
    ruletas.append([] * tiradas) #Lista con el tamaño dado por "tiradas"
    for i in range(tiradas): #Para la posicion "j" de la lista, y la posicion "i" de la sublista (que se encuentra dentro de la primera)...
            ruletas[j].append(rm.randint(0, 36)) #Coloco un numero generado aleatoriamente entre 0 y 36

#Calculo de frecuencias relativas
frecuencias=[] * corridas #Lista con el tamaño dado por "corridas"
for j in range(corridas): #En cada posicion de la lista coloco una...
    frecuencias.append([] * tiradas) #Lista con el tamaño dado por "tiradas"
    contador=0 #Inicializo el contador
    for i in range(1, tiradas): #Para la posicion "j" de la lista, y la posicion "i" de la sublista...
        if ruletas[j][i-1] == numero: #Si la lista ruletas en la posicion "j" y la posicion "i-1" de la sublista es igual al "numero" que deseo estudiarle la frecuencia relativa...
            contador=contador+1 #Incremento el contador
            fr=contador/i #La frecuencia relativa del numero es igual al "contador" (veces que aparece el "numero") dividido el numero "i" (cantidad de numeros de la lista en ese momento)
            frecuencias[j].append(fr) #Coloco el valor de la frecuencia relativa en la posicion de la lista "j" de la sublista "i"
        else: #Si no
            fr=contador/i #Mientras el "numero" no aparezca el contador no incrementara por lo tanto el valor de la frecuencia relativa será el mismo y...
            frecuencias[j].append(fr) #Se seguira guardando el mismo valor en las siguientes posiciones

#Graficar frecuencias relativas
plt.axhline(1/37, color='k',ls="dotted", xmax=2000) #Frecuencia relativa esperada (linea de puntos)
plt.title("Frecuencia Relativa")
plt.xlabel("Cantidad de tiradas")
plt.ylabel("Frecuencia")
for i in range (0, corridas-1): #Recorro el arreglo "frecuencias"
    plt.plot(frecuencias[i],linestyle='solid')
plt.show()

#Calculo de medias aritmeticas
medias=[] * corridas 
auxmd=0 #Inicializo la media auxiliar
md=0 #Inicializo la media
for j in range(corridas): 
    medias.append([] * tiradas) 
    auxmd=0 #Inicializo la media auxiliar en cada iteracion "j"
    md=0 #Inicializo la media en cada iteracion "j"
    for i in range(1, tiradas): 
        auxmd=auxmd+ruletas[j][i-1] #La media auxiliar va a ser igual a la suma de la misma mas el elemento que se encuentra en la posicion de la lista "j" de la sublista "i" de ruletas.
        md=auxmd/i #La media es igual a la media auxiliar dividida el numero "i" (cantidad de numeros de la lista en ese momento)
        medias[j].append(md) 

#Graficar medias aritmeticas
plt.axhline(18, color='k',ls="dotted", xmax=2000) #Media esperada
plt.title("Media aritmética")
plt.xlabel("Cantidad de tiradas")
plt.ylabel("Media")
for k in range (0, corridas-1): #Recorro el arreglo "medias"
    plt.plot(medias[k],linestyle='solid')
plt.show()

#Calcular desvios
desvios=[] * corridas 
auxdsv=[] #Inicializo la lista del desvio auxiliar
dsv=0 #Inicializo el desvio
for j in range (corridas): 
    desvios.append([] * tiradas) 
    auxdsv.clear() #Inicializo el desvio auxiliar en cada iteracion "j"
    dsv=0 #Inicializo el desvio en cada iteracion "j"
    for i in range (1, tiradas): 
        auxdsv.append(ruletas[j][i-1]) #Agrego a la lista del desvio auxiliar el elemento que se encuentra en la posicion de la lista "j" de la sublista "i" de ruletas.
        dsv=np.std(auxdsv) #El desvio es igual a el desvio (metodo np.std) de la lista del desvio auxiliar
        desvios[j].append(dsv) 

#Graficar desvios
plt.axhline(10.67, color='k',ls="dotted", xmax=2000) #Desvio esperado
plt.title("Desvío estándar")
plt.xlabel("Cantidad de tiradas")
plt.ylabel("Desvío")
for i in range (0, corridas-1): #Recorro el arreglo "desvios"
    plt.plot(desvios[i],linestyle='solid')
plt.show()

#Calcular varianzas
varianzas=[] * corridas
auxvar=[] #Inicializo la lista de la varianza auxiliar
var=0 #Inicializo la varianza
for j in range (corridas):
    varianzas.append([] * tiradas)
    auxvar.clear() #Inicializo la varianza auxiliar en cada iteracion "j"
    var=0 #Inicializo la varianza en cada iteracion "j"
    for i in range (1, tiradas):
        auxvar.append(ruletas[j][i-1]) #Agrego a la lista de la varianza auxiliar el elemento que se encuentra en la posicion de la lista "j" de la sublista "i" de ruletas.
        var=np.var(auxvar) #La varianza es igual a la varianza (metodo np.var) de la lista de la varianza auxiliar
        varianzas[j].append(var)

#Graficar varianzas
plt.axhline(114, color='k',ls="dotted", xmax=2000) #Varianza esperada
plt.title("Varianza")
plt.xlabel("Cantidad de tiradas")
plt.ylabel("Varianza")
for i in range (0, corridas-1): #Recorro el arreglo "varianzas"
    plt.plot(varianzas[i],linestyle='solid')
plt.show()



