# 문제
# N개의 수 A1, A2, ..., AN이 입력으로 주어진다. 총 M개의 구간 i, j가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N이 주어진다. (1 ≤ N ≤ 100,000) 둘째 줄에는 A1, A2, ..., AN이 주어진다. (-1,000 ≤ Ai ≤ 1,000) 셋째 줄에는 구간의 개수 M이 주어진다. (1 ≤ M ≤ 100,000) 넷째 줄부터 M개의 줄에는 각 구간을 나타내는 i와 j가 주어진다. (1 ≤ i ≤ j ≤ N)

# 출력
# 총 M개의 줄에 걸쳐 입력으로 주어진 구간의 합을 출력한다.

# 예제 입력 1 
# 5
# 10 20 30 40 50
# 5
# 1 3
# 2 4
# 3 5
# 1 5
# 4 4
# 예제 출력 1 
# 60
# 90
# 120
# 150
# 40
# 예제 입력 2 
# 3
# 1 0 -1
# 6
# 1 1
# 2 2
# 3 3
# 1 2
# 2 3
# 1 3
# 예제 출력 2 
# 1
# 0
# -1
# 1
# -1
# 0

import sys
input = sys.stdin.readline

N = int(input())
nList = list(map(int,input().split()))

totalSumList = [0]
sumValue = 0
for value in nList:
    sumValue += value
    totalSumList.append(sumValue)

M = int(input())
for _ in range(0,M):
   i, j = map(int,input().split()) 
   if i == 0:
        totalSum = totalSumList[j]-totalSumList[0]
        print(totalSum)
   else:
        totalSum = totalSumList[j]-totalSumList[i-1]
        print(totalSum)