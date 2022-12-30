# 1929번 소수구하기
# 문제) M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
# 입력) 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
# 출력) 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
import math
m, n = map(int, input().split())
# 처음에 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)
array = [True for i in range(2, 1000001)]
array[1] = 0
# 에라토스테네스의 체 알고리즘 수행
# 2부터 n의 제곱근까지의 모든 수를 확인하며
for i in range(2, int(math.sqrt(n)+1)):
    if array[i] == True:  # i가 소수인 경우(남은 수인 경우)
     # i를 제외한 i의 배수를 지우기
        j = 2  # j는 배수값을 의미함
        while i*j <= n:
            array[i*j] = False
            j += 1  # 배수를 증가시킴

# 모든 소수 출력
for i in range(m, n+1):
    if array[i]:
        print(i)
