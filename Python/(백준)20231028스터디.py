# ------------------------------------------------------
# 수열 2559번 / 실버3
# ------------------------------------------------------
import sys

input = sys.stdin.readline
N,K = map(int,input().split())

data = list(map(int,input().split()))

prefixSum = 0
prefixData = [0]

for i in data:
    prefixSum+=i
    prefixData.append(prefixSum)

maxList = []
for i in range(0,len(prefixData)-K):
    maxList.append(prefixData[i+K]-prefixData[i])
print(max(maxList))

# ------------------------------------------------------
# 블로그 21921번 / 실버3
# ------------------------------------------------------

import sys

input = sys.stdin.readline
N,K = map(int,input().split())

vistiedCountList = list(map(int,input().split()))

prefixSum = 0
prefixList = [0]
for i in vistiedCountList:
    prefixSum += i
    prefixList.append(prefixSum)

maxPrefix = 0
prefixCount = 0
for i in range(0,len(prefixList)-K):
    check = prefixList[i+K]-prefixList[i]
    if(maxPrefix < check):
        maxPrefix = check
        prefixCount=1
    elif(maxPrefix == check):
        prefixCount+=1

if(maxPrefix == 0):
    print("SAD")
else:
    print(maxPrefix)
    print(prefixCount)

# ------------------------------------------------------
# 게으른 백곰 10025번 / 실버3
# ------------------------------------------------------

# 틀린 문제, 수정 필요

# import sys

# input = sys.stdin.readline
# N,K = map(int,input().split())
# KL = K * 2 + 1 

# iceList = [0 for _ in range(1000001)]

# for i in range(0,N):
#     g, x = map(int,input().split())
#     iceList[x-1] = g

# prefixSum = 0
# prefixList = [0]
# for i in iceList:
#     prefixSum += i
#     prefixList.append(prefixSum)

# maxList = []
# for i in range(0,len(prefixList)-KL):
#     prefixValue = prefixList[i+KL] - prefixList[i]
#     maxList.append(prefixValue)
# print(max(maxList))



