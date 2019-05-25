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

def calc_fib_fast(n):
    if (n <= 1):
        return n
    f0=0
    f1=1
    for i in range(n-1):
        f0,f1=f1,f1+f0,
    return f1

def fibonacci_sum(n):
    if n <= 1:
        return n
    periodic_array=get_periodic_array(10)
    sum_periodic_array=sum(periodic_array)
    reminder_n_m=n%len(periodic_array)
    fab_sum=sum_periodic_array*int(n/len(periodic_array))
    if reminder_n_m>0:
        sum_reminder=sum(periodic_array[:reminder_n_m+1])
        fab_sum+=sum_reminder
        
#     q=int(n/periodic_number)
#     previous = 0
#     current  = 1
#     sum      = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         sum += current

    return fab_sum%10
def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


if __name__ == '__main__':
#     input = sys.stdin.read()
    n = int(input())
    print(fibonacci_sum(n))
