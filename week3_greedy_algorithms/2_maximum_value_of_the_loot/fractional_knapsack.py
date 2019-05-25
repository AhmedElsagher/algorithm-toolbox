# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    value_weight=[]
    for i in range(len(weights)):
        value_weight.append(values[i]/weights[i]) 
    ll=sorted(zip(value_weight,weights),reverse=True)
    value_weight,weights=zip(*ll)
    
    for i in range(len(weights)):
        if capacity>=weights[i]:
            value+=value_weight[i]*weights[i]
            capacity-=weights[i]

        else:
            value+=value_weight[i]*capacity
    return value


if __name__ == "__main__":
#     data = list(map(int, ))
    n, capacity = input().split()
    n, capacity =int( n),int( capacity )
    values=[]
    weights=[]
    for i in range(n):
        value_i, weight_i = input().split()
        value_i, weight_i = int(value_i),int(weight_i)
        values.append(value_i)
        weights.append(weight_i)
#     n, capacity =int( n),int( capacity )
#     values = data[2:(2 * n + 2):2]
#     weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
