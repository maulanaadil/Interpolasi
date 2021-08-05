import numpy as np
import matplotlib.pyplot as plt

# Data Nilai X dan Y
x = [5.0, 10.0, 15.0, 20.0]
y = [40.0, 30.0, 25.0, 40.0]

# Data yang dicari
xInput = 12.0

n = len(x) - 1

# Selisih Terbagi
ST = np.zeros((n + 1, n + 1))
ST[:,0] = y

# Penyelesaian
for k in range(1, n + 1):
    for i in range(0, n - k + 1):
        ST[i, k] = (ST[i + 1, k - 1] - ST[i,k-1]) / (x[i + k] - x[i])
print(ST)
plt.plot(ST)

p = ST[0, 0]
for i in range(1, n + 1):
    a = ST[0, i]

    for k in range(0, i):
        a = a * (xInput - x[k])

    p = p + a

## Memanggil hasil dari penyelesaian (Output)
print("Jadi waktu yang diperlukan adalah : ", p)
plt.show()
