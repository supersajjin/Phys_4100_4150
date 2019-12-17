import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits import mplot3d
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
#*****************************************************************
#***********************CONSTANTS*********************************

g = 9.81            #GRAVITY: m/s^2
Cd = 0.20           #drag coefficient
m= 0.43             #kg (MASS of football)
diameter = 0.1725   #meters
r= .1725/2          #Radius in meters or 0.09432414698 yards
A = np.pi*r**2      #FRONTal AREA if the football
p = 1.2754          #kg/m^3 AIR DENSITY
C= (Cd*p*A)/2       #drag force
Height = 2.0574     #meters
C2 = (0*p*A)/2      #NO DRAG
#I decided to include this as my starting point for my Y axis (polar)
#or Z axis (Spherical) because in reality, the football isn't thrown
#from the ground. I decided to use the average height of an NFL QB
#as my starting point. The average height is 81 inches which turns
#out to be 2.0574 meters

N=100
a=0                #Initial time in seconds
b=6                #Final time in seconds
h = (b-a)/N        #Step size parameter
time = np.arange(a,b, h)    #time in seconds



#TRANSFORM FROM METERS TO YARDS
def Yards(m):
    return m*1.094#yards




print('Hi. how far would you like to throw the football (in meters which will be converted to yards)?')

answer = float(input())                #Taking the user's input and changing it to an int.

print(answer, "in meters is", Yards(answer), "in yards.")

location = Yards(answer)                #Changing meters to yards. Will be used in my loop later on

print("At what angle would you like to throw it at? Please enter any angle from 10 to 80 degrees!")
angle = float(input())

def RANGE (X,angle ): #Using the range equation to solve for V without drag.
    theta= angle *np.pi/180       #The angle the football that the user entered. 
   
    velocity = np.sqrt((X *g)/np.sin(2*theta))
    return velocity

Vo = RANGE(answer, angle)       #This will give me an initial velocity. I will use this as my V1 when i use bisection method. 

print("The velocity that is produced when using the Range formula is", Vo, "m/s")

Vf = RANGE(answer, angle)+(RANGE(answer, angle)*.30) #This will be my V2 to be used in the bisection method. 


#I created a function to be used in the bisection method.

def function(Vo):
    theta= angle *np.pi/180 
    vxp=Vo*np.cos(theta)
    vyp=Vo*np.sin(theta)
    r2= np.array([0, vxp,Height, vyp] , dtype= float)
    

#THIS HAS Drag included!
    def polar (r, t):
        vxp = r[1]
        vyp = r[3]
        fvx2=-(C/m)*vxp*np.sqrt(vxp**2 + vyp**2) #ODE EQUATIONS for the X AXIS
        fvy2=-g-(C/m)*vyp*np.sqrt(vxp**2 + vyp**2)  #ODE EQUATIONS FOR THE Y AXIS
        return np.array([vxp,fvx2,vyp, fvy2], dtype = float)
    

    #lists to hold my points in the polar coordinates 
    xpolar=[]
    ypolar=[]

    #****************RUNGE KUTTA****************************************

    for t in time:
        xpolar.append(Yards(r2[0]))
        ypolar.append(Yards(r2[2]))

    
        k1= h*polar(r2, t)
        k2 = h*polar(r2+0.5*k1, t+0.5*h)
        k3 = h*polar(r2+0.5*k2, t + 0.5*h)
        k4 = h*polar(r2+ k3, t+h)
        r2= r2+ (k1+2*k2+2*k3+k4)/6
        ##THIS WILL MAKE SURE THAT THE LOOP STOPS IF Y goes below 0. 
        if Yards(r2[2])< 0:
            break

    return xpolar[-1] #HERE I AM RETURNING THE LAST VALUE AT on the X AXIS

print("This is the distance that the velocity produced: ", function(Vo),"yards")  #USING THE INITIAL SPEED to see what distace I got. 






#Using a loop to figure out the velocity needed to get to the location the user asked.
def bis(v1, function):
    fx = function(v1)
    if fx<location:
        while fx<location:
            v1=v1+.1
            fx=function(v1)
            
    elif fx>location:
        while fx>location:
            v1=v1-.1
            fx=function(v1)
            
    
    return v1 #RETURNING THE VELOCITY
       
velocity1 = bis (Vo, function)

print("This is the velocity given when using my loop:",velocity1,"m/s")

theta= angle *np.pi/180
vxp=velocity1*np.cos(theta)
vyp=velocity1*np.sin(theta)
r= np.array([0, vxp,Height, vyp] , dtype= float)

