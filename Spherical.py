import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits import mplot3d
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation




#****************************************************************
#**************ANGLES FOR 3D PLOTS*******************************


#theta = some angle *np.pi/180 #degrees ANGLE FROM X AXIS in X-Y Plane
##45 goes to the right.
##90 keeps it in the middle
#180 moves it to the left

#Launch Angle
#phi = some angle*np.pi/180 #ANGLE from the Positive Z Axis


#*****************************************************************
#***********************CONSTANTS*********************************


g = 9.81 #GRAVITY: m/s^2
Cd = 0.47 #drag coefficient
Co=0 #FOR NOT AIR DRAG
m= 0.43#kg (MASS of football)
diameter = 0.1725 #meters
r= .1725/2 #Radius in meters or 0.09432414698 yards
A = np.pi*r**2
p = 1.2754 #kg/m^3 AIR DENSITY
Vo = 22 #m/s Initial Velocity.

C= (Cd*p*A)/2 #drag force


#I decided to include this as my starting point for my Y axis (polar)
#or Z axis (Spherical) because in reality, the football isn't thrown
#from the ground. I decided to use the average height of an NFL QB
#as my starting point. The average height is 81 inches which turns
#out to be 2.0574 meters

Height = 2.0574 #meters

N=1000
a=0 #Initial time
b=6 #Final time
h = (b-a)/N #Step size parameter

time = np.arange(a,b, h)

#TRANSFORM FROM METERS TO YARDS
def Yards(m):
    return m*1.094#yards

#**********************************************************
#**************************END********************************


print('Hi. how far would you like to throw the football (in meters which will be converted to yards)?')

answer = float(input())                #Taking the user's input and changing it to an int.

print(answer, "in meters is", Yards(answer), "in yards.")

location = Yards(answer)                #Changing meters to yards. Will be used in my loop later on

print("At what angle would you like to throw it at? Please enter any angle from 10 to 80 degrees!")
anglePhi = float(input())

phi = anglePhi*np.pi/180 #ANGLE from the Positive Z Axis

print("would you like to throw it northwest (180 degrees), northeast (45), or straight(90 degrees) down the field?") 
angleTheta = input()

#ANGLE FROM X AXIS in X-Y Plane
if angleTheta.lower() in ['northwest']:
    theta= 180*np.pi/180
elif angleTheta.lower() in ['northeast']:
    theta= 45*np.pi/180
elif angleTheta.lower() in ['straight']:
    theta= 90*np.pi/180

    
def RANGE (X,angle ): #Using the range equation to solve for V without drag.
    theta= angle *np.pi/180       #The angle the football that the user entered. 
   
    velocity = np.sqrt((X *g)/np.sin(2*theta))
    return velocity

Vo = RANGE(answer, anglePhi)       #This will give me an initial velocity. I will use this as my V1 when i use bisection method.









def functions(Vo):
    vx= Vo*np.cos(theta)*np.sin(phi)
    vy= Vo*np.sin(theta)*np.sin(phi)
    vz= Vo*np.cos(phi)

    #MY array that will hold my vx, vy, and vz.
    #will use the 0,0,Height as my initial conditions for the my
    #vx, vy, and vz. When I apply it to the for loop,
    #it will use my intial cooditions first. After the first iteration
    #the vx, vy, and vz will be used afterwards.
    r= np.array([0, vx,0, vy, Height, vz] , dtype= float)


    #3D: SPHERICAL COORDINATES FUCNTION
    def f(r, t):
        vx = r[1]
        vy = r[3]
        vz = r[5]

        fvx=((-C/m)*vx)*np.sqrt(vx**2+vy**2+vz**2)
        fvy=((-C/m)*vy)*np.sqrt(vx**2+vy**2+vz**2)
        fvz= -g-((C/m)*vz)*np.sqrt(vx**2+vy**2+vz**2)
   
        return np.array([vx,fvx,vy, fvy, vz, fvz], dtype = float)


    #Lists to hold my points in the spherical
    xpoints= [] 
    ypoints= []
    zpoints= []

    #************RUNGE KUTTA********************************************
    #*************3D****************************************************


    for t in time:
        xpoints.append(Yards(r[0]))
        ypoints.append(Yards(r[2]))
        zpoints.append(Yards(r[4]))
        k1 = h*f(r, t)
        k2 = h*f(r+0.5*k1, t+0.5*h)
        k3 = h*f(r+0.5*k2, t + 0.5*h)
        k4 = h*f(r+ k3, t+h)
        r= r+ (k1+2*k2+2*k3+k4)/6
    

        ##THIS WILL MAKE SURE THAT THE LOOP STOPS IF Z goes below 0.
        if Yards(r[4])< 0:
            break
    
    return ypoints[-1]





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
       
velocity1 = bis (Vo, functions)

print("The velocity needed to throw it in that direction is", velocity1, "m/s")



