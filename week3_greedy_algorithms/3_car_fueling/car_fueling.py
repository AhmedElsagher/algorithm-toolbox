# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    whats_left=tank
    num_refils=0
    for i in range(len(stops)-1):
        if (whats_left>0 )and((stops[i+1]-stops[i])<whats_left):
            whats_left-=(stops[i+1]-stops[i])
        elif tank>(stops[i+1]-stops[i]):
            whats_left=tank
            whats_left-=(stops[i+1]-stops[i])
            num_refils+=1
        else:
            return -1
#         print(stops[i],whats_left,num_refils)


            
    return num_refils

if __name__ == '__main__':
#     d, m = map(int, input().split())
    d=int(input())
    m=int(input())
    n=int(input())
    stops=list(map(int, input().split()))
    stops=[0]+stops+[d]
    
    print(compute_min_refills(d, m, stops))
