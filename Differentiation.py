
import numpy as np
import astropy.constants as c
import mpmath
import matplotlib.pyplot as plt
import scipy.constants as sc
import astropy.units as u





#Positive Charge 
q1 = 1

#Negative Charge
q2 = -1 

#Distance between charges
r = 0.1





def Potential(q,r):
    return q/(4*np.pi*sc.epsilon_0*r)





print("The potential is",Potential(q1, r)*u.volt)





print("The potential is",Potential(q2, r)*u.volt)





#100 points
n = 100
#Array created to hold the potential
potential_Added= np.zeros([n,n])
dx=np.ones([n,n])
dy=np.ones([n,n])
x=np.linspace(-.5, .5, num = n)
y=x





#Will calculate the potential
xp=[-0.03,0.04]
yp=[0,0]
for i in range (n):
    for j in range(n):
        r1= np.sqrt((x[i] - xp[0])**2+(y[j]-yp[0])**2)
        r2= np.sqrt((x[i] - xp[1])**2+(y[j]-yp[1])**2)
        a= Potential(q1,r1)
        b= Potential(q2,r2)
        potential_Added[i][j]=a+b
        





#An array of potential that have been added and saved.
potential_Added





map=plt.imshow(potential_Added)
map.set_cmap("summer")
plt.title("Potential Density Plot")
plt.show()


# f(x+h)-f(x)/h





for i in range (0,n-1,5 ):
   for j in range(0,n-1,5):
       dx[i][j]=(potential_Added[i+1][j]-potential_Added[i-1][j])/(1/n)
       dy[i][j]=(potential_Added[i][j+1]-potential_Added[i][j-1])/(1/n)
       plt.arrow(x[i],y[j],1e-11*dx[i][j], 1e-11*dy[i][j],  )
       plt.xlim(-1,1)
       plt.ylim(-1,1)
plt.title("Visualiation of the field")
plt.show()
       

  

