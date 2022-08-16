import time

from tqdm import tqdm


def RABT (a, b):

    Q = (a + b) / 2
    w = 4 * Q / (3600 * pi * d[y] ** 2)
    Re = w * d[y] / v[j]
    if Re < 2320:
        λ = 64 / Re
    if Re < 10 * d[y] / k[u]:
        λ = 0.3164 / (Re ** 0.25)
    elif Re < 500 * d[y] / k[u]:
        λ = 0.11 * (68 / Re + k[u] / d[y]) ** 0.25
    else:
        λ = 0.11 * (k[u]/d[y]) ** 0.25
    ig = λ * w ** 2 / d[y] / 2 / g
    Ht = ig * L[o] + Ne * h0
    hn = an - bn * (Q / mn) ** 2
    hm = am[s] - bm[s] * Q ** 2 
    Hns = Ne * hn + km[r] * hm - dz[h]
    dh = Hns - Ht 
    #print (w, Q, Hns, Ht, a, b) 
    if abs(2 * dh / (Hns + Ht)) * 100 < EPS:
        #print (w, Q, Hns, Ht, abs(2 * dh / (Hns + Ht)) * 100)
        return
    elif dh > 0:
        return RABT (Q, b)
    else:
        return RABT (a, Q)
    

km = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] # 20 r

d = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.2] # 7 y
k = [0.0002, 0.0001, 0.00015, 0.00013, 0.00018, 0.00005] # 6 u
L = [10000, 16000, 26000, 40000, 64000, 100000, 159000, 252000, 399000, 631000, 1000000, 1585000, 2512000, 3982000, 6310000, 10000000] # 16 o
v = [0.00002, 0.000027, 0.0000365, 0.0000492, 0.0000663, 0.0000895, 0.0001207, 0.0001629, 0.0002198, 0.0002965, 0.0004, 0.0005398, 0.0007283 ] # 13 j
dz = [-150, -135, -120, -105, -90, -75, -60, -45, -30, -15, 0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150] # 21 h
h0 = 0
Q1 = 0
Q2 = 20000
EPS = 0.1
pi = 3.14
g = 9.81
an = 102.4
bn = 8.7817e-07
am = [566.8, 528.5, 351.3, 367.7, 317, 279.6, 305.4, 295.1, 293.7] # 9 s
bm = [0.00015542, 0.00049522, 0.00022509, 0.00018537, 0.000031709, 8.0256E-06, 0.000005596, 1.8752E-06, 8.7817E-07]
mn = 1
Ne = 0

start_time = float(time.time())

with open("test_data.txt", "r") as file: 
    for line in tqdm(file):
        r, y, u, o, j, h, s = map(int, line.split())
        RABT (Q1, Q2)
                                
finish_time = float(time.time())
print (finish_time - start_time)

