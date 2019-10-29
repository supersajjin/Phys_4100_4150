
# coding: utf-8

# In[21]:


# Accuracy and Speed

# A)
#Importing the packages I will be using
import numpy as np
import matplotlib.pyplot as plt


def f(x): #Function created
    return x*(x-1)

x=1
delta = 10**-2
print("The value of the derivative", (f(x+delta)-f(x))/delta, "\n")

#B)
delta2=np.array([10**-4, 10**-6, 10**-8, 10**-10, 10**-12, 10**-14]) #creating an array of delta values

answer= ((f(x+delta2)-f(x))/delta2)

print("Here are the 6 values: ")
for i in np.arange(0,6):
    print(i+1,")", answer[i])
print("\n")#Want to skip a line

fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.plot(np.log10(delta2), answer)
ax.set_title("Result as a function of δ ")
plt.show()


#Exercise 4.4: Calculating integrals

#A)
#Number of slices
N=100

def integral_function(N):#Created a function
    h=2/N
    k=1
    integral=0
    for k in range(N):
        Xk=-1+(h*k)
        Yk= np.sqrt(1-Xk**2)
        integral +=h*Yk
    return(integral)
#Running the N=100 through my function
print("The answer is", integral_function(N), "when N = 100" , "\n")

print("\n")#want some space between what is being printed.

#B)

N2=500

print("The answer is ", integral_function(N2),"when N = 500", "\n" )

