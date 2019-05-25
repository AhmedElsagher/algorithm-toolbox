# Uses python3
import sys
from decimal import Decimal
def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b
def lcm(a, b):
    a=Decimal(a)
    b=Decimal(b)
    lcm_value=(a*b)/gcd(a,b)
    return Decimal(lcm_value)

#     return a*b
if __name__ == '__main__':
#     input = sys.stdin.read()
    a, b = map(int, input().split())
    print(lcm(a, b))

