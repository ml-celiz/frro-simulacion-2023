import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp
import random as rm
import matplotlib.pyplot as plt
import math
import numpy as np
import scipy.interpolate as si

n = 100000

#Distribución Empírica Discreta
def empirica ():
    empiricos=[]
    x = np.array([1,2,3,4,5,6,7,8])
    frec=[0.06, 0.15, 0.20 ,0.10, 0.18, 0.12, 0.06, 0.13]
    acum=[0.06, 0.21, 0.41, 0.51, 0.69, 0.81, 0.87, 1]
    for i in range (n):
        r = rm.uniform(0,1)
        for j in range (len(x)):
            if (r <= acum[j]):
                empiricos.append(x[j])
                break

    print("Media: ", np.mean(empiricos))
    print("Desvio: ", np.sqrt(np.var(empiricos)))
    print("Varianza: ", np.var(empiricos))
    plt.title("Distribucion Empirica Discreta")
    xnew = np.linspace(x.min(), x.max(), 300)
    spl = si.make_interp_spline(x, frec, k=3)
    frec_suavizada = spl(xnew)
    plt.plot(xnew, frec_suavizada, '--')
    plt.bar(x , frec, edgecolor="black", alpha = 0.6, color="darkgrey", width = 0.2, )
    plt.show()

empirica()
