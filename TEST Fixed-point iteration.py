import time

from tqdm import tqdm


km = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] # 20 r
d = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.2] # 7 y
k = [0.0002, 0.0001, 0.00015, 0.00013, 0.00018, 0.00005] # 6 u
L = [10000, 16000, 26000, 40000, 64000, 100000, 159000, 252000, 399000, 631000, 1000000, 1585000, 2512000, 3982000, 6310000, 10000000] # 16 o
v = [0.00002 ,0.000027 ,0.0000365 ,0.0000492 ,0.0000663 ,0.0000895 ,0.0001207 ,0.0001629 ,0.0002198 ,0.0002965 ,0.0004 ,0.0005398 ,0.0007283 ] # 13 j
dz = [-150, -135, -120, -105, -90, -75, -60, -45, -30, -15, 0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150] # 21 h
h0 = 0
K1 = 1.426
K2 = 3.154
EPS = 0.05
pi = 3.14
g = 9.81
an = 102.4
bn = 3.7584E-06
am = [566.8, 528.5, 351.3, 367.7, 317, 279.6, 305.4, 295.1, 293.7] # 9 s
bm = [0.00015542, 0.00049522, 0.00022509, 0.00018537, 0.000031709, 8.0256E-06, 0.000005596, 1.8752E-06, 8.7817E-07]
mn = 1
Ne = 0
T = 0

start_time = float(time.time())

with open("test_data.txt", "r") as file: 
    for line in tqdm(file):
        r, y, u, o, j, h, s = map(int, line.split())
        A = km[r] * am[s] - dz[h]
        B = (pi * d[y] ** 2) ** 2 * bm[s] * km[r] * 3600 ** 2 / 16
        w1 = 10 * v[j] / k[u]
        C = 0.11 * k[u]** 0.25 * L[o] /(2 * g * d[y] ** 1.25)
        b = 68 * v[j] / k[u]
        e1 = A - C * (b * w1 ** 7 + w1 ** 8) ** 0.25 - B * w1 ** 2
        if e1 < 0:
            w2 = 2320 * v[j] / d[y] 
            d2 = 0.3164 * v[j] ** 0.25 * L[o] / (2 * g * d[y] ** 1.25)
            e2 = A - d2 * w2 ** 1.75 - B * w2 ** 2
            if e2 < 0:
                б = 64 * v[j] / d[y] ** 2 * L[o] / 2 / g
                D = б ** 2 + 4 * B * A
                w = (-б + D ** 0.5) / (2 * B)
                Ht = 64 * v[j] / d[y] ** 2 * L[o] / (2 * g) * w
                
            else:
                б = 0.3164 * v[j] ** 0.25 / d[y] ** 1.25 * L[o] / 2 / g
                β = б / B
                γ = A / B
                e3 = γ - 2 * β ** 8
                if e3 < 0:
                    t1 = (γ / (β * K1)) ** (1 / 7)
                    t2 = (γ / (β + t1)) ** (1 / 7)
                    t3 = (γ / (β + t2)) ** (1 / 7)
                    w = (γ / (β + t3)) ** (1 / 1.75)
                    Ht = 0.3164 / (w * d[y] / v[j]) ** 0.25 * L[o] / d[y] * w ** 2 /(2 * g)
                    
                else:
                    t1 = (γ / K1) ** (1 / 8)
                    t2 = (γ / (1 + β / t1)) ** (1 / 8)
                    t3 = (γ / (1 + β / t2)) ** (1 / 8)
                    w = (γ / (β + t3)) ** (1 / 1.75)
                    Ht = 0.3164 / (w * d[y] / v[j]) ** 0.25 * L[o] / d[y] * w ** 2 /(2 * g)
                    
        else:
            w2 = 500 * w1
            d1 = 0.11 * 68 ** 0.25 * v[j] ** 0.25 * L[o] / (2 * g * d[y] ** 1.75)
            c1 = B + 0.11 * k[u] ** 0.25 / d[y] ** 1.75 * L[o] / (2 * g)
            e2 = A - d1 * w2 ** 1.75 - c1 * w2 ** 2
            if e2 < 0:
                w1 = (A / (B + C * K2 ** 0.25)) ** 0.5
                w2 = (A / (B + C * (1 + b / w1) ** 0.25)) ** 0.5
                w3 = (A / (B + C * (1 + b / w2) ** 0.25)) ** 0.5
                w = (A / (B + C * (1 + b / w3) ** 0.25)) ** 0.5
                Ht = 0.11 * (68 / (d[y] * w / v[j]) + k[u] / d[y]) ** 0.25 * L[o] / d[y] * w ** 2 / (2 * g)
                
            else: 
                w = (A / (B + 0.11 * k[u] ** 0.25 * L[o] / (d[y] ^ 1.25 * 2 * g))) ** 0.5
                Ht = 0.11 * (k[u] / d[y]) ** 0.25 * L[o] / d[y] * w ** 2/ (2 * g)
                
        #print(w, A - B * w ** 2, Ht, w * d[y] / v[j] )                    
finish_time = float(time.time())
print (finish_time - start_time)