"""
이산확률분포 중 확률변수 x가 정의된 모든 곳에서 그 값이 일정한 분포
"""


def solution(n):
    print("f(%d) = {1/%d, x=1,2,3,...\n       {0, 다른 곳에서" % (n, n))
    print("평균 : %f" % ((n + 1) / 2))
    print("2차 적률 : %f" % ((n + 1) * (2 * n + 1) / 6))
    print("분산 : %f" % ((n ** 2 - 1) / 12))


print(solution(int(input())))
