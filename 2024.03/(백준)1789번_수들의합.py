# 문제
# 서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

# 입력
# 첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.

# 출력
# 첫째 줄에 자연수 N의 최댓값을 출력한다.

# 예제 입력 1 
# 200
# 예제 출력 1 
# 19

import sys
input = sys.stdin.readline
N = int(input())

totalValue = 0
value = 0
while totalValue <= N:
    value+=1
    totalValue+=value
    if N<totalValue:
        break
print(value-1)