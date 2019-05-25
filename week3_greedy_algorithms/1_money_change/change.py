# Uses python3
import sys

def get_change(m):
    #write your code here
    num_coin=0
    num_coin+=int(m/10)
    m=m%10
    num_coin+=int(m/5)
    m=m%5
    num_coin+=m
    return num_coin

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
