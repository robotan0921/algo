import numpy as np

a = 1.0
b = 1.0 / np.sqrt(2)
t = 1.0 / 4
p = 1.0

for i in range(10):
    an = (a + b) / 2
    bn = np.sqrt(a * b)
    tn = t - p * (a - an) * (a - an)
    pn = 2 * p

    a = an
    b = bn
    t = tn
    p = pn

    pi = (a + b) * (a + b) / (4 * t)
    print(i, pi)