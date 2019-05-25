#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    a=sorted(a)
    b=sorted(b)
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = list(map(int, input().split()))
    n = int(input())
    a = list(map(int, input().split()))
    b =  list(map(int, input().split()))
    print(max_dot_product(a, b))
    
