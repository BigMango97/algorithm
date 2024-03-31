# 문제
#  
# $n$개의 자연수로 이루어진 수열이 주어질 때, 특정 구간 
# $[i,j]$ (
# $i≤j)$의 합이 
# $k$보다 큰 모든 쌍 
# $(i, j)$의 개수를 출력하시오.

# 입력
# 첫째 줄에는 자연수의 개수 
# $n$이 주어진다. (
# $1≤n≤100\,000$)

# 다음 줄에는 자연수 
# $n$개가 주어진다. 자연수는 
# $100\,000$보다 크지 않다.

# 그 다음 줄에는 자연수 
# $k$가 주어진다. (
# $1≤k≤1\,000\,000\,000$)

# 출력
# 특정 구간 
# $[i,j]$의 합이 
# $k$보다 큰 모든 쌍 
# $(i,j)$의 개수를 출력하시오.


import sys
input = sys.stdin.readline

n = int(input())
rList = list(map(int,input().split()))
k = int(input())

sumList = [0]
nSum = 0 

for i in rList:
    nSum+=i
    sumList.append(nSum)
print(sumList)

left = 0
right = 1
count = 0
while left<=right and right<=k:
    if(sumList[right]-sumList[left]<=k):
        print('1번 right',right,'left',left)
        left-=1
    else:
        print('2번 right',right,'left',left)    
        count+=1    
        right+=1
print(count)
