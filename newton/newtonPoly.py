## module newTtonPoly

# Menghitung polinomial newton p saat x. Koefisien vektor 'a' dapat dihitung dengan fungsi coeffits
def evalPoly(a, xData, x):
    n = len(xData) - 1
    p = a[n]
    for k in range(1, n + 1):
        p = a[n - k] + (x - xData[n - k]) * p
    return p

# Menghitung koefisien polinom newton
def coeffts(xData, yData):
    m = len(xData)
    a = yData.copy()
    for k in range(1, m):
        a[k:m] = (a[k:m] - a[k - 1]) / (xData[k:m] - xData[k - 1])
    return a
