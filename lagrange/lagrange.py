import matplotlib.pyplot as plt
import numpy as np

# Nilai X Dan Y
x = [5.0, 10.0, 15.0, 20.0]
y = [40.0, 30.0, 25.0, 40.0]

m = len(x)

#Derajat dari fungsi
n = m - 1

xp = 5
yp = 0

xplt = np.linspace(x[0], x[-1])
yplt = []

for i in range(len(xplt)) :
    yp = 0
    for j in range(n + 1) :
        p = 1
        for k in range(n + 1) :
            if k != j :
                p *= (xplt[i] - x[k])/(x[j] - x[k])
        yp += y[j] * p
    yplt.append(yp)

print('Jadi nilai hampiram y : %.3f'%yplt[22])

plt.plot(x, y, 'bo')
plt.plot(xplt, yplt, 'r-')
plt.show()

