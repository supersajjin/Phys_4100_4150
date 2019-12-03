
##Importing the libaries and packages needed to complete the lab
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

steps = 1000000#Number of steps the particle will take
i = 50 #x
j = 50 #y
L= 101 #Size of the Lattice

#Creating two lists for the x and y points
xpoints=[]
ypoints=[]






#Collecting the points by using a for loop
#In the loop, a random number between 1-4 will be chosen and decide where the particle will head next.
#The starting point for the particle is i=50 and j =50
for k in range(steps):
    
    
    xpoints.append(i)
    ypoints.append(j)

    choice = np.random.randint(1,5)
    
    
    
    if (choice ==1):#Go Right
        i +=1
        if (i==L):
            i-=1
        
       
    elif(choice == 2):#Go Left
        i -=1
        if(i==0):
            i+=1
        
    elif(choice == 3):#Go Up
        j += 1
        if (j==L):
            j-=1
      
    elif(choice == 4):#Go Down
        j -=1
        if (j==0):
            j+=1
   
    
    
    
    
##Animating the Random Walk

fig = plt.figure(figsize=(6,7))
ax = plt.axes(xlim=(0, 101), ylim=(0,101))
particle=plt.Circle((50,50),radius=2,facecolor='black')



def init():
    particle.center = (50, 50)
    ax.add_patch(particle)
    return particle,

def animate(k):
    xx = xpoints[k]
    yy = ypoints[k]
    
    particle.center = (xx, yy)
    return particle,

anim = animation.FuncAnimation(fig, animate,
init_func=init,frames=360,interval=20,blit=True)
anim.save('RandomWalk.mp4')

plt.show()





