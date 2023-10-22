# 문제
# 윤호는 퍼주기로 유명한 편의점 사장이다. 그의 편의점에는 특이한 임금 체계를 가지고 있다.

# 각 날마다 일의 차이때문에 일마다 급여가 정해져 있다.
# 윤호는  오차 없이 일급을 따박 따박 당일에 준다.
# 정해진 일 수 만큼만 일을 시킨다.
# 한번이라도 퇴직한 자를 다시 취직 시키지 않는다. (만약 취직을 한다면, 일을 시작 한 날부터 끝날 때까지 하루도 빠지면 안 된다.)
# 무서운 아르바이트를 짤린 준수는 n+1일 후에 001에 월세를 내야 해서 윤호가 사장으로 있는 편의점에 취직하려 한다. 다행히 주변 퇴직자들의 얘기로 급여에 관련해 파악했다. 또한 퇴직자들의 급여 통계를 통해 당장 n일 후까지 일급 정보를 알아냈다. 하지만 준수는 시험을 준비해야 하기에 최대 m일 밖에 일을 할 수 없다.

# 어제까지 과제를 제출하고 지금도 001에서 자고 있는 준수를 위해 코딩 잘하는 여러분이 일을 해서 벌 수 있는 최대 이익을 준수에게 또 알려주도록 하자.

# 입력
# 월세를 내기 바로 전 날 까지 인 n (1 ≤ n ≤ 100,000) 일과 일을 할 수 있는 날 m (0 ≤ m ≤ n) 일이 주어진다.

# 그 다음 줄 에는 1일부터 n일 까지 일급 Ti가 순서대로 주어진다. (0 < Ti ≤ 1,000,000)

# 출력
# 준수가 일을 해서 벌 수 있는 최대 이익을 출력한다.

import sys
input = sys.stdin.readline
n,m = map(int,input().split())
salaryList = list(map(int,input().split()))

totalSalaryList = [0]
totalCount = 0
# 누적합 구하기
for i in salaryList:
    totalCount+=i
    totalSalaryList.append(totalCount)

# 3일간 최대합 구하기
maxSalary = 0
for i in range(0,n-m+1):
    threeDaysSalary = totalSalaryList[m+i]-totalSalaryList[i]
    if(maxSalary < threeDaysSalary):
        maxSalary = threeDaysSalary
print(maxSalary)