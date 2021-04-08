# Scary Da Vinci Code

count = 0

def fibo1(num):
    global count
    count += 1
    print(count)
    if num <= 1:
        return num
    else:
        return fibo1(num - 1) + fibo1(num - 2)