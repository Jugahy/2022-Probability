# import math
#
# print((3.4 ** 3) / 6 * (math.e ** -3.4))

def factorial(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(3))