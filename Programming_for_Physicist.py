# Programming for Physicist

import numpy as np

#Exercise 2.1

#Given information
Vo=0 #inital velocity
a= 9.8 #gravity
Yf=0 #final 

height=int(input("Enter the height of the tower in meters. "))


#Function used to calculate the height
def Equation(height):
    time= np.sqrt(2*height/a)
    return time


print ("It takes the ball {:4.2f} seconds to hit the ground.".format(Equation(height)))


#Use your program to calculate the time for a ball dropped from a 100 m high tower.

print ("A ball dropped from 100 m tower takes {:4.2f} seconds to hit the ground.".format(Equation(100)))

#Exercise 2.4:

v=float(input("Enter the speed the spaceship is traveling as a fraction of speed of light: "))

x=float(input("How many light years away is planet x? "))


x=x*9.461E15 #converts light years to meters
    
    
c=299792458 #speed of light
    
T0=(x/c)/3.154E7 #Converts time to years 
    
T=T0 / (np.sqrt(1-v**2)) 
    
print("The time it takes for the observer on Earth is {:4.2F} years".format(T), "\n",
      "The time it takes for the passanger on board the ship is {:4.2F} years".format(T0))
    
    

#Use your program to calculate the answers for a planet 10 light years away with v = 0.99c.
print("")
print("The program will calculate the answer for a planet 10 light years away with a velocity of 0.99c.")
x2= 10*9.461E15
To=(x2/c)/3.154E7
T2=To/(np.sqrt(1-0.99**2)) 

print("The time it takes for the observer on Earth is {:4.2F} years".format(T2), "\n",
      "The time it takes for the passanger on board the ship is {:4.2F} years".format(To))

