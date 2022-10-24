import matplotlib.pyplot as plt
import numpy as np

def funksjonen(tall):
    return tall**2 - tall*500

#x_koordinater = list()
#y_koordinater = list()

#for verdi in range(-1000, 1001):
    #x_koordinater.append(verdi)
    #y_koordinater.append(funksjonen(verdi))

#plt.plot(x_koordinater, y_koordinater)
#plt.show()

x_koordinater = np.arange(-1000, 1001, 1)
y_koordinater = funksjonen(x_koordinater)
plt.plot(x_koordinater, y_koordinater)
plt.show()