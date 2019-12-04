
# # Importing my packages


import numpy as np
import scipy.constants as cons
import astropy.constants as c
import astropy.units as u
import mpmath
import matplotlib.pyplot as plt


# A) Showed that the total energy per unit area radiated by a black body




W=((c.k_B)**4)/(4*np.pi**2 * (c.c)**2*(c.hbar)**3)


print(W)


# # Function Created

# B)  Write a program to evaluate the integral in this expression.




a = 1e-8 #starting point
b = (np.pi)/2 #endpoint
k=1
n= 1000
h = (b-a)/n #delta x
s=0


# Used integration by Trig Substitution


def Function(x):
    z=np.tan(x)
    integ =(z**3)*1/np.cos(x)**2/((np.exp(z)-1))
    return integ


# # Summation of Values of Function

# Created a for loop and added all the values together


for k in range (1,n):
       s += Function(a+k*h) 


# The value after running the for loop




s





Final= h*(0.5*Function(a)+0.5*Function(b)+ s)





print("This is the integral: ", Final)





Stefan_Boltzmann_constant= Final*W





print("The Stefan–Boltzmann constant is {r:1.2}".format(r = Stefan_Boltzmann_constant))





x = np.linspace(1e-8, np.pi/2)





z=np.tan(x)
y = Funny=(z**3)*1/np.cos(x)**2/((np.exp(z)-1))





f=plt.figure()
ax=f.add_subplot(1,1,1)
ax.plot(x,y)
plt.show()

