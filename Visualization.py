
# # QUESTION 1

# a)  Make a plot of the so-called deltoid curve, which is defined parametrically by the equations, x = 2 cos θ + cos 2θ, y = 2 sin θ − sin 2θ, where 0 ≤ θ < 2π. Take a set of values of θ between zero and 2π and calculate x and y for each from the equations above, then plot y as a function of x.
# 




#Importing that packages that I will be using for this lab.
import matplotlib.pyplot as plt
import math
import numpy as np





#Values between 0 and 2pi
theata = np.linspace(0, 2*np.pi )





#Getting the x values 
x= 2* np.cos(theata)+ np.cos(2*theata)





#Getting the y values
y = 2*np.sin(theata)-np.sin(2*theata)





#Plotting the Deltoid Curve
f=plt.figure()
ax=f.add_subplot(1,1,1)
ax.plot(x,y)
plt.title("Deltoid Curve")
plt.show()


# # QUESTION 2

# b)  Taking this approach a step further, one can make a polar plot r = f(θ) for some function f by calculating r for a range of values of θ and then converting r and θ to Cartesian coordinates using the standard equations x = r cos θ, y = r sin θ. Use this method to make a plot of the Galilean spiral, r=θ2 for 0 ≤ θ ≤ 10π




#Values between 0 and 10pi
theata2= np.linspace(0, 10*np.pi, num=200)





#Range of values of theta
r=theata2**2


# In[12]:


#Getting the x and y values
x2=r*np.cos(theata2)
y2=r*np.sin(theata2)





#Plotting the figure
f=plt.figure()
ax2=f.add_subplot(1,1,1)
ax2.plot(x2,y2)
plt.title("Polar Plot")
plt.show()


# # QUESTION 3
# 

# Using the same method, make a polar plot of “Fey’s function”




#Getting the values from 0 to 24pi
theata3= np.linspace(0, 24*np.pi, num = 10000)





r2= np.exp(np.cos(theata3))-2*np.cos(4*theata3)+np.sin(theata3/12)**5 


# In[20]:


#Getting the x and y values
x3=r2*np.cos(theata3)
y3=r2*np.sin(theata3)





#Plotting the figure
f=plt.figure()
ax3=f.add_subplot(1,1,1)
ax3.plot(x3,y3)
plt.title("Fey's Function")
plt.show()


# # PLOTTING ON SAME LINE
# 




f, axes=plt.subplots(1,3, figsize=(20,20))
axes[0].plot(x3,y3, linestyle='--',color='r')
axes[0].set_title("Fey's Function")
axes[1].plot(x2,y2,linestyle=':',color='b')
axes[1].set_title("Polar Plot")
axes[2].plot(x,y, linestyle='--',color='pink')
axes[2].set_title("Deltoid Curve")
plt.show()

