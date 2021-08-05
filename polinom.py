import numpy as np
from functions import *


t = [5.0, 10.0, 15.0, 20.0]
vt = [40.0, 30.0, 25.0, 40.0]
tcari = 12
points = [2,3,4,5]
vtcari0 = 0

for i in points:
    [tx, vtx] = terdekat(t,vt, tcari, i)
    [a, vtcari] = interpredict(tx, vtx, tcari)
    print("Orde", i-1, " Nilai Kecepatan jatuh kepada t ke ", tcari, " = ", "%.2f"%vtcari)
    if vtcari0 == 0 : print("error = -")
    else: print("Error = ", "%.5f"%abs((vtcari - vtcari0) / vtcari * 100), "%")
    vtcari0 = vtcari
