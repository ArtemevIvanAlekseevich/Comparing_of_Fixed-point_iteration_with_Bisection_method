import time


def RABT (a, b):
    Q = (a + b)/2
    w = 4 * Q / (3600 * pi * d ** 2)
    Re = w * d / v
    if Re < 2000:
        λ = 64 / Re
    elif Re < 10 * d / k:
        λ = 0.3164 / (Re ** 0.25)
    elif Re < 500 * d / k:
        λ = 0.11 * (68 / Re + k / d) ** 0.25
    else:
        λ = 0.11 * (k/d) ** 0.25
    ig = λ * w ** 2 / d / 2 / g
    Ht = ig * L + dz + Ne * h0
    hn = an - bn * (Q / mn) ** 2
    hm = am - bm * Q ** 2
    Hns = Ne * hn + km * hm
    dh = Hns - Ht    
    if abs(2 * dh/(Hns + Ht) * 100) < EPS:
        print (w, Q, Hns, Ht)
        return
    elif dh > 0:
        return RABT (Q, b)
    else:
        return RABT (a, Q)

km = 18
d = 0.5
k = 0.0002
L = 10 ** 7
v = 20 * (10 ** -6)
dz = 0
h0 = 0
Q1 = 0
Q2 = 10000
EPS = 0.05
pi = 3.14
g = 9.81
an = 102.4
bn = 3.7584E-06
am = 260.0
bm = 8.564 / (10 ** 5)
mn = 1
Ne = 0


start_time = float(time.time())
for i in range (100000):
    RABT (Q1, Q2)
finish_time = float(time.time())
print (finish_time - start_time)