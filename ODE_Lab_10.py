

#Will be plotting and animating a pendulum.
#Will also be using Runge Kutta 4th order to track the path of the pendulum. 

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
a =0
b=10
g= 9.81 #gravity
l = .1 #cm, length of the arm
h = 1E-2 #step
time = np.arange(a,b, h)#the time to be used in my for loop




r = np.array([179/180*np.pi, 0], dtype = float)#Array r


#Function that take r and t.

def f(r, t):
    
    theta = r[0]
    omega = r[1]

    ftheta = omega
    fomega = -1*(g/l)*np.sin(theta)

    return np.array([ftheta, fomega], dtype = float)

#A list that will hold the ftheta values
rpoints= [] #creating a list 

#A for loop 
for t in time:
    rpoints.append(r[0])
    
 #runge kutta 4th order   
    k1= h*f(r, t)
    k2 = h*f(r+0.5*k1, t+0.5*h)
    k3 = h*f(r+0.5*k2, t + 0.5*h)
    k4 = h*f(r+ k3, t+h)
    
    r= r+ (k1+2*k2+2*k3+k4)/6
    

#Plotting
plt.plot(time, rpoints)
plt.title("Pendulum")
plt.show()



##ANIMATING THE PENDULUM

fig = plt.figure(figsize=(5,5))
ax = plt.axes(xlim=(-4, 4), ylim=(-4,4))
pendulum=plt.Circle((0,0),radius=0.09,facecolor='black')



def init():
    pendulum.center = (0, 0)
    ax.add_patch(pendulum)
    return pendulum,

def animate(i):
    x = l*np.sin(rpoints[i])
    y = l*np.cos(rpoints[i])
    pendulum.center = (x, y)
    return pendulum,

anim = animation.FuncAnimation(fig, animate,
init_func=init,frames=360,interval=20,blit=True)
anim.save('pendulum.mp4')
plt.show()

