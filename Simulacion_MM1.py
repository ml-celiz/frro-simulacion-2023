import sys
import numpy as np
import random as rm
import matplotlib.pyplot as plt
import math
import statistics

NumEventos = 2 #Tipos de eventos (arribos / llegadas)
#Estados del servidor: BUSY=opcupado IDLE=libre
BUSY = 1 
IDLE = 0
QLIMIT = 100000 #Limite de cola, infinito


def Inicializar():
    global TEA, Reloj,TotalReloj, TiempoProxEvento,AreaS, EstadoServidor, ClientesCompletaronDemora, DemoraTotal, AreaQ, AreaEstadoServidor, TipoProxEvento, CantDemorasNecesarias, CantEnCola, TS, TiempoUltimoEvento, TiempoArribo, CantEnSistema
    Reloj = 0
    EstadoServidor = IDLE
    TipoProxEvento = 0
    ClientesCompletaronDemora = 0 #Cantidad de clientes que completaron la cola
    CantEnCola = 0 #Cantidd de clientes en cola
    EstadoServidor = 0
    CantEnSistema = 0 #Cantidad de clientes en el sistema
    AreaQ = 0
    AreaS = 0
    AreaEstadoServidor = 0
    Reloj = 0
    TotalReloj = 0
    TiempoUltimoEvento = 0 #Tiempo del último evento
    DemoraTotal = 0 #Demora total
    TiempoArribo = np.zeros([CantDemorasNecesarias+1])
    TiempoProxEvento = np.zeros([NumEventos+1])
    TiempoProxEvento[1] = Reloj + np.random.exponential(1/TEA)
    TiempoProxEvento[2] = 10**30

def Tiempos():
    global Reloj, TipoProxEvento
    MinTiempoProxEvento = 10**29
    TipoProxEvento = 0

    for i in range(1,NumEventos+1):
        if TiempoProxEvento[i] < MinTiempoProxEvento:
            MinTiempoProxEvento = TiempoProxEvento[i]
            TipoProxEvento = i

    if (TipoProxEvento > 0):
        Reloj = TiempoProxEvento[TipoProxEvento]
    else:
        print("La lista de eventos está vacía en el momento: ", Reloj, " TipoProxEvento == 0, error en Tiempos")
        sys.exit()
        
def Arribo():
    global EstadoServidor,TiempoArribo, DemoraTotal, ClientesCompletaronDemora, TiempoProxEvento, CantEnCola, TS, CantEnSistema 
    TiempoProxEvento[1] = Reloj + np.random.exponential(1/TEA)
    CantEnSistema += 1

    if EstadoServidor == BUSY:    
        CantEnCola += 1   
        TiempoArribo[CantEnCola] = Reloj   
    else:
        Demora = 0
        DemoraTotal = DemoraTotal + Demora
    
        ClientesCompletaronDemora = ClientesCompletaronDemora + 1

        EstadoServidor = BUSY

        TiempoProxEvento[2] = Reloj + np.random.exponential(1/TS)
    
def Partida():
    global CantEnCola, DemoraTotal,ClientesCompletaronDemora, EstadoServidor, TiempoProxEvento, Reloj, TiempoArribo, CantEnSistema
    
    CantEnSistema -= 1 
    if (CantEnCola == 0):
        EstadoServidor = IDLE
        TiempoProxEvento[2] = 10**30
    else:
        CantEnCola = CantEnCola - 1

        Demora = Reloj - TiempoArribo[1]
        DemoraTotal = DemoraTotal + Demora

        ClientesCompletaronDemora += 1
        TiempoProxEvento[2] = Reloj + np.random.exponential(1/TS)

        for I in range(1,CantEnCola+1):
            TiempoArribo[I] = TiempoArribo[I+1]

def Actualizar():
    global TiempoUltimoEvento, AreaQ, AreaS, AreaEstadoServidor, Reloj,TotalReloj, CantEnSistema
    
    TotalReloj += TiempoUltimoEvento
    TiempoDesdeUltimoEvento = Reloj - TiempoUltimoEvento
    TiempoUltimoEvento = Reloj
    AreaQ = AreaQ + CantEnCola * TiempoDesdeUltimoEvento
    AreaS = AreaS + CantEnSistema * TiempoDesdeUltimoEvento
    AreaEstadoServidor = AreaEstadoServidor + EstadoServidor * TiempoDesdeUltimoEvento

def Reporte():
    global ClientesCompletaronDemora

    PromDemoraCola = DemoraTotal/ClientesCompletaronDemora
    PromCantEnCola = AreaQ/Reloj
    PromCantEnSistema = AreaS/Reloj
    PromTiempoEnSis = PromDemoraCola+1/TS
    UtilizacionServidor = AreaEstadoServidor/Reloj
    return [PromCantEnCola,PromDemoraCola, UtilizacionServidor, PromCantEnSistema,PromTiempoEnSis]

