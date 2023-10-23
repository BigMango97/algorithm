# 문제
# 숭실골 높은 언덕 깊은 골짜기에 출제로 고통 받는 욱제가 살고 있다!

# 욱제는 또 출제를 해야 해서 단단히 화가 났다. 그래서 욱제는 길이 N짜리 수열 A를 만들고, A를 비내림차순으로 정렬해서 수열 B를 만들어 버렸다!! 여기서 B를 출력하기만 하면 문제가 너무 쉬우니까 하나만 더 하자. 아래와 같은 질문이 무려 Q개나 주어진다!! (ㅎㅎ;; ㅈㅅ.. ㅋㅋ!!)

# L R: BL + BL+1 + ... + BR-1 + BR 을 출력한다.


# Figure 1. 모든 참가자가 문제를 풀 수 있을 것이라고 기대하는 욱제의 표정

# 욱제의 질문에 답하고 함께 엠티를 떠나자!!

# 입력
# 첫 번째 줄에 수열 A의 길이 N과 질문의 개수 Q가 공백으로 구분되어 주어진다. (1 ≤ N, Q ≤ 300,000)
# 두 번째 줄에 N개의 정수 A1, A2, ..., AN 이 공백으로 구분되어 주어진다. Ai 는 수열 A의 i 번째 수이다. (1 ≤ Ai ≤ 1,000)
# 세 번째 줄부터 Q개의 줄에 걸쳐 욱제의 질문을 의미하는 두 수 L, R이 공백으로 구분되어 주어진다. (1 ≤ L ≤ R ≤ N)
# 주어지는 모든 입력은 자연수이다.


# 문제풀이

# 수열 A의 길이 : N / 질문의 갯수 Q

import sys
input = sys.stdin.readline
N, Q = map(int,input().split()) 
AList = list(map(int,input().split()))
AList.sort()

prefixSum = 0
prefixSumList = []

for i in AList:
    prefixSum+=i
    prefixSumList.append(prefixSum)


for i in range(Q):
    start, finish = map(int,input().split()) 
    if(start==1):
        print(prefixSumList[finish-1])
    else:
        print(prefixSumList[finish-1]-prefixSumList[start-2])
