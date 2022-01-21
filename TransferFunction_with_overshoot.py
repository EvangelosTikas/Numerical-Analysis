import matplotlib.pyplot as plt
import numpy as np
from numpy import *
import cmath
import sympy
from sympy import *

import scipy as sp

s,t = symbols('s,t')


print('A / (x * ( pow(x,2) + 2*ζ*np.sqrt(A) * x + A))')
def y(s,b):
    return b / (s * (s ** 2 + 10*b * s + b))
def invL(F):
    return sympy.inverse_laplace_transform(F, s, t)
def invLap_y(s,A):
    return invL(y(s,A))
""" Create three cases for A = 1000,10,100 ans z = 0.158,0.5,1.58
"""
listz=np.r_[0.158, 0.5, 1.58]
listA = np.r_[1000, 100, 10]

for A in listA:
    a=1
    b=10*A
    c=A
    # calculate the discriminant
    d = (b**2) - (4*a*c)

    # find two solutions
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)

    print('The solution are {0:.2f} and {1:.2f}'.format(sol1,sol2))

    y1= y(s, A)
    # y1 = A / (s * (s ** 2 + 2 * z * sympy.sqrt(A) * s + A))  ## Also an implementation for not using a def_ function
    c0 = limit( (s*y1 ), s, 0)
    c1 = limit( ( (s -sol1)*y1 ), s, sol1)
    c2 = limit( (s -sol2)*y1 , s, sol2)
    print('Cosntants are C0: ',c0,'C1:',c1,'C2:',c2,'\n')



x = np.linspace(0.00001,1.1, 100)
fig, ax = plt.subplots()
for (A,i) in zip(listA,range(3)):
    a=A
    y_t =  invL(y(s,a).apart(s))

    ax.plot(x, invL(y(x,A)))
    print("y(t) = ",y_t,'\n')

plt.show()
