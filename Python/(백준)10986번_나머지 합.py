# 문제
# 수 N개 A1, A2, ..., AN이 주어진다. 이때, 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램을 작성하시오.

# 즉, Ai + ... + Aj (i ≤ j) 의 합이 M으로 나누어 떨어지는 (i, j) 쌍의 개수를 구해야 한다.

# 입력
# 첫째 줄에 N과 M이 주어진다. (1 ≤ N ≤ 106, 2 ≤ M ≤ 103)

# 둘째 줄에 N개의 수 A1, A2, ..., AN이 주어진다. (0 ≤ Ai ≤ 109)

# 출력
# 첫째 줄에 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 출력한다.

import sys
input = sys.stdin.readline

N, M = map(int,input().split())
NList = list(map(int,input().split()))

NSum = 0
NSumList = [0]
for i in NList:
    NSum += i
    NSumList.append(NSum)
count = 0
for i in range(N):
    for j in range(i+1,N+1):
        if((NSumList[j]- NSumList[i]) % M ==0):
            count+=1
print(count)
