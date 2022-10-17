from cmath import pi
from math import sqrt
import numpy as np

def euk_disk(x, y):
    return(np.sqrt(x**2+y**2))

def circ_area(r):
    return(pi*r*r)

def turbin_effekt(strom_x, strom_y, tetthet, turbin_effekt, diamater):
    energi = 0.5 * turbin_effekt * tetthet * circ_area(diamater/2) * sqrt(strom_x**2+strom_y**2)**3
    return(energi)