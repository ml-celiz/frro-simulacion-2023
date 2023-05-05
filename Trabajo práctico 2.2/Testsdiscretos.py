import scipy.stats as sp
import numpy as np
import matplotlib.pyplot as plt

#Test Distribución Binomial
def testBinomial(data1,data2):
    stat, p = sp.wilcoxon(data1, data2)
    print('stat=%.3f, p=%.3f' % (stat, p))
    if p > 0.05:
        print('Probably the same distribution')
    else:
        print('Probably different distributions')

#Test Distribución Poisson
def testPoisson(data1,data2):
    stat, p = sp.wilcoxon(data1, data2)
    print('stat=%.3f, p=%.3f' % (stat, p))
    if p > 0.05:
        print('Probably the same distribution')
    else:
        print('Probably different distributions')
