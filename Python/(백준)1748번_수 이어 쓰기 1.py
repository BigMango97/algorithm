# 문제
# 1부터 N까지의 수를 이어서 쓰면 다음과 같이 새로운 하나의 수를 얻을 수 있다.

# 1234567891011121314151617181920212223...

# 이렇게 만들어진 새로운 수는 몇 자리 수일까? 이 수의 자릿수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100,000,000)이 주어진다.

# 출력
# 첫째 줄에 새로운 수의 자릿수를 출력한다.

import sys
input = sys.stdin.readline
N = int(input())
s = ""
count = len(s)
for i in range(1,N+1):
    count+=len(str(i))
sys.stdout.write(str(count))



