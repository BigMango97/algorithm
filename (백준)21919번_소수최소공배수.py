# 21919번 소수 최소 공배수
# 문제) 행복이는 길이가 N인 수열 A에서 소수들을 골라 최소공배수를 구해보려고 한다.
#       행복이를 도와 이를 계산해주자.
import math
import sys

N=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
my_set=set(a)
my_list=list(my_set)
my_list.sort()
max_num=my_list[-1]

array=[True for i in range(max_num+1)]

for i in range(2,int(math.sqrt(max_num)+1)):
    if array[i]==True:
        j=2
        while i*j<=max_num:
            array[i*j]=False
            j+=1
sosu=[]
for i in range(2,max_num+1):
    if array[i]:
        sosu.append(i)

tot=1
total_sosu = [i for i in my_list if i in sosu]
if len(total_sosu)==0:
    print(-1)
else :
    for i in total_sosu:
        tot*=i
    print(tot)