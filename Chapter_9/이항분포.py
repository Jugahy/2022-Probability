def solution(n, p):
    print("평균 : %f" % n * p)
    print("분산 : %f" % n * p * (1 - p))


def solution1(all, some):
    print("반복 시행한 %d번 중에서 꼭 %d만 성공할 확률" % all, some)

solution1(10, 0.05)
