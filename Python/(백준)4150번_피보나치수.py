# 4150번 피보나치 수
# 문제) 피보나치 수열은 다음과 같이 그 전 두 항의 합으로 계산되는 수열이다. 첫 두 항은 1로 정의된다.
#       f(1) = 1, f(2) = 1, f(n > 2) = f(n − 1) + f(n − 2)
#       정수를 입력받아, 그에 해당하는 피보나치 수를 출력하는 프로그램을 작성하여라.

import sys
sys.setrecursionlimit(10**8)
n = int(sys.stdin.readline())
d = [0]*(n+1)


def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1)+fibo(x-2)
    return d[x]


print(fibo(n))
