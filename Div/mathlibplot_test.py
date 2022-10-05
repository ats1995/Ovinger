import matplotlib.pyplot as plt
import numpy as np

x_cor = np.linspace(1,10,11)
y_cor = x_cor**2

plt.plot(x_cor,y_cor)
plt.show()