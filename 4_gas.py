#!/usr/bin/env python
#############################################################################
# course:   Numerische Methoden D-PHYS
# exercise: assignment 4
# author:   Thomas Diggelmann <thomas.diggelmann@student.ethz.ch>
# date:     30.03.2015
#############################################################################
from numpy import *
from matplotlib.pyplot import *
from scipy.integrate import quad

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
figure(figsize=(12,8))
plot(x, U(x))
ylim(-150,20)
xlabel(r"$r$")
ylabel(r"$U(r)$")
title("assignment 4a")
grid(True)
savefig("part_a.pdf")

###############################
#                             #
# Plotten Sie den Integranden #
#                             #
###############################
figure(figsize=(12,10))
for T in linspace(150, 550, 20):
    plot(x, f(x, T), alpha=0.7, label="$f(x, T=%s)$" % T)
xlabel(r"$r$")
ylabel(r"$f(r)$")
legend(loc="upper right")
title("assignment 4b")
grid(True)
savefig("part_b.pdf")

# Integrationsintervall
a = 0.01
b = 10

#################################################
#                                               #
# Implementieren Sie eine Monte-Carlo Quadratur #
#                                               #
#################################################
def monte_carlo(f, a, b, N):
    # generate N samples in [a,b]
    r = random.rand(N)
    r = a + (b - a) * r
    # volume of domain [a,b]
    vol = (b - a) # im 1d fall: volumen = interval
    # eval function at sample pts
    y = f(r)
    # eval integral
    I = sum(y) / N
    # compute square of var
    if (N > 1):
        var2 = (sum(y**2)/N - I**2) / (N-1)
    else:
        var2 = 0.
    return I*vol, var2*vol**2

Iref, _ = quad(lambda r: f(r, 300), a, b)
print("B_2 (reference) = %f" % Iref)

I, _ = monte_carlo(lambda r: f(r, 300), a, b, 500000)
print("B_2 (monte-carlo) = %f" % I)
