# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(starts,ends):
    points = []
    zip_st_en=sorted(zip(starts,ends))
    starts,ends=zip(*zip_st_en)
    #write your code here
    points.append(ends[0])
    for i in range(len(starts)):
        if starts[i]<=points[-1]:
            if points[-1]>ends[i]:
                points[-1]=ends[i]
            continue
        else:
            points.append(ends[i])
    return points

if __name__ == '__main__':
    n=int(input())
    starts,ends=[],[]
    for i in range(n):
        point=list(map(int, input().split()))
        start_i,end_i=point[0],point[1]
        starts.append(start_i)
        ends.append(end_i)


#     n, *data = map(int, input.split())
#     segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(starts,ends)
    print(len(points))
    for p in points:
        print(p, end=' ')
        
