# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)
def calc_fib_fast(n):
    if (n <= 1):
        return n
    f0=0
    f1=1
    for i in range(n-1):
        f0,f1=f1,f1+f0,
    return f1

n = int(input())
print(calc_fib_fast(n))
