# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

def max_pairwise_product_fast(numbers):
    n = len(numbers)
    max_number=0
    second_max=0
    for i in numbers:
#         for second in range(first + 1, n):
        if i>max_number:
            second_max=max_number
            max_number=i
        elif i>second_max:
            second_max=i
    max_product = max_number*second_max
    return max_product
if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))
