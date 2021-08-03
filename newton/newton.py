import numpy as np
import matplotlib.pyplot as plt
from newtonPoly import *

## Nilai Data X dan Data Y
xData = np.array([5.0, 10.0, 15.0, 20.0])
yData = np.array([40.0, 30.0, 25.0, 40.0])

a = coeffts(xData, yData)
print(" t    s_Interp    s_Exact")
print("-------------------------")

x = np.arange(12.0)
n = len(x)
y = np.zeros((n, 2))
yExact = np.zeros((n, 2))

for i in range(n):
    y[i, 0] = evalPoly(a, xData, x[i])
    yExact[i, 0] = 10 * x[i] + 0.5 * 2 * x[i] ** 2
    print('{:3.1f} {:9.5f} {:9.5f}'.format(x[i], y[i, 0], yExact[i, 0]))
plt.plot(xData, yData, 'o', x, y[:, 0], 'h-', x, yExact[:, 0], 's-')
plt.show()
