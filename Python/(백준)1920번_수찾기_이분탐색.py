# 1920번 수찾기
# 문제) N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
# 입력) 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.
# 출력) M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

# 기본 풀이
N = int(input())
A = set(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))
for i in B:
    if i in A:
        print(1, end='\n')
    else:
        print(0, end='\n')


# 이진 탐색 사용 풀이
# 이진탐색 : 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
N = int(input())
A = list(map(int, input().split()))
A.sort()  # B를 확인하여 A에 포함되어있는지 확인을 해야하므로 A를 정렬함

M = int(input())
B = list(map(int, input().split()))


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid-1
        elif array[mid] < target:
            start = mid+1
    return 0


for i in B:
    print(binary_search(A, i, 0, N-1))
