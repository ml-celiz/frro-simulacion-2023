import math
import random
import matplotlib.pyplot as plt
import numpy as np

def initialize():
    global time, int_level, time_last_level, total_ordering_cost, area_holding, area_shortage, time_next_event

    time = 0.0
    int_level = initial_inv_level
    time_last_level = 0.0
    total_ordering_cost = 0.0
    area_holding = 0.0
    area_shortage = 0.0
    time_next_event = [0] * (num_events + 1)
    time_next_event[1] = 10**30
    time_next_event[2] = time + math.exp(mean_interdemand)
    time_next_event[3] = num_months
    time_next_event[4] = 0.0

def order_arrival():
    global int_level, time, time_next_event

    int_level += amount
    time_next_event[1] = 10**30

def demand():
    global int_level, time, time_next_event

    size_demand = random_integer(prob_distrib_demand)
    int_level -= size_demand
    time_next_event[2] = time + math.exp(mean_interdemand)

def evaluate():
    global int_level, time, time_next_event, total_ordering_cost, amount

    if int_level < smalls:
        amount = bigs - int_level
        total_ordering_cost += setup_cost + (incremental_cost * amount)
        time_next_event[1] = time + random.uniform(minlag, maxlag)
    time_next_event[4] = time + 1.0

def report():
    global int_level, time, time_next_event, total_ordering_cost, area_holding, area_shortage

    avg_ordering_cost = total_ordering_cost / num_months
    avg_holding_cost = (holding_cost * area_holding) / num_months
    avg_shortage_cost = shortage_cost * area_shortage / num_months
    avg_tot_cost = avg_ordering_cost + avg_holding_cost + avg_shortage_cost

    ordering_cost_results.append(avg_ordering_cost)
    holding_cost_results.append(avg_holding_cost)
    shortage_cost_results.append(avg_shortage_cost)
    total_cost_results.append(avg_tot_cost)
    time_results.append(time)

def update_time_avg_stats():
    global time, time_last_event, area_shortage, area_holding
    
    time_last_event = time
    time_since_last_event = time - time_last_event
    if int_level < 0:
        area_shortage -= (int_level * time_since_last_event)
    elif int_level > 0:
        area_holding += (int_level * time_since_last_event)

def random_integer(prob_distrib):
    r = random.uniform(0, 1)
    cumulative_prob = 0.0
    for i, prob in enumerate(prob_distrib):
        cumulative_prob += prob
        if r <= cumulative_prob:
            return i
    return len(prob_distrib) - 1

#Crear listas vacías para almacenar los resultados
ordering_cost_results = []
holding_cost_results = []
shortage_cost_results = []
total_cost_results = []
time_results = []

