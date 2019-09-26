{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Programming for Physicist"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Exercise 2.1: Another ball dropped from a tower\n",
    "\n",
    "A ball is dropped from a tower of height h with initial velocity zero. Write a program that asks the user to enter the height in meters of the tower and then calculates and prints the time the ball takes until it hits the ground, ignoring air resistance. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Given information\n",
    "Vo=0\n",
    "a= 9.8\n",
    "Yf=0\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Asking the user to enter the height of the tower"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "height=int(input(\"Enter the height in meters of the tower. \"))\n",
    "\n",
    "\n",
    "#Function used to calculate the height\n",
    "def Equation(height):\n",
    "    time= np.sqrt(2*height/a)\n",
    "    return time\n",
    "\n",
    "\n",
    "print (\"It takes the ball {:4.2f} seconds to hit the ground.\".format(Equation(height)))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use your program to calculate the time for a ball dropped from a 100 m high tower."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print (\"A ball dropped from 100 m tower takes {:4.2f} seconds to hit the ground.\".format(Equation(100)))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Exercise 2.4:\n",
    "\n",
    "A spaceship travels from Earth in a straight line at relativistic speed v to another planet x light years away. Write a program to ask the user for the value of x and the speed v as a fraction of the speed of light c, then print out the time in years that the spaceship takes to reach its destination (a) in the rest frame of an observer on Earth and (b) as perceived by a passenger on board the ship. Use your program to calculate the answers for a planet 10 light years away with v = 0.99c."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the speed the spaceship is traveling as a fraction of speed of light: .99\n",
      "How many light years away is planet x? 10\n",
      "The time it takes for the observer on Earth is 70.93 years \n",
      " The time it takes for the passanger on board the ship is 10.01 years\n"
     ]
    }
   ],
   "source": [
    "v=float(input(\"Enter the speed the spaceship is traveling as a fraction of speed of light: \"))\n",
    "\n",
    "x=float(input(\"How many light years away is planet x? \"))\n",
    "\n",
    "\n",
    "x=x*9.461E15 #converts light years to meters\n",
    "    \n",
    "    \n",
    "c=299792458 #speed of light\n",
    "    \n",
    "T0=(x/c)/3.154E7 #Converts time to years \n",
    "    \n",
    "T=T0 / (np.sqrt(1-v**2)) \n",
    "    \n",
    "print(\"The time it takes for the observer on Earth is {:4.2F} years\".format(T), \"\\n\",\n",
    "      \"The time it takes for the passanger on board the ship is {:4.2F} years\".format(T0))\n",
    "    \n",
    "    \n",
    "   \n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use your program to calculate the answers for a planet 10 light years away with v = 0.99c."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The time it takes for the observer on Earth is 70.93 years \n",
      " The time it takes for the passanger on board the ship is 10.01 years\n"
     ]
    }
   ],
   "source": [
    "x2= 10*9.461E15\n",
    "To=(x2/c)/3.154E7\n",
    "T2=To/(np.sqrt(1-0.99**2)) \n",
    "\n",
    "print(\"The time it takes for the observer on Earth is {:4.2F} years\".format(T2), \"\\n\",\n",
    "      \"The time it takes for the passanger on board the ship is {:4.2F} years\".format(To))\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