def Simulacion():
    global ClientesCompletaronDemora, CantDemorasNecesarias

    Inicializar()
    while(ClientesCompletaronDemora < CantDemorasNecesarias):
        Tiempos()
        Actualizar()
        if (TipoProxEvento == 1):
            Arribo()
        elif (TipoProxEvento == 2):
            Partida()
        else:
            print ("Error in TipoProxEvento, Value =  ",TipoProxEvento)

    return Reporte()

if __name__ == '__main__':
    global TEA, TS, CantDemorasNecesarias

    TEAS = [25, 50, 75, 99, 125] #Tiempos entre arribos correspondientes al 25%, 50%, 75%, 100% y 125% de la tasa de servicio
    TS = 100 #Tiempo de servicio
    CantDemorasNecesarias = 10000 #Cantidad de clientes que deseo que completen el sistema
    for TEA in TEAS:

        PromClientesCola = (TEA**2)/(TS*(TS-TEA))
        PromDemoraCola = TEA/(TS*(TS-TEA))
        PromUtilizacionSv = TEA/TS
        PromClientesSistema = TEA/(TS-TEA)
        PromTiempoClienteEnSistema = 1/(TS-TEA)
        print(PromClientesCola, "  ",PromDemoraCola, "  ", PromUtilizacionSv,"  ",PromClientesSistema,"  ",PromTiempoClienteEnSistema)
        CliEnCola = []
        DemoraEnCola = []
        UtilizacionServidor = []
        CliEnSistema = []
        TiempoPromSistema = []

        n = 10 #Iteraciones totales

        for i in range(n):
            Simu = Simulacion()
            CliEnCola.append(Simu[0])
            DemoraEnCola.append(Simu[1])
            UtilizacionServidor.append(Simu[2])
            CliEnSistema.append(Simu[3])
            TiempoPromSistema.append(Simu[4])

        #Arrays para graficar
        listaCliEnCola = []
        listaDemoraEnCola = []
        listaUtilizacionServidor = []
        listaCliEnSistema = []
        listaTiempoPromSistema = []

        for i in range(n):
            CliEnCola_i = statistics.mean(CliEnCola[:i+1])
            listaCliEnCola.append([i,CliEnCola_i])

            demora_promedio_i = statistics.mean(DemoraEnCola[:i+1])
            listaDemoraEnCola.append([i,demora_promedio_i])

            UtilizacionServidor_i = statistics.mean(UtilizacionServidor[:i+1])
            listaUtilizacionServidor.append([i,UtilizacionServidor_i])

            CliEnSistema_i = statistics.mean(CliEnSistema[:i+1])
            listaCliEnSistema.append([i,CliEnSistema_i])

            TiempoPromSistema_i=statistics.mean(TiempoPromSistema[:i+1])
            listaTiempoPromSistema.append([i,TiempoPromSistema_i])
        
        #Graficas de las medidas de rendimiento
        plt.title('Prom. de clientes en cola con tasa de arribo del '+str(TEA)+'%') 
        x, y = zip(*[m for m in listaCliEnCola])
        plt.plot(x, y,color='b')
        plt.plot([PromClientesCola for i in range(n)], linestyle='dashed', color='black')
        plt.show()

        plt.title('Prom. de demora en cola con tasa de arribo del '+str(TEA)+'%') 
        x, y = zip(*[m for m in listaDemoraEnCola])
        plt.plot(x, y,color='g')
        plt.plot([PromDemoraCola for i in range(n)], linestyle='dashed', color='black')
        plt.show()

        plt.title('Utilización prom. del servidor con tasa de arribo del '+str(TEA)+'%') 
        x, y = zip(*[m for m in listaUtilizacionServidor])
        plt.plot(x, y,color='r')
        plt.plot([PromUtilizacionSv for i in range(n)], linestyle='dashed', color='black')
        plt.show()

        plt.title('Clientes en el sistema con tasa de arribo del '+str(TEA)+'%') 
        x, y = zip(*[m for m in listaCliEnSistema])
        plt.plot(x, y,color='c')
        plt.plot([PromClientesSistema for i in range(n)], linestyle='dashed', color='black')
        plt.show()

        plt.title('Tiempo prom. de clientes en el sistema con tasa de arribo del '+str(TEA)+'%') 
        x, y = zip(*[m for m in listaTiempoPromSistema])
        plt.plot(x, y,color='m')
        plt.plot([PromTiempoClienteEnSistema for i in range(n)], linestyle='dashed', color='black')
        plt.show()

