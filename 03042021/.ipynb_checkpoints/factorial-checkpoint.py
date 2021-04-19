# Recursive Factorial

count = 0

def factorial(num):
    global count
    count += 1
    print(count)
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)