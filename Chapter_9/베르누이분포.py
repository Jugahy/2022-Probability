# 팩토리얼 구현
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


# 베르누이분포의 평균, 분산
def solution(p):
    print("평균 : %f" % p)
    print("분산 : %f" % (p * (1 - p)))


# 반복 시행한 %d번 중에서 꼭 %d만 성공할 확률
def solution1(all, some, success, fail):
    print("반복 시행한 %d번 중에서 꼭 %d만 성공할 확률" % (all, some))
    c = factorial(all) / (factorial(some) * factorial(all - some))
    print(c * (success ** some) * (fail ** (all-some)))


p = 1 / 4
all = 3
some = 1
success = 1/4
fail = 3/4

print(solution1(all, some, success, fail))
