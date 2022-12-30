# 1978번 소수찾기
# 문제) 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
# 입력) 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
# 출력) 주어진 수들 중 소수의 개수를 출력한다.

import math
N=int(input())
A=input().split()
A = [int(i) for i in A]
n=1000
array=[True for i in range(n+1)]

for i in range(2, int(math.sqrt(n))+1):
    if array[i]==True:
        j=2
        while i*j<=n:
            array[i*j]=False
            j+=1
            
total_list=[]            
for i in range(2,n+1):
    if array[i]:
        total_list.append(i)

new_total_list=[] 
for i in A:
    if i in total_list:
        new_total_list.append(i)
print(len(new_total_list))