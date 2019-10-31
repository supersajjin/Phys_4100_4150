
# coding: utf-8

# In[2]:


#Importing packages that will be used
import numpy as np
import matplotlib.pyplot as plt
import astropy.constants as c
import astropy.units as u

#Mass of electron
massE= c.m_e

#
V=20*u.eV #3.2043532416e-18
w = 1.0 *u.nm
#
hbar = c.hbar
V1= 20



E=np.linspace(0,20,num = 100)*u.eV
#def Y1(x):

#Main
def TANFun(x):
    first= (((w**2 * massE * x)/(2*hbar**2)).decompose()).value
    new = np.tan(np.sqrt(first))
    return new

y1=TANFun(E)
print(y1)
print("  ")


#EVEN
def Even(x):
    first = (V-(x))/(x)
    new = np.sqrt(first)
    return new

y2=Even(E)
print (y2)
print("  ")



#ODD
def Odd(x):
    new = -1*np.sqrt((x)/(V-(x)))
    return new
y3= Odd(E)
print(y3)
print("  ")
    
plt.title("WELL")
plt.plot(E,y1, color = 'red', label = "Y1")
plt.plot(E, y2, color = 'purple', label = "Y2: Even")
plt.plot(E, y3, color = 'green', label = "Y3: Odd")
plt.ylim([-10,10])
plt.xlim([0, 20])
plt.legend()
plt.show()






#Unitless EVEN
def EvenNew(x):
    v=20
    first = (v-x)/(x)
    new = np.sqrt(first)
    return new





#Unitless ODD
def OddNew(x):
    v=20
    new = -1*np.sqrt((x)/(v-x))
    return new





def FunctionOdd(x):
    Tan = TANFun(x)
    Y = OddNew(x)
    newValue = Tan-Y
    return newValue

def FunctionEven(x):
    Tan = TANFun(x)
    Y = EvenNew(x)
    newValue = Tan-Y
    return newValue

    #x1=2.5
    #x2=2.8

#Bisection Function
def bis(x1, x2, function):
    
    if function(x1)>0:
        xp=x1
        xn=x2
    elif function(x1)<0:
        xp=x2 
        xn=x1   

    print ("Xn is: ", xn*u.eV)
    print ("XP is: ", xp*u.eV)
    print("     ")
    print("     ")

    x3=0.5*(xp+xn)

    fx3= function(x3)

    if fx3>0:
        xp=x3
    elif fx3<0:
        xn=x3
    
    x3=0.5*(xp+xn)
    tolerance = 1E-6

    while np.abs(xp-xn) > tolerance:
        

        fx3= function(x3)

        if fx3>0:
            xp=x3
        elif fx3<0:
            xn=x3

        x3=0.5*(xp+xn)
        print("xp: ", xp*u.eV)
        print("xn: ", xn*u.eV)
    
    return x3



 
    
#Write a second program to calculate the values of the first six energy 
# levels in electron volts to an accuracy of 0.001 eV using binary search.

Eo=bis(1.5, 1.8,OddNew )

E1=bis(2.5,2.8, EvenNew)

E2= bis(7.0, 7.4, OddNew)

E3= bis(7.6, 7.8, EvenNew )

E4= bis(11.0, 11.8, OddNew)

E5= bis(18.5, 19.0, EvenNew)

Eo = ("{0:.3f}".format(Eo))
E1 = ("{0:.3f}".format(E1))
E2 = ("{0:.3f}".format(E2))
E3 = ("{0:.3f}".format(E3))
E4 = ("{0:.3f}".format(E4))
E5 = ("{0:.3f}".format(E5))

#6 energy levels
print(Eo*u.eV)
print(E1*u.eV)
print(E2*u.eV)
print(E3*u.eV)
print(E4*u.eV)
print(E5*u.eV)

