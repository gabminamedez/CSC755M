from math import sqrt
import time

def pi_variant_3(r):
    inCount = 0
    rSquare = r * r

    for xInt in range(r + 1):
        x = xInt / r
        xSquare = x * x
        for yInt in range(r + 1):
            y = yInt / r
            ySquare = y * y
            if sqrt(xSquare + ySquare) <= 1:
                inCount += 1

    return 4 * (float(inCount) / rSquare)

samples = [10, 100, 1000, 10000]

t0 = time.time()
for s in samples:
    print("N = " + str(s) + ": " + str(pi_variant_3(s)))
t1 = time.time()
var3_time = t1 - t0
print("Time for 3rd variant: " + str(var3_time))