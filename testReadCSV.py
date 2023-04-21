from io import StringIO
import numpy as np

a = np.genfromtxt('data/ampl2.csv', delimiter=";", dtype=(float))[1:]
x = a[:, 0]
print(x[0])