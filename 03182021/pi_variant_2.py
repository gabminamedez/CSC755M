from random import random
from math import sqrt
import time

def pi_variant_2(n):
    inCount = 0

    for i in range(n):
        x = random()
        y = random()
        xSquare = x * x
        if sqrt(x**2 + y**2) < 1:
            inCount += 1

    return 4 * (float(inCount) / n)

samples = [10, 100, 1000, 10000]

t0 = time.time()
for s in samples:
    print("N = " + str(s) + ": " + str(pi_variant_2(s)))
t1 = time.time()
var2_time = t1 - t0
print("Time for 2nd variant: " + str(var2_time))