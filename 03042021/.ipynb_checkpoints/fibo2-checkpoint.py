# Iterative Fibonacci

def fibo2(num):
    older = 0
    old = 1
    i = 2

    while i <= num:
        curr = old + older
        older = old
        old = curr

        i += 1

    return curr