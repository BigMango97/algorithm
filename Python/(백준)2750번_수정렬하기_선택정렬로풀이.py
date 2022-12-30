# 2750번 수정렬하기
# 문제) N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 입력) 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수 주어진다.
#       이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
# 출력) 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 선택정렬 예제
# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# for i in range(len(array)):
#   for j in range(i+1, len(array)):
#        if array[min_index] > array[j]:
#            min_index = j
#    array[i], array[min_index] = array[min_index], array[i]
# print(array) */

import sys
import time

# 선택정렬 프로그램 성능 측정
start_time = time.time()
A_list = []
N = int(sys.stdin.readline())
for i in range(0, N):
    A = int(sys.stdin.readline())
    A_list.append(A)
# print(A_list)

for i in range(len(A_list)):
    min_index = i
    for j in range(i+1, len(A_list)):
        if A_list[min_index] > A_list[j]:
            min_index = j
    A_list[i], A_list[min_index] = A_list[min_index], A_list[i]
# print(A_list)

for i in A_list:
    print(i)

end_time = time.time()
print('선택정렬 성능측정', end_time-start_time)
