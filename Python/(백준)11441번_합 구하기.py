# 문제
# N개의 수 A1, A2, ..., AN이 입력으로 주어진다. 총 M개의 구간 i, j가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N이 주어진다. (1 ≤ N ≤ 100,000) 둘째 줄에는 A1, A2, ..., AN이 주어진다. (-1,000 ≤ Ai ≤ 1,000) 셋째 줄에는 구간의 개수 M이 주어진다. (1 ≤ M ≤ 100,000) 넷째 줄부터 M개의 줄에는 각 구간을 나타내는 i와 j가 주어진다. (1 ≤ i ≤ j ≤ N)

# 출력
# 총 M개의 줄에 걸쳐 입력으로 주어진 구간의 합을 출력한다.


## 누적합 잘 생각하기.....!

import sys
input = sys.stdin.readline
N= int(input())
s_list = list(map(int,input().split()))

prefix = []
temp = 0

for i in s_list:
    temp+=i
    prefix.append(temp) #누적합을 prefix리스트에 추가

TEST = int(input())

for i in range(TEST):
    start, finish = map(int,input().split())
    if(start == 1):
        print(prefix[finish-1])
    else:
        print(prefix[finish-1]-prefix[start-2])

        