import numpy as np

def GCL(mod,semilla,cantidadGenerada,a,c):

    listaAleatoria = []

    N = semilla
    for i in range (cantidadGenerada):
        N = (((a)* N + c) % mod)
        listaAleatoria.append(N)

    listaAleatoria = np.asarray(listaAleatoria)/2**32
    return (listaAleatoria)

def generarNumeros(n):
    return GCL(2**32,3298876,n,134775813,1)

hola = generarNumeros(1000)
print(hola)