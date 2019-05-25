# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m
def get_periodic_number(n):
    if (n <= 1):
        return n
    f0=0
    f1=1
    for i in range(10000):
        f0,f1=f1%n,(f1+f0)%n
        if f0==0 and f1==1:
            return i+1
def calc_fib_fast(n):
    if (n <= 1):
        return n
    f0=0
    f1=1
    for i in range(n-1):
        f0,f1=f1,f1+f0,
    return f1
def get_fibonacci_huge(n, m):
    if n <= 1:
        return n

#     previous = 0
#     current  = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current
    periodic_number=get_periodic_number(m)
#     print(periodic_number)
    reminder=n%periodic_number
    rem_fab=calc_fib_fast(reminder)%m
    return rem_fab
if __name__ == '__main__':
#     input = sys.stdin.read();
    n, m = map(int, input().split())
    print(get_fibonacci_huge(n, m))