#*************SPHERICAL COORDINATES USES******************************
#*********************************************************************
#Getting the Velocity in the x,y, and z direction
#This will be used for the 3d (spherical) graph.

#WE PUT THE VELOCITY TO THE TEST!
vx= velocity1*np.cos(theta)*np.sin(phi)
vy= velocity1*np.sin(theta)*np.sin(phi)
vz= velocity1*np.cos(phi)

#MY array that will hold my vx, vy, and vz.
#will use the 0,0,Height as my initial conditions for the my
#vx, vy, and vz. When I apply it to the for loop,
#it will use my intial cooditions first. After the first iteration
#the vx, vy, and vz will be used afterwards.
r= np.array([0, vx,0, vy, Height, vz] , dtype= float)


#3D: SPHERICAL COORDINATES FUCNTION
def f(r, t):
    vx = r[1]
    vy = r[3]
    vz = r[5]

    fvx=((-C/m)*vx)*np.sqrt(vx**2+vy**2+vz**2)
    fvy=((-C/m)*vy)*np.sqrt(vx**2+vy**2+vz**2)
    fvz= -g-((C/m)*vz)*np.sqrt(vx**2+vy**2+vz**2)
   
    return np.array([vx,fvx,vy, fvy, vz, fvz], dtype = float)


#Lists to hold my points in the spherical
xpoints= [] 
ypoints= []
zpoints= []

#******************************************************************
#***********************END****************************************





#************RUNGE KUTTA********************************************
#*************3D****************************************************


for t in time:
    xpoints.append(Yards(r[0]))
    ypoints.append(Yards(r[2]))
    zpoints.append(Yards(r[4]))
    k1 = h*f(r, t)
    k2 = h*f(r+0.5*k1, t+0.5*h)
    k3 = h*f(r+0.5*k2, t + 0.5*h)
    k4 = h*f(r+ k3, t+h)
    r= r+ (k1+2*k2+2*k3+k4)/6
    

    ##THIS WILL MAKE SURE THAT THE LOOP STOPS IF Z goes below 0.
    if Yards(r[4])< 0:
        break
    

print("The ball thrown with a velocity of", velocity1,"m/s landed at", ypoints[-1],"yards!")


r2= np.array([0, vx,0, vy, Height, vz] , dtype= float)
def noDrag(r, t):
        vx = r[1]
        vy = r[3]
        vz = r[5]

        fvx=((-Co/m)*vx)*np.sqrt(vx**2+vy**2+vz**2)
        fvy=((-Co/m)*vy)*np.sqrt(vx**2+vy**2+vz**2)
        fvz= -g-((Co/m)*vz)*np.sqrt(vx**2+vy**2+vz**2)
   
        return np.array([vx,fvx,vy, fvy, vz, fvz], dtype = float)

xpoints2= [] 
ypoints2= []
zpoints2= []

for t in time:
    xpoints2.append(Yards(r2[0]))
    ypoints2.append(Yards(r2[2]))
    zpoints2.append(Yards(r2[4]))
    k1 = h*noDrag(r2, t)
    k2 = h*noDrag(r2+0.5*k1, t+0.5*h)
    k3 = h*noDrag(r2+0.5*k2, t + 0.5*h)
    k4 = h*noDrag(r2+ k3, t+h)
    r2= r2+ (k1+2*k2+2*k3+k4)/6
    

    ##THIS WILL MAKE SURE THAT THE LOOP STOPS IF Z goes below 0.
    if Yards(r2[4])< 0:
        break

print("The football will land at", ypoints2[-1],"yards when there is no airdrag.")




#*****************PLOTTING IN 3D

fig = plt.figure(figsize= (50, 25))# a figure with no axes
ax = p3.Axes3D(fig)
ax.set_title("FOOTBALL FIELD")
ax.set_xlim3d([-25, 25])
ax.set_xlabel('X')
ax.set_ylim3d([0, 100])
ax.set_ylabel('Y')
ax.set_zlim3d([0.0, 40.0])
ax.set_zlabel('Z')
ax.scatter3D(xpoints, ypoints, zpoints)


for angle in range(0, 360):
    ax.view_init(30, angle)
    plt.draw()
    plt.pause(0.0000001)

plt.show()


#This will plot the the football thrown with no AIR Drag
fig1 = plt.figure(figsize= (50, 25))# a figure with no axes
ax1 = p3.Axes3D(fig1)
ax1.set_title("FOOTBALL FIELD with NO AIR DRAG")
ax1.set_xlim3d([-25, 25])
ax1.set_xlabel('X')
ax1.set_ylim3d([0, 100])
ax1.set_ylabel('Y')
ax1.set_zlim3d([0.0, 40.0])
ax1.set_zlabel('Z')
ax1.scatter3D(xpoints2, ypoints2, zpoints2)
plt.show()