# 문제
# 찬우는 친구들과 고양이 카페에 가려 한다.

# 고양이 카페에는 
# $N$마리의 고양이가 있다. 
# $i$번째 고양이의 무게는 
# $w_i$이다. 찬우와 친구들은 모두 고양이를 사랑하기 때문에 무릎 위에 고양이를 정확히 
# $2$마리 데리고 있으면 행복해진다. 하지만 허약한 찬우와 친구들은 데리고 있는 두 고양이의 무게의 합이 
# $K$를 넘는다면 버티지 못할 것이다.

# 각 고양이의 무게와 한 명이 버틸 수 있는 최대 무게 
# $K$가 주어질 때 최대 몇 명이 행복해질 수 있는지 구해보자.

# 입력
# 첫째 줄에 정수 
# $N$과 
# $K$가 공백으로 구분되어 주어진다. 
# $(1 \leq N \leq 5\,000;$ 
# $1 \leq K \leq 10^9)$ 

# 둘째 줄에는 각 고양이의 무게를 의미하는 
# $N$개의 정수 
# $w_1, w_2, \dotsm, w_N$이 공백으로 구분되어 주어진다. 
# $(1 \leq w_i \leq K)$ 

# 출력
# 행복해질 수 있는 사람의 수의 최댓값을 출력한다.


import sys
input = sys.stdin.readline

N, K = map(int,input().split())
catList = list(map(int,input().split()))

catList.sort()

left = 0
right = len(catList)-1
count = 0
while left<right:
    # 합이 K보다 작으면 같으면
    if(catList[left]+catList[right]<= K):
        left+=1
        right-=1
        count+=1
    # 합이 K보다 크면
    elif(catList[left]+catList[right]> K):
        right-=1
print(count)


