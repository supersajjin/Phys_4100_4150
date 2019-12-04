#Write Python programs to calculate the coefficients in the discrete Fourier transforms of the following 
#periodic functions sampled at N = 1000 evenly spaced points, and make plots of their amplitudes:



#Importing the packages
import numpy as np
import scipy as sc
from scipy import signal
import matplotlib.pyplot as plt



#Function to calculate the coefficients in the discrete Fourier transforms
def dft(y):
    N =1000
    c = np.zeros(N//2+1, complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*np.exp(-2j*np.pi*k*n/N) 
    return c


#Square Signal using Scipy
N= np.linspace(0,1, num =1000)
square= signal.square(2 * np.pi * 3 * N)

#plotting the spaced points vs square signal
plt.plot(N, square)
plt.title("Square-Wave")
plt.show()

transform = np.fft.rfft(square)#Transforming

transform = transform * np.conjugate(transform)#multiplying by conjugate

#Plotting
plt.plot(transform)
plt.title("Transformed Square-Wave")
plt.show()

#QUESTION 2 The sawtooth wave

yn = signal.sawtooth(2 * np.pi * 3 * N)#SAWTOOTH WAVE

#PLOTTING THE SAWTOOTH WAVE
plt.plot(yn)
plt.title("SAWTOOTH WAVE")
plt.show()

#TRANSFORMING
yn1=np.fft.rfft(yn)

#Multiplying by its conjugate
yn2=yn1*np.conjugate(yn1)

#PLOTTING
plt.plot(yn2)
plt.title("TRANSFORMED SAWTOOTH WAVE")
plt.show()

#Third Problem: The modulated sine wave

N=1000

n=np.arange(0,1000,step=1)
ynn= np.sin((np.pi*n)/N)*np.sin((20*np.pi*n)/N)

#PLOTTING MODULATED SINE WAVE
plt.plot(n,ynn)
plt.title("The modulated sine wave")
plt.show()


#Instead of using the built in function, i am using the function created called dft to transform
yn_Tran= dft(ynn)

#multiply by its conjugate
yn_Trans=  yn_Tran* np.conjugate(yn_Tran)

#PLOTTING TRANSFORMATION
plt.plot(yn_Trans)
plt.title("The modulated sine wave Transformed")
plt.show()

