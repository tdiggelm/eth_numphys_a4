from numpy import *
from matplotlib.pyplot import *


def U(r, eps=140, sigma=0.3943):
    x = (sigma / (1.0*r))**6
    return 4.0*eps*(x**2 - x)


def f(r, T, kB=0.693):
    return r**2 * (1.0 - exp(-U(r)/(kB*T)))


x = linspace(0.2, 2, 500)

#############################
#                           #
# Plotten Sie das Potential #
#                           #
#############################


###############################
#                             #
# Plotten Sie den Integranden #
#                             #
###############################


# Integrationsintervall
a = 0.01
b = 10

I = 0.0
#################################################
#                                               #
# Implementieren Sie eine Monte-Carlo Quadratur #
#                                               #
#################################################

print("B_2 = %f" % I)
