import numpy


def terdekat(t, vt, tcari, jml):
    tt = t[:]
    selindex = []
    closestvt = []
    for i in range(jml):
        daftar = []
        for j in range(len(tt)):
            daftar.append(abs(tt[j] - tcari))
        n = daftar.index(min(daftar))
        selindex.append(tt[n])
        tt.remove(tt[n])
    selindex.sort()
    for k in selindex: closestvt.append(vt[t.index(k)])
    return [selindex, closestvt]

def gaussJordan(A) :
    n = len(A)
    x = numpy.zeros(n)

    for k in range(n):
        pivot = A[k][k]
        A[k] = A[k]/pivot
        for i in range(n):
            if i == k: continue
            factor = A[i][k]
            for j in range(k, n+1) :
                A[i][j] = A[i][j] - factor * A[k][j]
            x = A[:, n]
            return (x)

def interpredict(t, vt, tcari) :
    matrixnya = numpy.zeros((len(t), len(t) + 1))
    for i in range(len(t)) :
        matrixnya[i, len(t)] = vt[i]
        for j in range(len(t)) :
            matrixnya[i, j] = t[i] ** j
    a = gaussJordan(matrixnya)
    vtcari = 0
    for i in range (len(a)):
        vtcari += a[i] * tcari ** i
    return[a, vtcari]
