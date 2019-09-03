{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "def fun(a,b,c):\n",
    "    x=(-b+math.sqrt((b**2) - (4*a*c)))/2*a\n",
    "    x2 = (-b-math.sqrt((b**2) - (4*a*c)))/2*a\n",
    "    print(x)\n",
    "    print(x2)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-9.999894245993345e-13\n",
      "-0.999999999999\n"
     ]
    }
   ],
   "source": [
    "fun(0.001, 1000, 0.001)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "def funAgain(a, b, c):\n",
    "    x= (2*c)/( -b+math.sqrt(b**2 - (4*a*c)))\n",
    "    x2= (2*c)/( -b-math.sqrt(b**2 - (4*a*c)))\n",
    "    print (x)\n",
    "    print(x2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-1000010.5755125057\n",
      "-1.000000000001e-06\n"
     ]
    }
   ],
   "source": [
    "funAgain(0.001, 1000, 0.001)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "hf=1\n",
    "B=0.01\n",
    "\n",
    "for n in range (2):\n",
    "    E=hf(n+1/2)\n",
    "    "
   ]
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