#THIS HAS Drag included!
def polar (r, t):
    vxp = r[1]
    vyp = r[3]
    fvx2=-(C/m)*vxp*np.sqrt(vxp**2 + vyp**2)
    fvy2=-g-(C/m)*vyp*np.sqrt(vxp**2 + vyp**2)
    return np.array([vxp,fvx2,vyp, fvy2], dtype = float)




#lists to hold my points in the polar coordinates DRAG
xpolar=[]
ypolar=[]


#****************RUNGE KUTTA****************************************

for t in time:
    xpolar.append(Yards(r[0]))
    ypolar.append(Yards(r[2]))

    
    k1= h*polar(r, t)
    k2 = h*polar(r+0.5*k1, t+0.5*h)
    k3 = h*polar(r+0.5*k2, t + 0.5*h)
    k4 = h*polar(r+ k3, t+h)
    r= r+ (k1+2*k2+2*k3+k4)/6
    ##THIS WILL MAKE SURE THAT THE LOOP STOPS IF Y goes below 0. 
    if Yards(r[2])< 0:
        break

FRAMES=np.size(ypolar)




#**************ENDING******************************************




#Bisection Function
def bis2(v1, v2, function):
    
    if function(v1)>location:
        xp=v1
        xn=v2
        
    elif function(v1)<location:
        xp=v2
        xn=v1 
        
    x3=0.5*(xp+xn)

    

    if function(x3)>location:
        xp=x3
        
    elif function(x3)<location:
        xn=x3
        
    
    x3=0.5*(xp+xn)
    tolerance = 1E-2

    while np.abs(xp-xn)>tolerance:
        
        if function(x3)> location:
            xp=x3
        elif function(x3)<location:
            xn=x3

        x3=0.5*(xp+xn)
    
    
    return x3

velocity2 = bis2 (Vo,Vf, function)

print("This is the velocity that is given when using the bisection method:", velocity2,"m/s")


theta= angle *np.pi/180
vxp=velocity2*np.cos(theta)
vyp=velocity2*np.sin(theta)
r2= np.array([0, vxp,Height, vyp] , dtype= float)


#lists to hold my points in the polar coordinates DRAG
xpolar2=[]
ypolar2=[]



#****************RUNGE KUTTA****************************************

for t in time:
    xpolar2.append(Yards(r2[0]))
    ypolar2.append(Yards(r2[2]))

    
    k1= h*polar(r2, t)
    k2 = h*polar(r2+0.5*k1, t+0.5*h)
    k3 = h*polar(r2+0.5*k2, t + 0.5*h)
    k4 = h*polar(r2+ k3, t+h)
    r2= r2+ (k1+2*k2+2*k3+k4)/6
    ##THIS WILL MAKE SURE THAT THE LOOP STOPS IF Y goes below 0. 
    if Yards(r2[2])< 0:
        break

FRAMES2=np.size(ypolar) 


#***************PLOTTING SECOND METHOD ******************************
#***************PLOTTING IN 2D ******************************
fig = plt.figure(figsize=(20,15))
ax1 = fig.add_subplot(2,2,1)
ax1.scatter(xpolar,ypolar,color= 'pink' )
football1 = plt.Circle((0, Height), radius=0.3, fc='brown')
ax1.add_patch(football1)
ax1.set_xlabel("X (Yards)")
ax1.set_ylabel("Y (Yards)")
ax1.set_title("Plot Using Loop")
ax2 = fig.add_subplot(2,2,2)
ax2.scatter(xpolar2,ypolar2,color= 'red' )
football2 = plt.Circle((0, Height), radius=0.3, fc='brown')
ax2.add_patch(football2)
ax2.set_xlabel("X (Yards)")
ax2.set_ylabel("Y (Yards)")
ax2.set_title("Plot Using BISECTION METHOD")


def init():
    football1.center = (0, Height)
    ax1.add_patch(football1)
    football2.center = (0, Height)
    ax2.add_patch(football2)
    return football1,

def animate(i):
    x, y = football1.center
    x = xpolar[i]
    y = ypolar[i]
    football1.center = (x, y)
    x1, y1 = football2.center
    x1= xpolar2[i]
    y1= ypolar2[i]
    return football1,

anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=FRAMES2, 
                               interval=5,
                               blit=True)
plt.show()


 


print("This is the distance produced when using my loop",function(velocity1))
print("this is the distance produced when using the bisection method", function(velocity2))


