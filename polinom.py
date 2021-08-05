import numpy as np
from functions import *


t = [0, 10, 15, 20, 22.5, 30]
vt = [0, 227.04, 362.72, 517.35, 602.97, 901.67]
tcari = 16
points = [2,3,4,5]
vtcari0 = 0

for i in points:
    [tx, vtx] = terdekat(t,vt, tcari, i)
    [a, vtcari] = interpredict(tx, vtx, tcari)
    print("Orde", i-1, " Nilai Kecepatan jatuh kepada t ke ", tcari, " = ", "%.2f"%vtcari)
    if vtcari0 == 0 : print("error = -")
    else: print("Error = ", "%.5f"%abs((vtcari - vtcari0) / vtcari * 100), "%")
    vtcari0 = vtcari
