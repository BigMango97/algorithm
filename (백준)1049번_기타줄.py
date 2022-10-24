# 1049번 기타줄
# 문제) Day Of Mourning의 기타리스트 강토가 사용하는 기타에서 N개의 줄이 끊어졌다. 따라서 새로운 줄을 사거나 교체해야 한다. 강토는 되도록이면 돈을 적게 쓰려고 한다. 6줄 패키지를 살 수도 있고, 1개 또는 그 이상의 줄을 낱개로 살 수도 있다.
#      끊어진 기타줄의 개수 N과 기타줄 브랜드 M개가 주어지고, 각각의 브랜드에서 파는 기타줄 6개가 들어있는 패키지의 가격, 낱개로 살 때의 가격이 주어질 때, 적어도 N개를 사기 위해 필요한 돈의 수를 최소로 하는 프로그램을 작성하시오.
# 입력) 첫째 줄에 N과 M이 주어진다. N은 100보다 작거나 같은 자연수이고, M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 M개의 줄에는 각 브랜드의 패키지 가격과 낱개의 가격이 공백으로 구분하여 주어진다. 가격은 0보다 크거나 같고, 1,000보다 작거나 같은 정수이다.
# 출력) 첫째 줄에 기타줄을 적어도 N개 사기 위해 필요한 돈의 최솟값을 출력한다.
import sys
import math
N, M = map(int, sys.stdin.readline().split())
a__list = []
b__list = []
for i in range(0, M):
    a = list(map(int, sys.stdin.readline().split()))
    a__list.append(a[0])
    b__list.append(a[1])

large_num = min(a__list)
small_num = min(b__list)
total_list = []

if N <= 6:
    if large_num > small_num*N:  # 묶음으로 사는게 저렴한지
        total_list.append(small_num*N)  # 낱개로 주문
    else:
        total_list.append(large_num)  # 묶음으로 주문 5개가 필요하더라도 1세트 주문
elif N > 6:
    if (math.ceil(N/6))*large_num <= N*small_num:  # 예를 들어 19개가 필요하면 낱개로 16개 보다 세트로 4세트가 더 저렴한경우
        total_list.append(math.ceil(N/6)*large_num)
    if (N//6*large_num)+(N % 6*small_num) <= N*small_num:  # 최대한 세트로 사고 나머지는 낱개로 사는 경우
        total_list.append((N//6*large_num)+(N % 6*small_num))
    else:  # 낱개가 더 저렴한 경우
        total_list.append(N*small_num)
print(min(total_list))  # 가장 최소값