def main():
    global initial_inv_level, num_months, num_policies, num_values_demand, mean_interdemand, setup_cost, incremental_cost
    global holding_cost, shortage_cost, minlag, maxlag, prob_distrib_demand, smalls, bigs, num_events, time

    #Especificar el número de eventos para la función de temporización
    num_events = 4

    initial_inv_level = int(input("Ingrese nivel de inventario inicial: "))
    num_months = int(input("Ingrese el número de meses de duración de la simulación: "))
    num_policies = int(input("Ingrese el número de políticas de inventario: "))
    num_values_demand = int(input("Ingrese el número de valores de demanda: "))
    mean_interdemand = float(input("Ingrese el tiempo medio entre demanda (meses): "))
    setup_cost = float(input("Ingrese el costo de configuración: "))
    incremental_cost = float(input("Ingrese el costo incremental: "))
    holding_cost = float(input("Ingrese el costo de mantenimiento: "))
    shortage_cost = float(input("Ingrese el costo por faltante: "))
    minlag = float(input("Ingrese el rango mínimo de retraso de entrega (meses): "))
    maxlag = float(input("Ingrese el rango máximo de retraso de entrega (meses): "))

    prob_distrib_demand = []
    print("Ingrese la función de distribución de tamaños de demanda:")
    for _ in range(num_values_demand):
        prob = float(input())
        prob_distrib_demand.append(prob)

    print("Sistema de inventario de un solo producto")
    print("Nivel de inventario inicial:", initial_inv_level, "artículos")
    print("Número de tamaños de demanda:", num_values_demand)
    print("Función de distribución de tamaños de demanda:", prob_distrib_demand)
    print("Tiempo medio entre demanda:", mean_interdemand, "meses")
    print("Rango de retraso de entrega:", minlag, "a", maxlag, "meses")
    print("Duración de la simulación:", num_months, "meses")
    print("k =", setup_cost, "i =", incremental_cost, "h =", holding_cost, "pi =", shortage_cost)
    print("Número de políticas:", num_policies)

    for _ in range(num_policies):
        smalls = int(input("Ingrese el valor de smalls para la política actual: "))
        bigs = int(input("Ingrese el valor de bigs para la política actual: "))

        initialize()

        while time < num_months:
            next_event_type = time_next_event.index(min(time_next_event[1:]))
            time = time_next_event[next_event_type]

            if next_event_type == 1:
                update_time_avg_stats()
                order_arrival()
            elif next_event_type == 2:
                update_time_avg_stats()
                demand()
            elif next_event_type == 4:
                update_time_avg_stats()
                evaluate()

        if next_event_type == 3:
            report()

    #Convierte las listas de resultados en matrices numpy para un análisis más fácil
    ordering_cost_results = np.array(ordering_cost_results)
    holding_cost_results = np.array(holding_cost_results)
    shortage_cost_results = np.array(shortage_cost_results)
    total_cost_results = np.array(total_cost_results)
    time_results = np.array(time_results)

    #Graficas de las medidas de rendimiento
    plt.title('Promedio de costos en 10 corridas s=2 S=80') 
    plt.plot(time_results, ordering_cost_results, label='Costo de Orden')
    plt.xlabel('Tiempo de Simulación (meses)')
    plt.ylabel('Costo')
    plt.show()

    plt.title('Promedio de costos en 10 corridas s=2 S=80') 
    plt.plot(time_results, holding_cost_results, label='Costo de Mantenimiento')
    plt.xlabel('Tiempo de Simulación (meses)')
    plt.ylabel('Costo')
    plt.show()

    plt.title('Promedio de costos en 10 corridas s=2 S=80') 
    plt.plot(time_results, shortage_cost_results, label='Costo de Faltante')
    plt.xlabel('Tiempo de Simulación (meses)')
    plt.ylabel('Costo')
    plt.show()

    plt.title('Promedio de costos en 10 corridas s=2 S=80') 
    plt.plot(time_results, total_cost_results, label='Costo Total')
    plt.xlabel('Tiempo de Simulación (meses)')
    plt.ylabel('Costo')
    plt.show()
    
    #Analisis de los resultados
    print("Análisis de los resultados:")
    print("Costo de Orden máximo:", np.max(ordering_cost_results))
    print("Costo de Orden mínimo:", np.min(ordering_cost_results))
    print("Costo de Orden promedio:", np.mean(ordering_cost_results))
    print("Costo de Mantenimiento máximo:", np.max(holding_cost_results))
    print("Costo de Mantenimiento mínimo:", np.min(holding_cost_results))
    print("Costo de Mantenimiento promedio:", np.mean(holding_cost_results))
    print("Costo de Faltante máximo:", np.max(shortage_cost_results))
    print("Costo de Faltante mínimo:", np.min(shortage_cost_results))
    print("Costo de Faltante promedio:", np.mean(shortage_cost_results))
    print("Costo Total máximo:", np.max(total_cost_results))
    print("Costo Total mínimo:", np.min(total_cost_results))
    print("Costo Total promedio:", np.mean(total_cost_results))

#Ejecutar la función principal
main()
