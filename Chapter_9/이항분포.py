def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def solution(n, p):
    print("평균 : %f" % (n * p))
    print("분산 : %f" % (n * p * (1 - p)))


def solution1(n, x, p):
    print("반복 시행한 %d번 중에서 꼭 %d만 성공할 확률" % (n, x))
    c = factorial(n) / (factorial(x) * factorial(n - x))
    print(c * (p ** x) * ((1 - p) ** (n - x)))


n = 10
x = 2
p = 0.05

solution(n, p)
solution1(n, x, p)
