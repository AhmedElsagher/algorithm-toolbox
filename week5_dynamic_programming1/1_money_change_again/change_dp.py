# Uses python3
import sys
import math
def get_change(m):
    #write your code here
    coins=[1,3,4]
    changes=[0]
    for i in range(1,m+1):
        changes.append(math.inf)
        for j in coins:
            if i>=j:
                changes[-1]=min(changes[-1],changes[-1-j]+1)
                
        
    return changes[-1]

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
