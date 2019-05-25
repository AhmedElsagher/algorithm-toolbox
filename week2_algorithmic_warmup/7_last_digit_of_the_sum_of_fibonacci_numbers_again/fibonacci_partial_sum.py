# Uses python3
import sys

def get_periodic_array(n):
    list_reminders=list()
    list_reminders.append(0)
    list_reminders.append(1)
    f1,f0=1,0
    for i in range(10000):
        f0,f1=f1%n,(f1+f0)%n
        if f0==0 and f1==1:
            return list_reminders[:-1]
        list_reminders.append(f1)
        

def fibonacci_partial_sum(from_, to):
    sum_ = 0
    periodic_array=get_periodic_array(10)
    from_=from_%len(periodic_array)
    to=to%len(periodic_array)
    if to>from_:
        sum_=sum(periodic_array[from_:to+1])
    else:
        sum_=sum(periodic_array[0:from_+1])+sum(periodic_array[to:])

#     for i in range(to + 1):
#         if i >= from_:
#             sum += current

#         current, next = next, current + next

    return sum_ % 10

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


if __name__ == '__main__':
#     input = sys.stdin.read();
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum(from_, to))