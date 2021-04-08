import time

def pi_variant_1(r):
    inCount = 0
    rSquare = r * r

    for x in range(1, r + 1):
        xSquare = x * x
        for y in range(1, r + 1):
            ySquare = y * y
            if xSquare + ySquare <= rSquare:
                inCount += 1

    return 4 * (float(inCount) / rSquare)

samples = [10, 100, 1000, 10000]

t0 = time.time()
for s in samples:
    print("N = " + str(s) + ": " + str(pi_variant_1(s)))
t1 = time.time()
var1_time = t1 - t0
print("Time for 1st variant: " + str(var1_time))